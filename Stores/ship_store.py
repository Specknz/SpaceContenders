import logging
from Models.ship import Ship
from Stores.istore import IStore

class ShipStore(IStore):
    def __init__(self):
        self.ships = []
        pass
        
    def update(self, ships: list[Ship]):
        self.clear()
        self.ships = ships
              
    def clear(self):
        self.ships = []
    
    def get_stored_item(self) -> list[Ship]:
        return self.ships
           