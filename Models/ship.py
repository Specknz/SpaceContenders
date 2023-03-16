import logging
import pygame

from dataclasses import dataclass, field
from Models.bullet import Bullet
from Models.spawn_side import SpawnSide
from Config.isettings import ISettings


@dataclass
class Ship:
    
    HEIGHT = 50
    WIDTH = 40
    SIZE = (HEIGHT, WIDTH)
    MOVE_SPEED = 4
    MAX_BULLETS = 6
    
    spawn_side: SpawnSide
    color_text: str
    color_value: set
    control_scheme: dict
    health: int
    sprite: pygame.Surface
    rect: pygame.Rect
    shot_bullets: list[Bullet] = field(default_factory = list)
        

    def __repr__(self) -> str:
        return f"{self.color_text} Spaceship"
            
    
    def damage(self):
        self.health -= 1
        logging.debug(f"{self.color_text} ship was damaged - New health value: {self.health}")
        