import pygame

from Views.iview import IView
from Models.ibutton import IButton
from Windows.main_window import MainWindow
from Factories.button_factory import ButtonFactory


class MainMenuView(IView):

    def __init__(self, pyg: pygame) -> None:
        self.pyg = pyg
        
        self.game_button: IButton = ButtonFactory \
            .create_button(self.__get_game_button_pos(),
                           "Start",
                           MainWindow.SURFACE)
            
        self.quit_button: IButton = ButtonFactory \
            .create_button(self.__get_quit_button_pos(),
                           "Quit",
                           MainWindow.SURFACE)

    def draw(self):
        self.__draw_buttons()

        self.pyg.display.update()

    def __draw_buttons(self):
        self.game_button.draw()
        self.quit_button.draw()

    def __get_game_button_pos(self) -> tuple:
        return (MainWindow.WIDTH / 2,
                MainWindow.HEIGHT / 2 - IButton.HEIGHT)

    def __get_quit_button_pos(self) -> tuple:
        return (MainWindow.WIDTH / 2,
                MainWindow.HEIGHT / 2 + IButton.HEIGHT)
