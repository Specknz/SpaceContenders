import pygame
from Models.ship import Ship
from Views.game_view import GameView
from Views.main_menu_view import MainMenuView
from Views.game_finish_view import GameFinishView


def create_main_menu_view(pyg: pygame):
    return MainMenuView(pyg)


def create_game_view(pyg: pygame, ships: list[Ship]):
    return GameView(pyg, ships)


def create_game_finish_view(pyg: pygame):
    return GameFinishView(pyg)