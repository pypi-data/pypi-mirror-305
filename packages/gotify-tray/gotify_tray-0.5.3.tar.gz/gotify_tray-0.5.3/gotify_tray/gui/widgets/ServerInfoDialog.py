import os

from gotify_tray.database import Settings
from gotify_tray.gotify.models import GotifyVersionModel
from gotify_tray.tasks import ImportSettingsTask, VerifyServerInfoTask
from gotify_tray.utils import update_widget_property
from PyQt6 import QtWidgets

from ..designs.widget_server import Ui_Dialog


settings = Settings("gotify-tray")


class ServerInfoDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, url: str = "", token: str = "", enable_import: bool = True):
        super(ServerInfoDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Server info")
        self.line_url.setPlaceholderText("https://gotify.example.com")
        self.line_url.setText(url)
        self.line_token.setText(token)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setDisabled(True)
        self.pb_import.setVisible(enable_import)
        self.link_callbacks()

    def test_server_info(self):
        update_widget_property(self.pb_test, "state", "")
        update_widget_property(self.line_url, "state", "")
        update_widget_property(self.line_token, "state", "")
        self.label_server_info.clear()

        url = self.line_url.text()
        client_token = self.line_token.text()
        if not url or not client_token:
            return

        self.pb_test.setDisabled(True)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setDisabled(True)

        self.task = VerifyServerInfoTask(url, client_token)
        self.task.success.connect(self.server_info_success)
        self.task.incorrect_token.connect(self.incorrect_token_callback)
        self.task.incorrect_url.connect(self.incorrect_url_callback)
        self.task.start()

    def server_info_success(self):
        self.pb_test.setEnabled(True)
        update_widget_property(self.pb_test, "state", "success")
        update_widget_property(self.line_token, "state", "success")
        update_widget_property(self.line_url, "state", "success")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(True)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setFocus()

    def incorrect_token_callback(self):
        self.pb_test.setEnabled(True)
        update_widget_property(self.pb_test, "state", "failed")
        update_widget_property(self.line_token, "state", "failed")
        update_widget_property(self.line_url, "state", "success")
        self.line_token.setFocus()

    def incorrect_url_callback(self):
        self.pb_test.setEnabled(True)
        self.label_server_info.clear()
        update_widget_property(self.pb_test, "state", "failed")
        update_widget_property(self.line_token, "state", "success")
        update_widget_property(self.line_url, "state", "failed")
        self.line_url.setFocus()

    def input_changed_callback(self):
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setDisabled(True)
        update_widget_property(self.pb_test, "state", "")

    def import_success_callback(self):
        self.line_url.setText(settings.value("Server/url", type=str))
        self.line_token.setText(settings.value("Server/client_token"))

    def import_callback(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(
            self, "Import Settings", settings.value("export/path", type=str), "*",
        )[0]
        if fname and os.path.exists(fname):
            self.import_settings_task = ImportSettingsTask(fname)
            self.import_settings_task.success.connect(self.import_success_callback)
            self.import_settings_task.start()

    def link_callbacks(self):
        self.pb_test.clicked.connect(self.test_server_info)
        self.line_url.textChanged.connect(self.input_changed_callback)
        self.line_token.textChanged.connect(self.input_changed_callback)
        self.pb_import.clicked.connect(self.import_callback)
