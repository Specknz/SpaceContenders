from Config.isettings import ISettings
from Config.settings import Settings


def settings() -> ISettings:
    return Settings()