import os
import pygame

from Models.ship import Ship
from Models.ibutton import IButton
from Views.iview import IView
from Windows.main_window import MainWindow
from Factories.button_factory import ButtonFactory


class GameFinishView(IView):
    WINNING_FONT_SIZE = 35

    def __init__(self, pyg: pygame, winning_ship: Ship, font_path: str) -> None:
        self.pyg = pyg
        self.winning_ship = winning_ship
        self.background = self.__load_background()

        self.font = pygame.font.Font(font_path, self.WINNING_FONT_SIZE)
        self.continue_button: IButton = ButtonFactory \
            .create_button(self.__get_continue_button_pos(),
                           "Continue",
                           MainWindow.SURFACE)
            
    def draw(self) -> None:
        self.__background()
        self.__winner_text()
        self.__buttons()
        self.__ship()
        
        self.pyg.display.update()        

    def __load_background(self):
        return self.pyg.transform.scale(self.pyg.image.load(os.path.join('Assets', 'space.png')),
                                        (MainWindow.WIDTH, MainWindow.HEIGHT))

    def __background(self) -> None:
        MainWindow.SURFACE.blit(self.background, (0, 0))

    def __get_continue_button_pos(self):
        return (MainWindow.WIDTH / 2,
                MainWindow.HEIGHT / 2 + (IButton.HEIGHT * 2))
              
    def __winner_text(self) -> None:
        draw_text = self.font.render(f"{self.winning_ship.color_text} Ship Wins!", 
                                     True, 
                                     self.winning_ship.color_value)
        MainWindow.SURFACE.blit(draw_text, 
                                (MainWindow.WIDTH/2 - draw_text.get_width() / 2, 
                                 MainWindow.HEIGHT/2 - draw_text.get_height() / 2))

    def __buttons(self):
        self.continue_button.draw()
        
    def __ship(self):
        MainWindow.SURFACE.blit(self.winning_ship.sprite, 
                                (MainWindow.WIDTH/2 - self.winning_ship.HEIGHT/2, 
                                 MainWindow.HEIGHT/2 - self.winning_ship.WIDTH/2 - 100))