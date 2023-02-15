import pygame
from game_parameters import GameParameters
from ship import Ship
from .game import ship_logic

def check_events(pyg: pygame, ships: list[Ship]) -> None:
    
    for event in pyg.event.get():

            # Check if player has quit
            if check_for_quit(pyg, event):
                break

            # Check if ship has shot
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LCTRL or event.key == pyg.K_RCTRL:
                    ship_logic.shoot_ships(ships=ships, key_pressed=event.key)
                    
                    
def check_for_quit(pyg, event):
    if event.type == pyg.QUIT:
        GameParameters.game_running = False
        return True 
    
    
