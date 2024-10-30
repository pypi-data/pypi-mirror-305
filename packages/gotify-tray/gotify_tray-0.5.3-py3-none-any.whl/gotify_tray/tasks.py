import abc
import glob
import logging
import time
import os

from functools import reduce
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal

from gotify_tray.database import Cache, Settings
from gotify_tray.gotify.models import GotifyVersionModel
from gotify_tray.utils import process_messages

from . import gotify


settings = Settings("gotify-tray")
logger = logging.getLogger("gotify-tray")


class BaseTask(QtCore.QThread):
    failed = pyqtSignal()

    def __init__(self):
        super(BaseTask, self).__init__()
        self.running = False
        self._abort = False

    @abc.abstractmethod
    def task(self):
        ...

    def abort(self):
        self._abort = True

    def abort_requested(self) -> bool:
        return self._abort

    def run(self):
        self.running = True
        try:
            self.task()
        except Exception as e:
            logger.error(f"{self.__class__.__name__} failed: {e}")
            self.failed.emit()
        finally:
            self.running = False


class DeleteMessageTask(BaseTask):
    success = pyqtSignal()
    error = pyqtSignal(gotify.GotifyErrorModel)

    def __init__(self, message_id: int, gotify_client: gotify.GotifyClient):
        super(DeleteMessageTask, self).__init__()
        self.message_id = message_id
        self.gotify_client = gotify_client

    def task(self):
        result = self.gotify_client.delete_message(self.message_id)
        if isinstance(result, gotify.GotifyErrorModel):
            self.error.emit(result)
        else:
            self.success.emit()


class DeleteApplicationMessagesTask(BaseTask):
    success = pyqtSignal()
    error = pyqtSignal(gotify.GotifyErrorModel)

    def __init__(self, appid: int, gotify_client: gotify.GotifyClient):
        super(DeleteApplicationMessagesTask, self).__init__()
        self.appid = appid
        self.gotify_client = gotify_client

    def task(self):
        result = self.gotify_client.delete_application_messages(self.appid)
        if isinstance(result, gotify.GotifyErrorModel):
            self.error.emit(result)
        else:
            self.success.emit()


class DeleteAllMessagesTask(BaseTask):
    success = pyqtSignal()
    error = pyqtSignal(gotify.GotifyErrorModel)

    def __init__(self, gotify_client: gotify.GotifyClient):
        super(DeleteAllMessagesTask, self).__init__()
        self.gotify_client = gotify_client

    def task(self):
        result = self.gotify_client.delete_messages()
        if isinstance(result, gotify.GotifyErrorModel):
            self.error.emit(result)
        else:
            self.success.emit()


class GetApplicationsTask(BaseTask):
    success = pyqtSignal(list)
    error = pyqtSignal(gotify.GotifyErrorModel)

    def __init__(self, gotify_client: gotify.GotifyClient):
        super(GetApplicationsTask, self).__init__()
        self.gotify_client = gotify_client

    def task(self):
        result = self.gotify_client.get_applications()
        if isinstance(result, gotify.GotifyErrorModel):
            self.error.emit(result)
        else:
            self.success.emit(result)


class GetApplicationMessagesTask(BaseTask):
    message = pyqtSignal(gotify.GotifyMessageModel)
    error = pyqtSignal(gotify.GotifyErrorModel)

    def __init__(self, appid: int, gotify_client: gotify.GotifyClient):
        super(GetApplicationMessagesTask, self).__init__()
        self.appid = appid
        self.gotify_client = gotify_client

    def task(self):
        result = self.gotify_client.get_application_messages(self.appid)
        if isinstance(result, gotify.GotifyErrorModel):
            self.error.emit(result)
        else:
            for message in process_messages(result.messages):
                if self.abort_requested():
                    return
                self.message.emit(message)
                
                # Prevent locking up the UI when there are a lot of messages ready at the same time
                # -- side effect: switching application while the previous messages are still being inserted causes mixing of messages
                time.sleep(0.001)


class GetMessagesTask(BaseTask):
    message = pyqtSignal(gotify.GotifyMessageModel)
    success = pyqtSignal(gotify.GotifyPagedMessagesModel)
    error = pyqtSignal(gotify.GotifyErrorModel)

    def __init__(self, gotify_client: gotify.GotifyClient):
        super(GetMessagesTask, self).__init__()
        self.gotify_client = gotify_client

    def task(self):
        result = self.gotify_client.get_messages()
        if isinstance(result, gotify.GotifyErrorModel):
            self.error.emit(result)
        else:
            for message in process_messages(result.messages):
                if self.abort_requested():
                    return
                self.message.emit(message)
                time.sleep(0.001)
            self.success.emit(result)


class ProcessMessageTask(BaseTask):
    def __init__(self, message: gotify.GotifyMessageModel):
        super(ProcessMessageTask, self).__init__()
        self.message = message

    def task(self):
        for _ in process_messages([self.message]):
            pass


class VerifyServerInfoTask(BaseTask):
    success = pyqtSignal()
    incorrect_token = pyqtSignal()
    incorrect_url = pyqtSignal()

    def __init__(self, url: str, client_token: str):
        super(VerifyServerInfoTask, self).__init__()
        self.url = url
        self.client_token = client_token

    def task(self):
        try:
            gotify_client = gotify.GotifyClient(self.url, self.client_token)

            result = gotify_client.get_messages(limit=1)

            if isinstance(result, gotify.GotifyPagedMessagesModel):
                self.success.emit()
                return
            elif (
                isinstance(result, gotify.GotifyErrorModel)
                and result["error"] == "Unauthorized"
            ):
                self.incorrect_token.emit()
                return
            self.incorrect_url.emit()
        except Exception as e:
            self.incorrect_url.emit()


class ServerConnectionWatchdogTask(BaseTask):
    closed = pyqtSignal()

    def __init__(self, gotify_client: gotify.GotifyClient):
        super(ServerConnectionWatchdogTask, self).__init__()
        self.gotify_client = gotify_client

    def task(self):
        while True:
            time.sleep(settings.value("watchdog/interval/s", type=int))
            if not self.gotify_client.is_listening():
                self.closed.emit()
                logger.debug("ServerConnectionWatchdogTask: gotify_client is not listening")


class ExportSettingsTask(BaseTask):
    success = pyqtSignal()

    def __init__(self, path: str):
        super(ExportSettingsTask, self).__init__()
        self.path = path

    def task(self):
        settings.export(self.path)
        self.success.emit()


class ImportSettingsTask(BaseTask):
    success = pyqtSignal()

    def __init__(self, path: str):
        super(ImportSettingsTask, self).__init__()
        self.path = path

    def task(self):
        settings.load(self.path)
        self.success.emit()


class CacheSizeTask(BaseTask):
    size = pyqtSignal(int)

    def task(self):        
        cache_dir = Cache().directory()
        if os.path.exists(cache_dir):
            cache_size_bytes = reduce(lambda x, f: x + os.path.getsize(f), glob.glob(os.path.join(cache_dir, "*")), 0)
            self.size.emit(cache_size_bytes)

class ClearCacheTask(BaseTask):        
    def task(self):
        cache = Cache()
        cache.clear()
        