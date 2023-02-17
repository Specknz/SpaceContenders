import pygame
import ship_logic
from Stores.ships_store import ShipsStore


class EventHandler:
    
    def __init__(self, pyg: pygame, ships_store: ShipsStore):
        self._pyg: pygame = pyg
        self._ships_store: ShipsStore = ships_store


    def check_events(self) -> None:
        for event in self._pyg.event.get():
                self._check_player_quit(event)
                self._check_ship_shot(event)
                        
                        
    def _check_player_quit(self, event) -> None:
        if event.type == self._pyg.QUIT:
            self._pyg.quit()
        

    def _check_ship_shot(self, event) -> None:
        if self._keydown_pressed(event):
            if self._shoot_pressed(event):
                ship_logic.shoot_ships(self._ships_store.ships, event.key)
            

    def _keydown_pressed(self, event) -> bool:
        return event.type == self._pyg.KEYDOWN

            
    def _shoot_pressed(self, event) -> bool:
        return event.key == self._pyg.K_LCTRL or event.key == self._pyg.K_RCTRL