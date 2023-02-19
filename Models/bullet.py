import pygame


class Bullet:
    
    HEIGHT = 4
    WIDTH = 10
    SPEED = 7
    
    def __init__(self, x_spawn_loc, y_spawn_loc) -> None:
        self.rect = pygame.Rect(x_spawn_loc, y_spawn_loc, self.WIDTH, self.HEIGHT)