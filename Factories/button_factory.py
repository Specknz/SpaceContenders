import pygame
from Models.button import Button
from Models.ibutton import IButton


class ButtonFactory:
    
    def create_button(x, y, text: str, surface: pygame.Surface) -> IButton:
        return Button(x, y, text, surface)
    
    
    def create_button(x_y: tuple, text: str, surface: pygame.Surface) -> IButton:
        x, y = x_y
        return Button(x, y, text, surface)