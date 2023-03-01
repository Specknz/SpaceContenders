import pygame

from typing import Callable
from Handlers.game_event_handler import GameEventHandler
from Handlers.main_menu_event_handler import MainMenuEventHandler
from Models.ship import Ship
from States.istate import IState
from Views.main_menu_view import MainMenuView



def create_main_menu_event_handler(pyg: pygame, 
                                   view: MainMenuView,
                                   game_state_factory: Callable[[], IState],
                                   update_state_func: Callable[[IState], None]):
    return MainMenuEventHandler(pyg, view, game_state_factory, update_state_func)


def create_game_event_handler(pyg: pygame, ships: list[Ship]):
    return GameEventHandler(pyg, ships)