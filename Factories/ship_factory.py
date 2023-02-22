import os
import pygame
from Models.ship import Ship
from Models.ui import UI
from Settings.colors import Colors
from Settings.control_schemes import ControlSchemes


class ShipFactory:
    
    
    # SHIPS = [
    #     {
    #         "spawn_side" : "left",
    #         "color_text" : "Yellow",
    #         "color_value" : Colors.YELLOW,
    #         "control_scheme" : ControlSchemes.LEFT_CONTROLS_1,
    #         "sprite_path" : "ship_yellow.png",
    #         "rotation" : 90
    #     }
    # ]
    
    
    # def create_ships():
    #     pass
    
    
    def create_1v1_ships(self) -> list[Ship]:

        return [
            self.__create_left_side_ship(),
            self.__create_right_side_ship()
        ]
        
        
    def __create_left_side_ship(self) -> Ship:
        return Ship(spawn_side = "left",
                 color_text = "Yellow",
                 color_value = Colors.YELLOW,
                 control_scheme = ControlSchemes.LEFT_CONTROLS_1,
                 sprite = self._load_ship_sprite("ship_yellow.png", rotation = 90),
                 rect = self._load_ship_rect(start_x_loc = self.__get_spawn_x_loc(0.25),
                                             start_y_loc = self.__get_spawn_y_loc(2))
                 )
    
    
    def __create_right_side_ship(self) -> Ship:
        return Ship(spawn_side = "right",
                 color_text = "Red",
                 color_value = Colors.RED,
                 control_scheme = ControlSchemes.RIGHT_CONTROLS_1,
                 sprite = self._load_ship_sprite("ship_red.png", rotation = -90),
                 rect = self._load_ship_rect(start_x_loc = self.__get_spawn_x_loc(0.75),
                                             start_y_loc = self.__get_spawn_y_loc(2))
                 )
    
    
    # def __create_ship(self, rotation, spawn_x_loc: Callable[[int], int], spawn_y_loc: Callable[[int], int]):
    #     return Ship(spawn_side = "right",
    #              color_text = "Red",
    #              color_value = Colors.RED,
    #              control_scheme = ControlSchemes.RIGHT_CONTROLS_1,
    #              sprite = self._load_ship_sprite("ship_red.png", rotation),
    #              rect = self._load_ship_rect(start_x_loc = spawn_x_loc(), 
    #                                          start_y_loc = spawn_y_loc())
    #              )
        
    def __get_spawn_x_loc(self, x_pos_of_window):
        return (UI.WIN_WIDTH*x_pos_of_window) - (Ship.WIDTH/2)
    
    
    def __get_spawn_y_loc(self, total_num_of_ships):
        return (UI.WIN_HEIGHT/total_num_of_ships) - (Ship.HEIGHT/2)
        
        
    def _load_ship_sprite(self, image_path: str, rotation: int) -> pygame.Surface:
        sprite_loaded = pygame.image.load(os.path.join('Assets', image_path))
        sprite_scaled = pygame.transform.scale(sprite_loaded, Ship.SIZE)
        sprite_rotated = pygame.transform.rotate(sprite_scaled, rotation)

        return sprite_rotated
    
    
    def _load_ship_rect(self, start_x_loc, start_y_loc) -> pygame.Rect:
        return pygame.Rect(
                start_x_loc, 
                start_y_loc, 
                Ship.HEIGHT,
                Ship.WIDTH)