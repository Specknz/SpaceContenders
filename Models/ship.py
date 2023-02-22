import logging
import pygame
from Factories.bullet_factory import BulletFactory
from Models.bullet import Bullet
from Models.ui import UI


class Ship:
    
    WIDTH = 50
    HEIGHT = 40
    SIZE = (WIDTH, HEIGHT)
    MOVE_SPEED = 5
    MAX_BULLETS = 6
    
    def __init__(self, 
                 spawn_side: str,
                 color_text: str, 
                 color_value: set, 
                 control_scheme: dict,
                 sprite: pygame.Surface,
                 rect: pygame.Rect) -> None:

        self.spawn_side = spawn_side.lower()

        self.color_text: str = color_text
        self.color_value: set = color_value
        
        self.control_scheme: dict = control_scheme
        
        self.sprite: pygame.Surface = sprite
        self.rect: pygame.Rect = rect
 
        self.shot_bullets: list[Bullet] = []
        
        self.health: int = 10


    def __repr__(self) -> str:
        return f"{self.color_text} Spaceship"
    
    
    def shoot(self):
        if len(self.shot_bullets) < self.MAX_BULLETS:
            bullet = BulletFactory.create_bullet(self.rect.x, 
                                                 self.rect.y,
                                                 self.__get_bullet_x_spawn_adjustment(),
                                                 self.WIDTH)
            
            self.shot_bullets.append(bullet)
            logging.debug(f"{self.color_text} ship shot")
            
            
    def move(self, keys_pressed):
        if keys_pressed[self.control_scheme["LEFT"]]:
            self.__move_left()
            
        if keys_pressed[self.control_scheme["RIGHT"]]:
            self.__move_right()
            
        if keys_pressed[self.control_scheme["UP"]]:
            self.__move_up()

        if keys_pressed[self.control_scheme["DOWN"]]:
            self.__move_down()
        
            
    def __move_left(self):
        
        if (self.rect.x - self.MOVE_SPEED) > 0:
            self.rect.x -= self.MOVE_SPEED
            logging.debug(f"{self.color_text} ship moved LEFT")
            return
            
        if self.rect.colliderect(UI.CENTER_LINE):
            logging.debug(f"{self.color_text} ship colliding with center line")
            return
        
        logging.debug(f"{self.color_text} ship colliding with outer wall")
            
            
    def __move_right(self): 
        if (self.rect.x + self.MOVE_SPEED + self.HEIGHT) < UI.WIN_WIDTH:
            self.rect.x += self.MOVE_SPEED
            logging.debug(f"{self.color_text} ship moved RIGHT")
            return

        if self.rect.colliderect(UI.CENTER_LINE):
            logging.debug(f"{self.color_text} ship colliding with center line")
            return
            
        logging.debug(f"{self.color_text} ship colliding with outer wall")
            
            
    def __move_up(self):
        if (self.rect.y - self.MOVE_SPEED) > 0:
            self.rect.y -= self.MOVE_SPEED
        
        
    def __move_down(self):
        if (self.rect.y + self.MOVE_SPEED) + self.WIDTH < UI.WIN_HEIGHT:
            self.rect.y += self.MOVE_SPEED
            
            
    def __get_bullet_x_spawn_adjustment(self):
        if self.spawn_side == "left":
            return self.HEIGHT
        
        return 0
