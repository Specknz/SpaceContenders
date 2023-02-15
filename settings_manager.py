import json

class SettingsManager:
    
    def __init__(self) -> None:
        self.settings = self.load_settings()
        
        
    def load_settings(self):
        with open("settings.json") as settings:
            return json.load(settings)