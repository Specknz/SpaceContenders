from Models.ship import Ship
from Stores.istore import IStore


class WinningShipStore(IStore):
    def __init__(self):
        self.__winning_ship: Ship

    def update(self, ship: Ship) -> None:
        self.__clear()
        self.__winning_ship = ship
        
    def get_stored_item(self) -> Ship:
        return self.__winning_ship
        
    def __clear(self) -> None:
        self.__winning_ship = None