import pygame
import logging
from Factories.ship_factory import ShipFactory
from UI.game_ui import GameUI
from Handlers.game_event_handler import GameEventHandler
from Stores.ships_store import ShipsStore
from Settings.settings_manager import SettingsManager


def main():
    setup_logger()
    
    pyg = pygame
    pyg.init()
    pyg.font.init()
    pyg.mixer.init()
    pyg.display.set_caption("Space Contenders")
    clock = pyg.time.Clock()
    
    settings = SettingsManager()
    
    ships_factory = ShipFactory(settings)
    ships_store = ShipsStore()
    ships_store.store_ships(ships_factory.create_1v1_ships)
    
    main_menu(pyg, settings, ships_store, clock)

    
def main_menu(pyg: pygame, settings: SettingsManager, ships_store: ShipsStore, clock: pygame.time.Clock):
    in_menu = True
    while in_menu:
        game(pyg, settings, ships_store, clock)
        clock.tick(settings.fps)


def game_setup_menu(pyg: pygame, settings: SettingsManager, clock: pygame.time.Clock):
    pass
        

def game(pyg: pygame, settings: SettingsManager, ships_store: ShipsStore, clock: pygame.time.Clock):
    game_ui = GameUI(pyg, ships_store.ships)
    game_event_handler = GameEventHandler(pyg, game_ui, ships_store.ships)
    
    game_running = True
    while game_running:
        game_ui.draw() 
        game_running = game_event_handler.handle_events()
        clock.tick(settings.fps)
        
        
def options_menu():
    pass
    
    
def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s:%(asctime)s: %(message)s', 
                        datefmt="%Y-%m-%d %H:%M:%S")
    
    
if __name__ == "__main__":
    main()
