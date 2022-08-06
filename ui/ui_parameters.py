import pygame

class UIParameters:

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

    WIN = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    pygame.display.set_caption("My First PyGame")