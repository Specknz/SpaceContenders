import pygame

from dataclasses import dataclass
from States.state import State
from States.istate import IState
from Stores.istore import IStore
from Factories.ifactory import IFactory
from Factories.iship_factory import IShipFactory
from Settings.settings import Settings

@dataclass
class StateFactory(IFactory):
    pyg: pygame
    clock: pygame.time.Clock
    settings: Settings
    ship_store: IStore
    winning_ship_store: IStore
    ship_factory: IShipFactory
    view_factory: IFactory
    event_handler_factory: IFactory
    
    # def __init__(self,
    #              pyg: pygame,
    #              clock: pygame.time.Clock,
    #              settings: SettingsManager,
    #              state_store: IStore) -> None:
    #     self.pyg: pygame = pyg
    #     self.clock: pygame.time.Clock = clock
    #     self.settings: SettingsManager = settings
    #     self.state_store: IStore = state_store

        # self.ship_store: IStore = ShipStore()
        # self.winning_ship_store: IStore = WinningShipStore()
        # self.ship_factory = ShipFactory(self.settings)
        # self.view_factory = ViewFactory(self.pyg, self.settings)
        # self.event_handler_factory = EventHandlerFactory(self.pyg, state_store.update)

    def main_menu(self) -> IState:
        view = self.view_factory.main_menu()
        event_handler = self.event_handler_factory.main_menu(view, self.game)
        return self.__create_state(view, event_handler)

    def game(self) -> IState:
        self.ship_store.update(self.ship_factory.create_1v1_ships())
        view = self.view_factory.game(self.ship_store.get_stored_item())
        event_handler = self.event_handler_factory.game(self.ship_store.get_stored_item(), 
                                                        self.game_finish,
                                                        self.winning_ship_store.update)
        return self.__create_state(view, event_handler)

    def game_finish(self) -> IState:
        view = self.view_factory.game_finish(self.winning_ship_store.get_stored_item())
        event_handler = self.event_handler_factory.game_finish(view, self.main_menu)
        return self.__create_state(view, event_handler)

    def __create_state(self, view, event_handler) -> IState:
        return State(self.pyg,
                     self.clock,
                     self.settings,
                     view,
                     event_handler)
