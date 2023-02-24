import pygame
import logging
from Factories.ship_factory import ShipFactory
from Models.ui import UI
from event_handler import EventHandler
from Stores.ships_store import ShipsStore
from Settings.settings_manager import SettingsManager
from Stores.game_state_store import GameStateStore


def main():
    setup_logger()
    
    pyg = pygame
    pyg.font.init()
    pyg.mixer.init()
    pyg.display.set_caption("Space Contenders")
    clock = pyg.time.Clock()
    
    settings = SettingsManager()
    game_state_store = GameStateStore()
    
    ships_factory = ShipFactory(settings)
    ships_store = ShipsStore()
    ships_store.store_ships(ships_factory.create_1v1_ships)
    
    ui = UI(pyg, game_state_store, ships_store.ships)
    event_handler = EventHandler(pyg, ui, game_state_store, ships_store.ships)

    while game_state_store.GAME_RUNNING:
        ui.draw_window() 
        clock.tick(settings.fps)
        event_handler.handle_events()


def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s:%(asctime)s: %(message)s', 
                        datefmt="%Y-%m-%d %H:%M:%S")
    
    
if __name__ == "__main__":
    main()
