import pygame
from Views.iview import IView
from Models.button import Button
from Windows.main_window import MainWindow


class MainMenuView(IView):
    

    def __init__(self, pyg: pygame) -> None:
        self.pyg = pyg
        
        self.game_button = Button(MainWindow.WIDTH / 2, MainWindow.HEIGHT / 2 - Button.HEIGHT, 
                                  "Start",
                                  MainWindow.SURFACE)
        
        self.quit_button = Button(MainWindow.WIDTH / 2, MainWindow.HEIGHT / 2 + Button.HEIGHT, 
                                  "Quit",
                                  MainWindow.SURFACE)
    
    
    def draw(self):
        self.__draw_buttons()
        
        self.pyg.display.update()
        

    def __draw_buttons(self):
        self.game_button.draw_button()
        self.quit_button.draw_button()