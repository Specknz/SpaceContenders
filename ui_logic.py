import pygame
from ui_parameters import UIParameters
from ship import Ship


def draw_window(ships: list[Ship], pyg: pygame) -> None:

        def __draw_bullets():
            for ship in ships:
                for bullet in ship.shot_bullets:
                    pyg.draw.rect(surface=UIParameters.WIN, color=ship.color_value, rect=bullet)

        def __draw_ships():
            for ship in ships:
                UIParameters.WIN.blit(ship.ship_sprite, (ship.ship_rect.x, ship.ship_rect.y))

        # BACKGROUND
        UIParameters.WIN.fill(color=UIParameters.WIN_BACKGROUND_COLOR)

        # CENTER LINE
        pyg.draw.rect(surface=UIParameters.WIN, color=UIParameters.Colors.BLACK, rect=UIParameters.CENTER_LINE, border_radius=100)

        # BULLETS
        __draw_bullets()

        # SHIPS
        __draw_ships()

        # SCOREBOARD

        # Update / Refresh / Redraw Display
        pygame.display.update()