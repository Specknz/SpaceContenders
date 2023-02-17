import pygame

class UI:
    
    class Colors: 
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREY = (105,105,105)

        RED = (255,0,0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)

        YELLOW = (255,255,0)
           
    WIN_WIDTH = 900
    WIN_HEIGHT = 500
    WIN_BACKGROUND_COLOR = Colors.GREY

    CENTER_LINE_WIDTH = 10
    CENTER_LINE = pygame.Rect(
        (WIN_WIDTH/2)-(CENTER_LINE_WIDTH/2),
        0,
        CENTER_LINE_WIDTH,
        WIN_HEIGHT)
    
    def __init__(self, pyg: pygame, ships) -> None:
        self._pyg = pyg
        
        self._ships = ships
        
        self._window = self._pyg.display.set_mode(size=(self.WIN_WIDTH, self.WIN_HEIGHT))
    
    def draw_window(self) -> None:
        self._draw_background()
        self._draw_center_line()
        self._draw_bullets()
        self._draw_ships()
        pygame.display.update()
        
    
    def _draw_background(self):
        self._window.fill(color = self.WIN_BACKGROUND_COLOR)
    
    
    def _draw_center_line(self):
        self._pyg.draw.rect(
            surface = self._window, 
            color = self.Colors.BLACK, 
            rect = self.CENTER_LINE, 
            border_radius = 100)
    
    
    def _draw_bullets(self):
            for ship in self._ships:
                for bullet in ship.shot_bullets:
                    self._pyg.draw.rect(
                        surface = self._window, 
                        color = ship.color_value, 
                        rect = bullet)


    def _draw_ships(self):
        for ship in self._ships:
            self._window.blit(ship.ship_sprite, (ship.ship_rect.x, ship.ship_rect.y))