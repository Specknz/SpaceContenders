import pygame
from Handlers.game_event_handler import GameEventHandler
from Handlers.main_menu_event_handler import MainMenuEventHandler
from Views.main_menu_view import MainMenuView



def create_main_menu_event_handler(pyg: pygame, 
                                   view: MainMenuView):
    return MainMenuEventHandler(pyg, view)


def create_game_event_handler(pyg: pygame):
    return GameEventHandler(pyg)