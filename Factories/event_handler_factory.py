import pygame
from Handlers.game_event_handler import GameEventHandler
from Handlers.main_menu_event_handler import MainMenuEventHandler


def create_main_menu_event_handler(pyg: pygame):
    return MainMenuEventHandler(pyg)


def create_game_event_handler(pyg: pygame):
    return GameEventHandler(pyg)