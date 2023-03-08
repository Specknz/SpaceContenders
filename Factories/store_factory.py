from Stores.istore import IStore
from Stores.ship_store import ShipStore
from Stores.state_store import StateStore
from Stores.winning_ship_store import WinningShipStore


def ship() -> IStore:
    return ShipStore()

def winning_ship() -> IStore:
    return WinningShipStore()

def state() -> IStore:
    return StateStore()
