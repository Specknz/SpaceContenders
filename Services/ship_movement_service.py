import pygame
import logging
from Models.ship import Ship
from Views.game_view import GameView
from Windows.main_window import MainWindow


def move(ship: Ship, keys_pressed):
    if keys_pressed[ship.control_scheme["LEFT"]]:
        __move_x(ship, -(ship.MOVE_SPEED) )
        
    if keys_pressed[ship.control_scheme["RIGHT"]]:
        __move_x(ship, ship.MOVE_SPEED)
        
    if keys_pressed[ship.control_scheme["UP"]]:
        __move_y(ship, -(ship.MOVE_SPEED) )

    if keys_pressed[ship.control_scheme["DOWN"]]:
        __move_y(ship, ship.MOVE_SPEED)


def __move_x(ship: Ship, amount_to_move):
    next_position: pygame.Rect = __get_next_position(ship, 'x', amount_to_move)
    
    if (next_position.x > 0) and (next_position.x + ship.HEIGHT < MainWindow.WIDTH) and not (next_position.colliderect(GameView.CENTER_LINE)):
        ship.rect.x += amount_to_move
        logging.debug(f"{ship.color_text} ship moved {'Right' if amount_to_move > 0 else 'Left'}")
        return
    
    if next_position.colliderect(GameView.CENTER_LINE):
        logging.debug(f"{ship.color_text} ship colliding with center line")
        return
    
    logging.debug(f"{ship.color_text} ship colliding with outer wall")
        
        
def __move_y(ship: Ship, amount_to_move):
    next_position: pygame.Rect = __get_next_position(ship, 'y', amount_to_move)
    
    if (next_position.y > 0) and (next_position.y + ship.WIDTH < MainWindow.HEIGHT):
        ship.rect.y += amount_to_move
        logging.debug(f"{ship.color_text} ship moved {'Down' if amount_to_move > 0 else 'Up'}")
        return
    
    logging.debug(f"{ship.color_text} ship colliding with outer wall")
    

def __get_next_position(ship: Ship, axis, amount_to_move) -> pygame.Rect:
    if axis == 'x':
        return pygame.Rect(ship.rect.x + amount_to_move, 
                            ship.rect.y, 
                            ship.HEIGHT, 
                            ship.WIDTH)
    elif axis == 'y':
        return pygame.Rect(ship.rect.x, 
                            ship.rect.y + amount_to_move, 
                            ship.HEIGHT, 
                            ship.WIDTH)