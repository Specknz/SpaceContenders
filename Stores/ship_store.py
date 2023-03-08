import logging
from Models.ship import Ship
from Stores.istore import IStore

class ShipStore(IStore):
    def __init__(self):
        self.__ships = []
        pass
        
    def update(self, ships: list[Ship]):
        self.__clear()
        self.__ships = ships
              
    def __clear(self):
        self.__ships = []
    
    def get_stored_item(self) -> list[Ship]:
        return self.__ships
           