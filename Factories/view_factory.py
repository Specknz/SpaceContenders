import pygame

from dataclasses import dataclass
from Models.ship import Ship
from Views.iview import IView
from Views.game_view import GameView
from Views.main_menu_view import MainMenuView
from Views.game_finish_view import GameFinishView
from Config.isettings import ISettings
from Factories.ifactory import IFactory


@dataclass
class ViewFactory(IFactory):
    pyg: pygame
    settings: ISettings

    def main_menu(self) -> IView:
        return MainMenuView(self.pyg, self.settings.font_path)

    def game(self, ships: list[Ship]) -> IView:
        return GameView(self.pyg, ships, self.settings.font_path)

    def game_finish(self, winning_ship: Ship) -> IView:
        return GameFinishView(self.pyg, winning_ship, self.settings.font_path)