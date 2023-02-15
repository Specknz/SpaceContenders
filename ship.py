import os
import pygame
from ui_parameters import UIParameters
from ship_parameters import ShipParameters


class Ship:

    def __init__(self, image_path: str, spawn_side: str) -> None:

        self.spawn_side: str = spawn_side.lower()
        self.control_scheme = self.__set_control_scheme()

        self.ship_sprite: pygame.Surface = self.__load_sprite(image_path)
        self.ship_rect: pygame.Rect = self.__load_rect()
        self.shot_bullets: list[pygame.Rect] = []
        self.health: int = 10

        if self.spawn_side == "left":
            self.color_text = "Yellow"
            self.color_value = UIParameters.Colors.YELLOW

        elif self.spawn_side == "right":
            self.color_text = "Red"
            self.color_value = UIParameters.Colors.RED


    def __repr__(self) -> str:
        return f"{self.color_text} Spaceship"


    def __load_sprite(self, image_path: str) -> pygame.Surface:

        if self.spawn_side == "left":
            rotation = 90

        elif self.spawn_side == "right":
            rotation = -90

        else:
            raise Exception(f'No valid spawn side argument given for {image_path}')

        sprite_loaded = pygame.image.load(os.path.join('Assets', image_path))
        sprite_scaled = pygame.transform.scale(sprite_loaded, ShipParameters.SHIP_SIZE)
        sprite_rotated = pygame.transform.rotate(sprite_scaled, rotation)

        return sprite_rotated


    def __load_rect(self) -> pygame.Rect:
        if self.spawn_side == "left":
            amount = 0.25

        elif self.spawn_side == "right":
            amount = 0.75

        ship_start_x_loc = (UIParameters.WIN_WIDTH*amount) - (ShipParameters.SHIP_WIDTH/2)

        return pygame.Rect(
                ship_start_x_loc, 
                ShipParameters.SHIP_START_Y_LOC, 
                ShipParameters.SHIP_WIDTH,
                ShipParameters.SHIP_HEIGHT)


    def __set_control_scheme(self) -> dict:
        if self.spawn_side == "left":
            return ShipParameters.LEFT_CONTROLS

        elif self.spawn_side == "right":
            return ShipParameters.RIGHT_CONTROLS