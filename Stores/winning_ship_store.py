from Models.ship import Ship
from Stores.istore import IStore


class WinningShipStore(IStore):
    def __init__(self):
        self. winning_ship: Ship
        pass

    def update(self, ship: Ship) -> None:
        self.__clear()
        self.winning_ship = ship
        
    def get_stored_item(self) -> Ship:
        return self.winning_ship
        
    def __clear(self) -> None:
        self.winning_ship = None