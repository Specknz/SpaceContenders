import os
import pygame
from Models.ship import Ship
from Config.colors import Colors
from Views.iview import IView
from Windows.main_window import MainWindow
from Models.spawn_side import SpawnSide


class GameView(IView):
    CENTER_LINE_WIDTH = 10
    CENTER_LINE_COLOR = Colors.BLACK
    CENTER_LINE = pygame.Rect((MainWindow.WIDTH/2 - CENTER_LINE_WIDTH/2),
                              0,
                              CENTER_LINE_WIDTH,
                              MainWindow.HEIGHT)
    
    FONT_SIZE = 15

    def __init__(self, pyg: pygame, ships: list[Ship], font_path: str) -> None:
        self.pyg = pyg
        self.ships = ships
        self.background = self.__load_background()
        self.font = self.pyg.font.Font(font_path, self.FONT_SIZE)

    def draw(self) -> None:
        self.__background()
        self.__center_line()
        self.__bullets()
        self.__ships()
        self.__ship_health_text()

        self.pyg.display.update()

    def __load_background(self):
        return self.pyg.transform.scale(self.pyg.image.load(os.path.join('Assets', 'space.png')),
                                        (MainWindow.WIDTH, MainWindow.HEIGHT))

    def __background(self) -> None:
        MainWindow.SURFACE.blit(self.background, (0, 0))

    def __center_line(self) -> None:
        self.pyg.draw.rect(
            surface=MainWindow.SURFACE,
            color=self.CENTER_LINE_COLOR,
            rect=self.CENTER_LINE)

    def __bullets(self) -> None:
        for ship in self.ships:
            for bullet in ship.shot_bullets:
                self.pyg.draw.rect(
                    surface=MainWindow.SURFACE,
                    color=ship.color_value,
                    rect=bullet)

    def __ships(self) -> None:
        for ship in self.ships:
            MainWindow.SURFACE.blit(ship.sprite, (ship.rect.x, ship.rect.y))

    def __ship_health_text(self) -> None:
        for ship in self.ships:
            health_text = self.font.render(f"Health: {ship.health}",
                                           True,
                                           ship.color_value)
            if ship.spawn_side == SpawnSide.Left:
                MainWindow.SURFACE.blit(health_text, (10, 10))

            if ship.spawn_side == SpawnSide.Right:
                MainWindow.SURFACE.blit(
                    health_text, (MainWindow.WIDTH - health_text.get_width() - 10, 10))
