from dataclasses import dataclass, field
import logging
import pygame
from Factories.bullet_factory import BulletFactory
from Models.bullet import Bullet
from Models.spawn_side import SpawnSide
import Services.ship_movement_service as ShipMovementService


@dataclass
class Ship:
    
    WIDTH = 50
    HEIGHT = 40
    SIZE = (WIDTH, HEIGHT)
    MOVE_SPEED = 4
    MAX_BULLETS = 6
    
    spawn_side: SpawnSide
    color_text: str
    color_value: set
    control_scheme: dict
    health: int
    sprite: pygame.Surface
    rect: pygame.Rect
    shot_bullets: list[Bullet] = field(default_factory = list)
        

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
            ShipMovementService.move_x(self, -(self.MOVE_SPEED) )
            
        if keys_pressed[self.control_scheme["RIGHT"]]:
            ShipMovementService.move_x(self, self.MOVE_SPEED)
            
        if keys_pressed[self.control_scheme["UP"]]:
            ShipMovementService.move_y(self, -(self.MOVE_SPEED) )

        if keys_pressed[self.control_scheme["DOWN"]]:
            ShipMovementService.move_y(self, self.MOVE_SPEED)
            
    
    def damage(self):
        self.health -= 1
        logging.debug(f"{self.color_text} ship was damaged - New health value: {self.health}")
        
        
    # def __move_x(self, amount_to_move):
    #     next_position: pygame.Rect = self.__get_next_position('x', amount_to_move)
        
    #     if (next_position.x > 0) and (next_position.x + self.HEIGHT < UI.WIN_WIDTH) and not (next_position.colliderect(UI.CENTER_LINE)):
    #         self.rect.x += amount_to_move
    #         logging.debug(f"{self.color_text} ship moved {'Right' if amount_to_move > 0 else 'Left'}")
    #         return
            
    #     if next_position.colliderect(UI.CENTER_LINE):
    #         logging.debug(f"{self.color_text} ship colliding with center line")
    #         return
        
    #     logging.debug(f"{self.color_text} ship colliding with outer wall")
            
            
    # def __move_y(self, amount_to_move):
    #     next_position: pygame.Rect = self.__get_next_position('y', amount_to_move)
        
    #     if (next_position.y > 0) and (next_position.y + self.WIDTH < UI.WIN_HEIGHT):
    #         self.rect.y += amount_to_move
    #         logging.debug(f"{self.color_text} ship moved {'Down' if amount_to_move > 0 else 'Up'}")
    #         return
        
    #     logging.debug(f"{self.color_text} ship colliding with outer wall")
            
            
    def __get_bullet_x_spawn_adjustment(self):
        if self.spawn_side == SpawnSide.Left:
            return self.HEIGHT
        
        return 0
    
    
    # def __get_next_position(self, axis, amount_to_move) -> pygame.Rect:
    #     if axis == 'x':
    #         return pygame.Rect(self.rect.x + amount_to_move, 
    #                            self.rect.y, 
    #                            self.HEIGHT, 
    #                            self.WIDTH)
    #     elif axis == 'y':
    #         return pygame.Rect(self.rect.x, 
    #                            self.rect.y + amount_to_move, 
    #                            self.HEIGHT, 
    #                            self.WIDTH)
