from dataclasses import dataclass, field
import logging
import pygame
from Models.bullet import Bullet
from Models.spawn_side import SpawnSide


@dataclass
class Ship:
    
    WIDTH = 50
    HEIGHT = 40
    SIZE = (WIDTH, HEIGHT)
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
        