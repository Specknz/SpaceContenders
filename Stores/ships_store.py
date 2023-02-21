from typing import Callable

class ShipsStore:
    def __init__(self):
        pass
        
    def create_ships(self, ship_factory: Callable[[], list] ):
        self.ships = ship_factory()
        
        
    def clear_ships(self):
        self.ships = []
        
        
        