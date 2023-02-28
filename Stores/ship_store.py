import logging
from typing import Callable
from Models.ship import Ship

class ShipStore:
    def __init__(self):
        self.ships = []
        pass
        
    def store(self, ship_factory: Callable[[], list[Ship]]):
        self.clear()
        self.ships = ship_factory()
        
        
    def clear(self):
        self.ships = []
           