import pygame
import Factories.store_factory as StoreFactory
import Factories.settings_factory as SettingsFactory

from dataclasses import dataclass
from Factories.event_handler_factory import EventHandlerFactory
from Factories.ifactory import IFactory
from Factories.iship_factory import IShipFactory
from Factories.ship_factory import ShipFactory
from Factories.state_factory import StateFactory
from Factories.view_factory import ViewFactory
from Stores.istore import IStore


@dataclass
class AppFactory:
    pyg: pygame
    clock: pygame.time.Clock
    
    def state(self, pyg, state_store: IStore) -> IFactory:
        return StateFactory(pyg, 
                            self.clock, 
                            SettingsFactory.settings(), 
                            StoreFactory.ship(), 
                            StoreFactory.winning_ship(),
                            self.ship_factory(),
                            self.view_factory(),
                            self.event_handler_factory(state_store))
        
    def ship_factory(self) -> IShipFactory:
        return ShipFactory(SettingsFactory.settings())
    
    def view_factory(self) -> IFactory:
        return ViewFactory(self.pyg, SettingsFactory.settings())
    
    def event_handler_factory(self, state_store: IStore) -> IFactory:
        return EventHandlerFactory(self.pyg, state_store)