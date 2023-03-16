import pygame

from Config.isettings import ISettings


class AudioService():
    def __init__(self, pyg: pygame, settings: ISettings) -> None:
        self.pyg = pyg
        self.settings = settings
        
        self.shoot_sfx = pyg.mixer.Sound(settings.shoot_sfx_path)
        self.explosion_sfx = pyg.mixer.Sound(settings.explosion_sfx_path)
 
    def shoot(self):
        self.shoot_sfx.play()
        
    def explosion(self):
        self.explosion_sfx.play()