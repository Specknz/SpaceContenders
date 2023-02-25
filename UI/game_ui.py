import os
import pygame
from Models.ship import Ship
from Settings.colors import Colors
from UI.main_window import MainWindow
from Models.spawn_side import SpawnSide


class GameUI:
    CENTER_LINE_WIDTH = 10
    CENTER_LINE_COLOR = Colors.BLACK
    CENTER_LINE = pygame.Rect((MainWindow.WIDTH/2 - CENTER_LINE_WIDTH/2),
                              0,
                              CENTER_LINE_WIDTH,
                              MainWindow.HEIGHT)
    
    def __init__(self, pyg: pygame, ships: list[Ship]) -> None:
        self.__pyg = pyg
        self.__ships = ships
        self.__background = self.__load_background()
        self.__health_font = pyg.font.SysFont('Arial', 20)
        self.__winner_font = pyg.font.SysFont('Arial', 20)
        
    
    def draw(self) -> None:
        self.__draw_background()
        self.__draw_center_line()
        self.__draw_bullets()
        self.__draw_ships()
        self.__draw_ship_health()

        self.__pyg.display.update()
        
    
    def draw_winner_text(self, winner_text: str) -> None:
        draw_text = self.__winner_font.render(winner_text, 1, Colors.WHITE)
        MainWindow.SURFACE.blit(draw_text, 
                          (MainWindow.WIDTH/2 - draw_text.get_width() / 2, 
                           MainWindow.HEIGHT/2 - draw_text.get_height() / 2)
                          )
        self.__pyg.display.update()
        
      
    def __load_background(self):
            return self.__pyg.transform.scale(self.__pyg.image.load(os.path.join('Assets', 'space.png')), 
                                              (MainWindow.WIDTH, MainWindow.HEIGHT))
        
    
    def __draw_background(self) -> None:
        MainWindow.SURFACE.blit(self.__background, (0, 0))
    
    
    def __draw_center_line(self) -> None:
        self.__pyg.draw.rect(
            surface = MainWindow.SURFACE, 
            color = self.CENTER_LINE_COLOR, 
            rect = self.CENTER_LINE)
    
    
    def __draw_bullets(self) -> None:
            for ship in self.__ships:
                for bullet in ship.shot_bullets:
                    self.__pyg.draw.rect(
                        surface = MainWindow.SURFACE, 
                        color = ship.color_value, 
                        rect = bullet)


    def __draw_ships(self) -> None:
        for ship in self.__ships:
            MainWindow.SURFACE.blit(ship.sprite, (ship.rect.x, ship.rect.y))
            
            
    def __draw_ship_health(self) -> None:
        for ship in self.__ships:
            health_text = self.__health_font.render(f"{ship.color_text} Health: {ship.health}", 
                                                    1, 
                                                    ship.color_value)
            if ship.spawn_side == SpawnSide.Left:
                MainWindow.SURFACE.blit(health_text, (10, 10))
                
            if ship.spawn_side == SpawnSide.Right:
                MainWindow.SURFACE.blit(health_text, (MainWindow.WIDTH - health_text.get_width() - 10, 10))
                
                
