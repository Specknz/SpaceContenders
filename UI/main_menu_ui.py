import pygame
from dataclasses import dataclass
from UI.main_window import MainWindow

@dataclass
class MainMenuUI:
    pyg: pygame
    
    
    game_button = pygame.Rect(50, 100, 200, 50)
    quit_button = pygame.Rect(50, 200, 200, 50)
    
    
    def draw(self):
        self.__draw_buttons()
        
        self.pyg.display.update()
        
        
        
    def __draw_buttons(self):
        self.pyg.draw.rect(MainWindow.SURFACE, (255, 0, 0), self.game_button)
        self.pyg.draw.rect(MainWindow.SURFACE, (255, 0, 0), self.quit_button)