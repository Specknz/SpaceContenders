import os
import pygame
from Models.spawn_side import SpawnSide
from Settings.colors import Colors
from Stores.game_state_store import GameStateStore



class UI:
    
    WIN_WIDTH = 900
    WIN_HEIGHT = 500
    WIN_BACKGROUND_COLOR = Colors.GREY

    CENTER_LINE_WIDTH = 10
    
    CENTER_LINE = pygame.Rect(WIN_WIDTH/2 - CENTER_LINE_WIDTH/2,
                              0,
                              CENTER_LINE_WIDTH,
                              WIN_HEIGHT)
    
    
    def __init__(self, pyg: pygame, game_state_store: GameStateStore, ships) -> None:
        self.__pyg = pyg
        self.__ships = ships
        self.__game_state_store = game_state_store
        self.__background = self.__pyg.transform.scale(self.__pyg.image.load(
            os.path.join('Assets', 'space.png')), (self.WIN_WIDTH, self.WIN_HEIGHT))
        
        self.__window = self.__pyg.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))
        self.__health_font = pyg.font.SysFont('Arial', 20)
        self.__winner_font = pyg.font.SysFont('Arial', 20)
        
    
    def draw_window(self) -> None:
        if self.__game_state_store.GAME_RUNNING:
            self.__draw_background()
            self.__draw_center_line()
            self.__draw_bullets()
            self.__draw_ships()
            self.__draw_ship_health()
        else:
            pass
        self.__pyg.display.update()
        
    
    def draw_winner_text(self, winner_text: str):
        draw_text = self.__winner_font.render(winner_text, 1, Colors.WHITE)
        self.__window.blit(draw_text, 
                          (self.WIN_WIDTH/2 - draw_text.get_width() / 2, 
                           self.WIN_HEIGHT/2 - draw_text.get_height() / 2)
                          )
        self.__pyg.display.update()
        
    
    def __draw_background(self):
        self.__window.blit(self.__background, (0, 0))
    
    
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
        for ship in self.__ships:
            health_text = self.__health_font.render(f"{ship.color_text} Health: {ship.health}", 
                                                    1, 
                                                    ship.color_value)
            if ship.spawn_side == SpawnSide.Left:
                self.__window.blit(health_text, (10, 10))
                
            if ship.spawn_side == SpawnSide.Right:
                self.__window.blit(health_text, (self.WIN_WIDTH - health_text.get_width() - 10, 10))
                
                
