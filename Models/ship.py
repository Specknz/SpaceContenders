import os
import pygame
from Models.ui import UI
from control_schemes import ControlSchemes


class Ship:
    
    SHIP_WIDTH = 50
    SHIP_HEIGHT = 40
    SHIP_SIZE = (SHIP_WIDTH, SHIP_HEIGHT)
    SHIP_MOVEMENT_SPEED = 5
    SHIP_START_Y_LOC = (UI.WIN_HEIGHT/2) - (SHIP_HEIGHT/2)
    

    def __init__(self, image_path: str, spawn_side: str) -> None:

        self.spawn_side: str = spawn_side.lower()
        self.control_scheme: dict = self._set_control_scheme()

        self.ship_sprite: pygame.Surface = self._load_sprite(image_path)
        self.ship_rect: pygame.Rect = self._load_rect()
        
        self.shot_bullets: list[pygame.Rect] = []
        self.health: int = 10

        if self.spawn_side == "left":
            self.color_text = "Yellow"
            self.color_value = UI.Colors.YELLOW

        elif self.spawn_side == "right":
            self.color_text = "Red"
            self.color_value = UI.Colors.RED


    def __repr__(self) -> str:
        return f"{self.color_text} Spaceship"


    def _load_sprite(self, image_path: str) -> pygame.Surface:

        if self.spawn_side == "left":
            rotation = 90

        elif self.spawn_side == "right":
            rotation = -90

        else:
            raise Exception(f'No valid spawn side argument given for {image_path}')

        sprite_loaded = pygame.image.load(os.path.join('Assets', image_path))
        sprite_scaled = pygame.transform.scale(sprite_loaded, Ship.SHIP_SIZE)
        sprite_rotated = pygame.transform.rotate(sprite_scaled, rotation)

        return sprite_rotated


    def _load_rect(self) -> pygame.Rect:
        if self.spawn_side == "left":
            amount = 0.25

        elif self.spawn_side == "right":
            amount = 0.75

        ship_start_x_loc = (UI.WIN_WIDTH*amount) - (Ship.SHIP_WIDTH/2)

        return pygame.Rect(
                ship_start_x_loc, 
                Ship.SHIP_START_Y_LOC, 
                Ship.SHIP_WIDTH,
                Ship.SHIP_HEIGHT)


    def _set_control_scheme(self) -> dict:
        if self.spawn_side == "left":
            return ControlSchemes.LEFT_CONTROLS

        elif self.spawn_side == "right":
            return ControlSchemes.RIGHT_CONTROLS