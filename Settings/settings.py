import json

from Settings.isettings import ISettings


class Settings(ISettings):

    def __init__(self) -> None:
        self.__settings = self.__load_settings()
        
        self.ship_health: int = self.__settings["ShipHealth"]
        self.fps: int = self.__settings["FPS"]
        self.font_path: str = self.__settings["FontPath"]
        
        
    def __load_settings(self):
        with open("Settings\settings.json") as settings:
            return json.load(settings)