import os

# DOCKER ENVIRONMENT VARIABLES
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_ADMIN = os.environ.get("TELEGRAM_ADMIN")
TELEGRAM_GROUP = os.environ.get("TELEGRAM_GROUP")
TELEGRAM_NOTIFICATION_CHANNEL = os.environ.get("TELEGRAM_NOTIFICATION_CHANNEL")
TELEGRAM_THREAD = os.environ.get("TELEGRAM_THREAD")
CHECK_UPDATES = bool(int(os.environ.get("CHECK_UPDATES")))
CHECK_UPDATE_EVERY_HOURS = float(os.environ.get("CHECK_UPDATE_EVERY_HOURS"))
CHECK_UPDATE_STOPPED_CONTAINERS = bool(int(os.environ.get("CHECK_UPDATE_STOPPED_CONTAINERS")))
CONTAINER_NAME = os.environ.get("CONTAINER_NAME")
LANGUAGE = os.environ.get("LANGUAGE")
EXTENDED_MESSAGES = bool(int(os.environ.get("EXTENDED_MESSAGES")))
BUTTON_COLUMNS = int(os.environ.get("BUTTON_COLUMNS"))
GROUPED_UPDATES = bool(int(os.environ.get("GROUPED_UPDATES")))

# CONSTANTS
UPDATER_IMAGE = "dgongut/docker-container-updater:latest"
UPDATER_CONTAINER_NAME = "UPDATER-Docker-Controler-Bot"
CONTAINER_ID_LENGTH = 5
ANONYMOUS_USER_ID = "1087968824"
SCHEDULE_PATH = "/app/schedule"
SCHEDULE_FILE = "schedule.txt"
MUTE_FILE = ".muted_until"
FULL_SCHEDULE_PATH = f'{SCHEDULE_PATH}/{SCHEDULE_FILE}'
FULL_MUTE_FILE_PATH = f'{SCHEDULE_PATH}/{MUTE_FILE}'

# LABELS
LABEL_IGNORE_CHECK_UPDATES = "DCB-Ignore-Check-Updates"
LABEL_AUTO_UPDATE = "DCB-Auto-Update"

docker_architectures = {
    "x86_64": "amd64",
    "i386": "i386",
    "386": "386",
    "amd64": "amd64",
    "arm": "arm32v7",
    "arm64": "arm64",
    "ppc64le": "ppc64le",
    "s390x": "s390x",
    "unknown": "unknown",
}
