import pygame
from Models.ship import Ship
from Settings.settings_manager import SettingsManager
from Views.game_view import GameView
from Views.iview import IView
from Views.main_menu_view import MainMenuView
from Views.game_finish_view import GameFinishView


class ViewFactory:

    def __init__(self, pyg: pygame, settings: SettingsManager):
        self.pyg: pygame = pyg
        self.settings: SettingsManager = settings

    def main_menu(self) -> IView:
        return MainMenuView(self.pyg, self.settings.font_path)

    def game(self, ships: list[Ship]) -> IView:
        return GameView(self.pyg, ships, self.settings.font_path)

    def game_finish(self, winning_ship: Ship) -> IView:
        return GameFinishView(self.pyg, winning_ship, self.settings.font_path)