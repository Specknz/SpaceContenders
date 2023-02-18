import os
import pygame
from Models.ship import Ship
from Models.ui import UI
from control_schemes import ControlSchemes


class ShipFactory:
    
    def create_1v1_ships(self) -> list[Ship]:

        return [
            Ship(spawn_side = "left",
                 color_text = "Yellow",
                 color_value = UI.Colors.YELLOW,
                 control_scheme = ControlSchemes.LEFT_CONTROLS,
                 ship_sprite = self._load_ship_sprite("ship_yellow.png", rotation = 90),
                 ship_rect = self._load_ship_rect(start_x_loc = self._set_start_x_loc(0.25),
                                                  start_y_loc = self._set_start_y_loc(2))),
            
            Ship(spawn_side = "right",
                 color_text = "Red",
                 color_value = UI.Colors.RED,
                 control_scheme = ControlSchemes.RIGHT_CONTROLS,
                 ship_sprite = self._load_ship_sprite("ship_red.png", rotation = -90),
                 ship_rect = self._load_ship_rect(start_x_loc = self._set_start_x_loc(0.75),
                                                  start_y_loc = self._set_start_y_loc(2))),
        ]
        
        
    def _set_start_x_loc(self, amount):
        return (UI.WIN_WIDTH*amount) - (Ship.WIDTH/2)
    
    
    def _set_start_y_loc(self, amount):
        return (UI.WIN_HEIGHT/amount) - (Ship.HEIGHT/2)
        
        
    def _load_ship_sprite(self, image_path: str, rotation: int) -> pygame.Surface:

        # if self.spawn_side == "left":
        #     rotation = 90

        # elif self.spawn_side == "right":
        #     rotation = -90

        # else:
        #     raise Exception(f'No valid spawn side argument given for {image_path}')

        sprite_loaded = pygame.image.load(os.path.join('Assets', image_path))
        sprite_scaled = pygame.transform.scale(sprite_loaded, Ship.SIZE)
        sprite_rotated = pygame.transform.rotate(sprite_scaled, rotation)

        return sprite_rotated
    
    
    def _load_ship_rect(self, start_x_loc, start_y_loc) -> pygame.Rect:
        # if self.spawn_side == "left":
        #     amount = 0.25

        # elif self.spawn_side == "right":
        #     amount = 0.75

        return pygame.Rect(
                start_x_loc, 
                start_y_loc, 
                Ship.WIDTH,
                Ship.HEIGHT)