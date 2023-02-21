from typing import Callable
from Models.ship import Ship

class ShipsStore:
    def __init__(self):
        pass
        
    def create_ships(self, ship_factory: Callable[[], list[Ship]]):
        self.ships = ship_factory()
        
        
    def clear_ships(self):
        self.ships = []
        
        
        