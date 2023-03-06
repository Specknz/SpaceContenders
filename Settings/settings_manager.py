import json

class SettingsManager:

    def __init__(self) -> None:
        self.__settings = self.load_settings()
        
        self.fps = self.__settings["FPS"]
        self.font_path = self.__settings["FontPath"]
        self.ship_health = self.__settings["ShipHealth"]
        
        
    def load_settings(self):
        with open("Settings\settings.json") as settings:
            return json.load(settings)