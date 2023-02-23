import json

class SettingsManager:
    
    def __init__(self) -> None:
        self.__settings = self.load_settings()
        
        self.ship_health = self.__settings["ShipHealth"]
        self.fps = self.__settings["FPS"]
        
        
    def load_settings(self):
        with open("Settings\settings.json") as settings:
            return json.load(settings)