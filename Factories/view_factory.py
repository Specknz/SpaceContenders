import pygame
from Models.ship import Ship
from Settings.settings import Settings
from Views.game_view import GameView
from Views.iview import IView
from Views.main_menu_view import MainMenuView
from Views.game_finish_view import GameFinishView
from Factories.ifactory import IFactory


class ViewFactory(IFactory):

    def __init__(self, pyg: pygame, settings: Settings):
        self.pyg: pygame = pyg
        self.settings: Settings = settings

    def main_menu(self) -> IView:
        return MainMenuView(self.pyg, self.settings.font_path)

    def game(self, ships: list[Ship]) -> IView:
        return GameView(self.pyg, ships, self.settings.font_path)

    def game_finish(self, winning_ship: Ship) -> IView:
        return GameFinishView(self.pyg, winning_ship, self.settings.font_path)