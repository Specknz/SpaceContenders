import pygame
from Models.ibutton import IButton
from Settings.colors import Colors


class Button(IButton):
    BORDER_THICKNESS: int = 2
    
    FONT_SIZE: int = 18
    
    TEXT_COLOR = Colors.WHITE
    HOVER_COLOR = Colors.LIGHT_BLUE
    BACKGROUND_COLOR = Colors.BLUE
    BORDER_UPPER_COLOR = Colors.NEON_BLUE
    BORDER_LOWER_COLOR = Colors.NEON_BLUE_DARKER

    def __init__(self, x, y, text: str, main_surface: pygame.Surface):
        self.x = x - (self.WIDTH / 2)
        self.y = y - (self.HEIGHT / 2)
        self.text = text
        self.main_surface = main_surface
        
        self.font = pygame.font.Font('Assets/Fonts/induction/Induction.otf', self.FONT_SIZE)
        self.rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)

    def draw(self):
        self.__mouse_hover()
        self.__border()
        self.__text()
        
    def collides(self, mouse_pos: tuple[int, int]) -> bool:
        return self.rect.collidepoint(mouse_pos)

    def __mouse_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.main_surface, self.HOVER_COLOR, self.rect)
        else:
            pygame.draw.rect(self.main_surface, self.BACKGROUND_COLOR, self.rect)

    def __border(self):
        pygame.draw.line(surface = self.main_surface, 
                         color = self.BORDER_UPPER_COLOR,
                         start_pos = (self.x, self.y), 
                         end_pos = (self.x + self.WIDTH, self.y), 
                         width = self.BORDER_THICKNESS)
        
        pygame.draw.line(surface = self.main_surface, 
                         color = self.BORDER_UPPER_COLOR,
                         start_pos = (self.x, self.y), 
                         end_pos = (self.x, self.y + self.HEIGHT), 
                         width = self.BORDER_THICKNESS)
        
        pygame.draw.line(surface = self.main_surface, 
                         color = self.BORDER_LOWER_COLOR, 
                         start_pos = (self.x, self.y + self.HEIGHT), 
                         end_pos = (self.x + self.WIDTH, self.y + self.HEIGHT), 
                         width = self.BORDER_THICKNESS)
        
        pygame.draw.line(surface = self.main_surface, 
                         color = self.BORDER_LOWER_COLOR, 
                         start_pos = (self.x + self.WIDTH, self.y), 
                         end_pos = (self.x + self.WIDTH, self.y + self.HEIGHT), 
                         width = self.BORDER_THICKNESS)

    def __text(self):
        text_img = self.font.render(self.text, True, self.TEXT_COLOR)
        text_len = text_img.get_width()
        self.main_surface.blit(text_img, (self.x + int(self.WIDTH / 2) - int(text_len / 2),
                                          self.y + 25))