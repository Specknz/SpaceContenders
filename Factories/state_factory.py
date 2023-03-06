import pygame
import Factories.view_factory as ViewFactory

from Stores.istore import IStore
from Stores.ship_store import ShipStore
from States.istate import IState
from States.main_menu_state import State
from States.game_state import State
from Factories.ship_factory import ShipFactory
from Factories.event_handler_factory import EventHandlerFactory
from Settings.settings_manager import SettingsManager


class StateFactory:
    def __init__(self,
                 pyg: pygame,
                 clock: pygame.time.Clock,
                 settings: SettingsManager,
                 state_store: IStore) -> None:
        self.pyg: pygame = pyg
        self.clock: pygame.time.Clock = clock
        self.settings: SettingsManager = settings
        self.state_store: IStore = state_store

        self.ship_store: IStore = ShipStore()
        self.ship_factory = ShipFactory(self.settings)
        self.event_handler_factory = EventHandlerFactory(self.pyg, state_store.update)

    def main_menu(self) -> IState:
        view = ViewFactory.create_main_menu_view(self.pyg)
        event_handler = self.event_handler_factory.main_menu(view, self.game)
        return self.__create_state(view, event_handler)

    def game(self) -> IState:
        self.ship_store.update(self.ship_factory.create_1v1_ships())
        view = ViewFactory.create_game_view(self.pyg, self.ship_store.get_stored_item())
        event_handler = self.event_handler_factory.game(self.ship_store.get_stored_item(), self.game_finish)
        return self.__create_state(view, event_handler)

    def game_finish(self) -> IState:
        view = ViewFactory.create_game_finish_view(self.pyg)
        event_handler = self.event_handler_factory.game_finish(view, self.main_menu)
        return self.__create_state(view, event_handler)

    def __create_state(self, view, event_handler) -> IState:
        return State(self.pyg,
                     self.clock,
                     self.settings,
                     view,
                     event_handler)
