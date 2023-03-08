from Stores.istore import IStore
from Stores.ship_store import ShipStore
from Stores.state_store import StateStore
from Stores.winning_ship_store import WinningShipStore


def ship_store() -> IStore:
    return ShipStore()

def state_store() -> IStore:
    return StateStore()

def winning_ship_store() -> IStore:
    return WinningShipStore()