import pygame
from game_parameters import GameParameters
from . import game_event_handler
from . import game_logic
from . import ui_logic
from .game import ship_logic


class GameEngine():

    def run_game():
        pyg = pygame
        clock = pyg.time.Clock()
        ships = game_logic.create_ships()

        while GameParameters.game_running:

            clock.tick(GameParameters.FPS)

            game_event_handler.check_events(pyg=pyg, ships=ships)

            ship_logic.move_bullets(ships=ships)
            
            ship_logic.move_ships(ships=ships, keys_pressed=pyg.key.get_pressed())

            ui_logic.draw_window(ships=ships, pyg=pyg)
        
        pyg.quit()


