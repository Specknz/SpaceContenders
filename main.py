import pygame
import logging
from Factories.ship_factory import ShipFactory
from Models.ui import UI
from game_event_handler import EventHandler
from Stores.ships_store import ShipsStore
from Settings.settings_manager import SettingsManager
from Stores.game_state_store import GameStateStore


def main():
    setup_logger()
    
    pyg = pygame
    pyg.init()
    pyg.font.init()
    pyg.mixer.init()
    pyg.display.set_caption("Space Contenders")
    clock = pyg.time.Clock()
    
    settings_manager = SettingsManager()
    game_state_store = GameStateStore()
    
    ships_factory = ShipFactory(settings_manager)
    ships_store = ShipsStore()
    ships_store.store_ships(ships_factory.create_1v1_ships)
    
    ui = UI(pyg, game_state_store, ships_store.ships)
    event_handler = EventHandler(pyg, ui, game_state_store, ships_store.ships)

    game_loop(settings_manager, ui, event_handler, clock)


def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s:%(asctime)s: %(message)s', 
                        datefmt="%Y-%m-%d %H:%M:%S")
   
    
def main_menu():
    while True:
        pass


def game_setup_menu():
    pass


def game_loop(settings_manager: SettingsManager, ui: UI, event_handler: EventHandler, clock: pygame.time.Clock):
    
    game_running = True
    while game_running:
        ui.draw_window() 
        clock.tick(settings_manager.fps)
        game_running = event_handler.handle_events()
        
        
def options_menu():
    pass
    
    
if __name__ == "__main__":
    main()
