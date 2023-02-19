import pygame
from Models.ship import Ship


class EventHandler:
    def __init__(self, pyg: pygame, ships: list[Ship]):
        self.__pyg: pygame = pyg
        self.__ships: list[Ship] = ships


    def handle_events(self) -> None:
        for event in self.__pyg.event.get():
                self.__handle_quit(event)
                self.__handle_key_presses(event)
                        
                        
    def __handle_quit(self, event) -> None:
        if event.type == self.__pyg.QUIT:
            self.__pyg.quit()
    
    
    def __key_pressed(self, event_type) -> bool:
        return event_type == self.__pyg.KEYDOWN    


    def __handle_key_presses(self, event) -> None:
        if self.__key_pressed(event.type):
            for ship in self.__ships:
                
                if self.__shoot_key_pressed(event.key, ship):
                    ship.shoot()
                    
                if self.__move_key_pressed(event.key, ship):
                    ship.move(event.key)
                    
    
    def __shoot_key_pressed(self, key, ship: Ship) -> bool:
        return key == ship.control_scheme["SHOOT"]
    
    
    def __move_key_pressed(self, key, ship: Ship):
        return key in (ship.control_scheme["LEFT"], 
                       ship.control_scheme["UP"], 
                       ship.control_scheme["RIGHT"], 
                       ship.control_scheme["DOWN"])