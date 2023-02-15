from ship_factory import ShipFactory

class ShipsStore:
    def __init__(self):
        self.ships = ShipFactory.create_ships()