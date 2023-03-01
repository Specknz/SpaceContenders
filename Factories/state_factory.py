import pygame
import Factories.view_factory as ViewFactory
import Factories.event_handler_factory as EventHandlerFactory

from dataclasses import dataclass
from States.game_state import GameState
from Stores.istore import IStore
from States.istate import IState
from States.main_menu_state import MainMenuState
from Settings.settings_manager import SettingsManager
from Stores.ship_store import ShipStore


@dataclass
class StateFactory:
    pyg: pygame
    clock: pygame.time.Clock
    settings: SettingsManager
    ship_store: ShipStore
    state_store: IStore
    

    def create_main_menu_state(self) -> IState:
        view = ViewFactory.create_main_menu_view(self.pyg)
        
        event_handler = EventHandlerFactory.create_main_menu_event_handler(self.pyg, 
                                                                           view, 
                                                                           self.create_game_state,
                                                                           self.state_store.update)
        
        return MainMenuState(self.pyg,
                             self.clock,
                             self.settings,
                             view,
                             event_handler)
        
        
    def create_game_state(self) -> IState:
        return GameState(self.pyg,
                         self.clock,
                         self.settings,
                         ViewFactory.create_game_view(self.pyg, self.ship_store.ships),
                         EventHandlerFactory.create_game_event_handler(self.pyg, self.ship_store.ships))
