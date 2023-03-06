import pygame

from typing import Callable
from Models.ship import Ship
from Views.iview import IView
from States.istate import IState
from dataclasses import dataclass, field
from Handlers.game_event_handler import GameEventHandler
from Handlers.main_menu_event_handler import MainMenuEventHandler
from Handlers.game_finish_event_handler import GameFinishEventHandler


@dataclass
class EventHandlerFactory:
    pyg: pygame
    update_state_store_func: Callable[[IState], None] = field(default_factory=Callable)

    def main_menu(self, view: IView, game_state_factory_func: Callable[[], IState]):
        return MainMenuEventHandler(self.pyg,
                                    view,
                                    self.update_state_store_func,
                                    game_state_factory_func)

    def game(self, ships: list[Ship], game_finish_state_factory_func: Callable[[], IState]):
        return GameEventHandler(self.pyg,
                                ships,
                                self.update_state_store_func,
                                game_finish_state_factory_func)

    def game_finish(self, view: IView, main_menu_state_factory_func: Callable[[], IState]):
        return GameFinishEventHandler(self.pyg,
                                      view,
                                      self.update_state_store_func,
                                      main_menu_state_factory_func)
