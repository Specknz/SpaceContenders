import os
import pygame

from Views.iview import IView
from Models.ibutton import IButton
from Windows.main_window import MainWindow
from Factories.button_factory import ButtonFactory
from Config.colors import Colors


class MainMenuView(IView):
    
    TITLE_FONT_SIZE = 38

    def __init__(self, pyg: pygame, font_path: str) -> None:
        self.pyg = pyg
        self.font = pygame.font.Font(font_path, self.TITLE_FONT_SIZE)
        self.title_text = self.font.render(f"Space Contenders", 
                                     True, 
                                     Colors.WHITE)
        self.background = self.__load_background()
        
        self.game_button: IButton = ButtonFactory \
            .create_button(self.__get_game_button_pos(),
                           "Start",
                           MainWindow.SURFACE)
            
        self.quit_button: IButton = ButtonFactory \
            .create_button(self.__get_quit_button_pos(),
                           "Quit",
                           MainWindow.SURFACE)

    def draw(self):
        self.__background()
        self.__title()
        self.__buttons()

        self.pyg.display.update()

    def __title(self):
       MainWindow.SURFACE.blit(self.title_text , 
                                (MainWindow.WIDTH/2 - self.title_text.get_width() / 2, 
                                 MainWindow.HEIGHT/2 - self.title_text.get_height() / 2 - (MainWindow.HEIGHT/4)))

    def __buttons(self):
        self.game_button.draw()
        self.quit_button.draw()
        
    def __load_background(self):
        return self.pyg.transform.scale(self.pyg.image.load(os.path.join('Assets', 'space.png')),
                                        (MainWindow.WIDTH, MainWindow.HEIGHT))

    def __background(self) -> None:
        MainWindow.SURFACE.blit(self.background, (0, 0))

    def __get_game_button_pos(self) -> tuple:
        return (MainWindow.WIDTH / 2,
                MainWindow.HEIGHT / 2 )

    def __get_quit_button_pos(self) -> tuple:
        return (MainWindow.WIDTH / 2,
                MainWindow.HEIGHT / 2 + IButton.HEIGHT + 20)
