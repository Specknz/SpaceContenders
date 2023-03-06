import pygame
from Models.ibutton import IButton
from Settings.colors import Colors


class Button(IButton):

    def __init__(self, x, y, text: str, main_surface: pygame.Surface):
        self.x = x - (self.WIDTH / 2)
        self.y = y - (self.HEIGHT / 2)
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
        self.font = pygame.font.Font(
            'Assets/Fonts/induction/Induction.otf', 15)
        self.main_surface = main_surface

    def draw(self):
        self.__handle_mouse_hover()
        self.__draw_shading()
        self.__add_text()
        
    def collides(self, mouse_pos: tuple[int, int]) -> bool:
        return self.rect.collidepoint(mouse_pos)

    def __handle_mouse_hover(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            pygame.draw.rect(self.main_surface, Colors.LIGHT_BLUE, self.rect)
        else:
            pygame.draw.rect(self.main_surface, Colors.BLUE, self.rect)

    def __draw_shading(self):
        pygame.draw.line(self.main_surface, Colors.WHITE,
                         (self.x, self.y), (self.x + self.WIDTH, self.y), 2)
        pygame.draw.line(self.main_surface, Colors.WHITE,
                         (self.x, self.y), (self.x, self.y + self.HEIGHT), 2)
        pygame.draw.line(self.main_surface, Colors.BLACK, (self.x, self.y +
                         self.HEIGHT), (self.x + self.WIDTH, self.y + self.HEIGHT), 2)
        pygame.draw.line(self.main_surface, Colors.BLACK, (self.x + self.WIDTH,
                         self.y), (self.x + self.WIDTH, self.y + self.HEIGHT), 2)

    def __add_text(self):
        text_img = self.font.render(self.text, True, Colors.WHITE)
        text_len = text_img.get_width()
        self.main_surface.blit(text_img, (self.x + int(self.WIDTH / 2) - int(text_len / 2),
                                          self.y + 25))

