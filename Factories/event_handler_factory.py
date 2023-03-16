import pygame

from dataclasses import dataclass
from typing import Callable
from Models.ship import Ship
from Models.istate import IState
from Stores.istore import IStore
from Views.iview import IView
from Factories.ifactory import IFactory
from Handlers.game_event_handler import GameEventHandler
from Handlers.main_menu_event_handler import MainMenuEventHandler
from Handlers.game_finish_event_handler import GameFinishEventHandler


@dataclass
class EventHandlerFactory(IFactory):
    pyg: pygame
    state_store: IStore

    def main_menu(self, 
                  view: IView, 
                  game_state_factory_func: Callable[[], IState]):
        return MainMenuEventHandler(self.pyg,
                                    view,
                                    self.state_store.update,
                                    game_state_factory_func)

    def game(self, 
             ships: list[Ship], 
             game_finish_state_factory_func: Callable[[], IState],
             update_winning_ship_func: Callable[[Ship], None]):
        return GameEventHandler(self.pyg,
                                ships,
                                self.state_store.update,
                                game_finish_state_factory_func,
                                update_winning_ship_func)

    def game_finish(self, 
                    view: IView, 
                    main_menu_state_factory_func: Callable[[], IState]):
        return GameFinishEventHandler(self.pyg,
                                      view,
                                      self.state_store.update,
                                      main_menu_state_factory_func)
