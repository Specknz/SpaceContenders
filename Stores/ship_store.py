import logging
from Models.ship import Ship

class ShipStore:
    def __init__(self):
        self.ships = []
        pass
        
    def store(self, ships: list[Ship]):
        self.clear()
        self.ships = ships
        
        
    def clear(self):
        self.ships = []
           