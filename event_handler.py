import pygame
from ship import Ship
import ship_logic


def check_events(pyg: pygame, ships: list[Ship]) -> None:
    
    for event in pyg.event.get():
        
            check_player_quit(pyg, event)
            
            check_ship_shot(event, pyg, ships)
                    
                    
def check_player_quit(pyg, event):
    if event.type == pyg.QUIT:
        pyg.quit()
    

def check_ship_shot(event, pyg, ships):
    if keydown_pressed(event, pyg) and shoot_pressed(event, pyg):
        ship_logic.shoot_ships(ships=ships, key_pressed=event.key)
        

def keydown_pressed(event, pyg):
    return event.type == pyg.KEYDOWN

        
def shoot_pressed(event, pyg):
    return event.key == pyg.K_LCTRL or event.key == pyg.K_RCTRL