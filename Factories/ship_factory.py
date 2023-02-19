import os
import pygame
from Models.ship import Ship
from Models.ui import UI
from Settings.colors import Colors
from Settings.control_schemes import ControlSchemes


class ShipFactory:
    
    def create_1v1_ships(self) -> list[Ship]:

        return [
            Ship(spawn_side = "left",
                 color_text = "Yellow",
                 color_value = Colors.YELLOW,
                 control_scheme = ControlSchemes.LEFT_CONTROLS,
                 sprite = self._load_ship_sprite("ship_yellow.png", rotation = 90),
                 rect = self._load_ship_rect(start_x_loc = self.__get_spawn_x_loc(0.25),
                                                  start_y_loc = self.__get_spawn_y_loc(0.5))
                 ),
            
            Ship(spawn_side = "right",
                 color_text = "Red",
                 color_value = Colors.RED,
                 control_scheme = ControlSchemes.RIGHT_CONTROLS,
                 sprite = self._load_ship_sprite("ship_red.png", rotation = -90),
                 rect = self._load_ship_rect(start_x_loc = self.__get_spawn_x_loc(0.75),
                                                  start_y_loc = self.__get_spawn_y_loc(0.5))
                 )
        ]
        
        
    def __get_spawn_x_loc(self, x_pos_of_window):
        return (UI.WIN_WIDTH*x_pos_of_window) - (Ship.WIDTH/2)
    
    
    def __get_spawn_y_loc(self, y_pos_of_window):
        return (UI.WIN_HEIGHT*y_pos_of_window) - (Ship.HEIGHT/2)
        
        
    def _load_ship_sprite(self, image_path: str, rotation: int) -> pygame.Surface:
        sprite_loaded = pygame.image.load(os.path.join('Assets', image_path))
        sprite_scaled = pygame.transform.scale(sprite_loaded, Ship.SIZE)
        sprite_rotated = pygame.transform.rotate(sprite_scaled, rotation)

        return sprite_rotated
    
    
    def _load_ship_rect(self, start_x_loc, start_y_loc) -> pygame.Rect:
        return pygame.Rect(
                start_x_loc, 
                start_y_loc, 
                Ship.WIDTH,
                Ship.HEIGHT)