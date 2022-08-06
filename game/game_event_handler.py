import pygame
from game.game_parameters import GameParameters
from ship.ship import Ship
from ship import ship_logic

def check_events(pyg: pygame, ships: list[Ship]) -> None:
    
    for event in pyg.event.get():

            # Check if player has quit
            if event.type == pyg.QUIT:
                GameParameters.game_running = False
                break

            # Check if ship has shot
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LCTRL or event.key == pyg.K_RCTRL:
                    ship_logic.shoot_ships(ships=ships, key_pressed=event.key)