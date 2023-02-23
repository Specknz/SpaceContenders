import pygame
import logging
from Factories.ship_factory import ShipFactory
from Models.ui import UI
from event_handler import EventHandler
from Stores.ships_store import ShipsStore
from Settings.settings_manager import SettingsManager


def main():
    pyg = pygame
    pyg.font.init()
    pyg.mixer.init()
    pyg.display.set_caption("Space Contenders")
    clock = pyg.time.Clock()
    
    ships_store = ShipsStore()
    ships_factory = ShipFactory()
    ships_store.create_ships(ships_factory.create_1v1_ships)
    
    setup_logger()
    
    settings = SettingsManager()
    
    ui = UI(pyg, ships_store.ships)
    
    event_handler = EventHandler(pyg, ui, ships_store.ships)
       
    game_running = True

    while game_running:
        
        ui.draw_window()
        
        clock.tick(settings.fps)

        game_running = event_handler.handle_events()


def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s:%(asctime)s: %(message)s', 
                        datefmt="%Y-%m-%d %H:%M:%S")
    
    
if __name__ == "__main__":
    main()
