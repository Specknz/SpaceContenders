import json

from Config.isettings import ISettings


class Settings(ISettings):

    def __init__(self) -> None:
        self.settings = self.__load_settings()
        
        self.ship_health: int = self.settings["ShipHealth"]
        self.fps: int = self.settings["FPS"]
        self.font_path: str = self.settings["FontPath"]
        self.shoot_sfx_path: str = self.settings["ShootSFXPath"]
        self.explosion_sfx_path: str = self.settings["ExplosionSFXPath"]
        
        
    def __load_settings(self):
        with open("Config\settings.json") as settings:
            return json.load(settings)