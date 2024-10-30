import os
from pathlib import Path

from ..__version__ import __title__


DEFAULT_SETTINGS = {
    "message/check_missed/notify": True,
    "locale": False,
    "logging/level": "Disabled",
    "export/path": os.path.join(
        Path.home(), f"{__title__.replace(' ', '-').lower()}-settings.bytes"
    ),
    "shortcuts/quit": "Ctrl+Q",
    "tray/notifications/priority": 5,
    "tray/notifications/duration_ms": 5000,
    "tray/notifications/icon/show": True,
    "tray/notifications/click": True,
    "tray/icon/unread": False,
    "watchdog/enabled": True,
    "watchdog/interval/s": 60,
    "MessageWidget/height/min": 100,
    "MessageWidget/image/size": 33,
    "MessageWidget/content_image/W_percentage": 1.0,
    "MessageWidget/content_image/H_percentage": 0.5,
    "MessageWidget/priority_color": True,
    "MessageWidget/image_urls": True,
    "MainWindow/label/size": 25,
    "MainWindow/button/size": 33,
    "MainWindow/application/icon/size": 40,
    "ApplicationModel/sort": False,
    "ImagePopup/enabled": False,
    "ImagePopup/extensions": [".jpg", ".jpeg", ".png", ".svg"],
    "ImagePopup/w": 400,
    "ImagePopup/h": 400,
}
