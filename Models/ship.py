import pygame
from Models.ui import UI


class Ship:
    
    WIDTH = 50
    HEIGHT = 40
    SIZE = (WIDTH, HEIGHT)
    MOVE_SPEED = 5
    
    def __init__(self, 
                 spawn_side: str,
                 color_text: str, 
                 color_value: set, 
                 control_scheme: dict,
                 ship_sprite: pygame.Surface,
                 ship_rect: pygame.Rect) -> None:

        self.spawn_side = spawn_side.lower()

        self.color_text: str = color_text
        self.color_value: set = color_value
        
        self.control_scheme: dict = control_scheme
        
        self.ship_sprite: pygame.Surface = ship_sprite
        self.ship_rect: pygame.Rect = ship_rect
 
        self.shot_bullets: list[pygame.Rect] = []
        self.health: int = 10


    def __repr__(self) -> str:
        return f"{self.color_text} Spaceship"
