from Factories.ship_factory import ShipFactory

class ShipsStore:
    def __init__(self):
        self.ship_factory = ShipFactory()
        self.ships = self.ship_factory.create_1v1_ships()