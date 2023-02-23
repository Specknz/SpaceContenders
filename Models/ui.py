import pygame
from Settings.colors import Colors

class UI:
    
    WIN_WIDTH = 900
    WIN_HEIGHT = 500
    WIN_BACKGROUND_COLOR = Colors.GREY

    CENTER_LINE_WIDTH = 10
    
    CENTER_LINE = pygame.Rect(WIN_WIDTH/2 - CENTER_LINE_WIDTH/2,
                              0,
                              CENTER_LINE_WIDTH,
                              WIN_HEIGHT)
    
    
    def __init__(self, pyg: pygame, ships) -> None:
        self.__pyg = pyg
        self.__window = self.__pyg.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))
        self.__ships = ships
        self.__health_font = pyg.font.SysFont('Arial', 40)
        self.__winner_font = pyg.font.SysFont('Arial', 20)
        
    
    def draw_window(self) -> None:
        self.__draw_background()
        self.__draw_center_line()
        self.__draw_bullets()
        self.__draw_ships()
        self.__draw_ship_health()
        self.__pyg.display.update()
        
    
    def draw_winner_text(self, winner_text: str):
        draw_text = self.__winner_font.render(winner_text, 1, Colors.WHITE)
        self.__window.blit(draw_text, 
                          (self.WIN_WIDTH/2 - draw_text.get_width() / 2, 
                           self.WIN_HEIGHT/2 - draw_text.get_height() / 2)
                          )
        self.__pyg.display.update()
        
    
    def __draw_background(self):
        self.__window.fill(color = self.WIN_BACKGROUND_COLOR)
    
    
    def __draw_center_line(self):
        self.__pyg.draw.rect(
            surface = self.__window, 
            color = Colors.BLACK, 
            rect = self.CENTER_LINE)
    
    
    def __draw_bullets(self):
            for ship in self.__ships:
                for bullet in ship.shot_bullets:
                    self.__pyg.draw.rect(
                        surface = self.__window, 
                        color = ship.color_value, 
                        rect = bullet)


    def __draw_ships(self):
        for ship in self.__ships:
            self.__window.blit(ship.sprite, (ship.rect.x, ship.rect.y))
            
            
    def __draw_ship_health(self):
        pass
        # for ship in self._ships:
        #     red_health_text = self.HEALTH_FONT.render( "Health: " + str(red_health), 1, WHITE)
        #     yellow_health_text = self.HEALTH_FONT.render( "Health: " + str(yellow_health), 1, WHITE)
        #     self._window.blit(red_health_text, (self.WIN_WIDTH - red_health_text.get_width() - 10, 10))
        #     self._window.blit(yellow_health_text, (10, 10))
