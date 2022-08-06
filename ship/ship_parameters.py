import pygame
from ui.ui_parameters import UIParameters

class ShipParameters:
    
    SHIP_WIDTH = 50
    SHIP_HEIGHT = 40

    SHIP_SIZE = (SHIP_WIDTH, SHIP_HEIGHT)

    SHIP_MOVEMENT_SPEED = 5

    SHIP_START_Y_LOC = (UIParameters.WIN_HEIGHT/2) - (SHIP_HEIGHT/2)

    BULLET_HEIGHT = 4
    BULLET_WIDTH = 10

    BULLET_MAX_AMOUNT = 6
    
    BULLET_SPEED = SHIP_MOVEMENT_SPEED + 2

    LEFT_CONTROLS = {
                "LEFT": pygame.K_a,
                "RIGHT": pygame.K_d,
                "UP": pygame.K_w,
                "DOWN": pygame.K_s,
                "SHOOT": pygame.K_LCTRL
            }

    RIGHT_CONTROLS = {
                "LEFT": pygame.K_LEFT,
                "RIGHT": pygame.K_RIGHT,
                "UP": pygame.K_UP,
                "DOWN": pygame.K_DOWN,
                "SHOOT": pygame.K_RCTRL
            }