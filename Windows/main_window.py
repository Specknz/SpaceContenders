import pygame


class MainWindow:
    WIDTH = 900
    HEIGHT = 500
    SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
    
    def clear():
        MainWindow.SURFACE.fill((0,0,0))
