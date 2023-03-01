import pygame
import logging
from Factories.ship_factory import ShipFactory
from Stores.ship_store import ShipStore

from Stores.state_store import StateStore
from Factories.state_factory import StateFactory
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
    
    ship_store = ShipStore()
    state_store = StateStore()
    ship_factory = ShipFactory(settings)
    ship_store.store(ship_factory.create_1v1_ships())
    state_factory = StateFactory(pyg, clock, settings, ship_store, state_store)
    state_store.update(state_factory.create_main_menu_state())
      
    while True:
        state_store.run_current_state()
    
    
def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s:%(asctime)s: %(message)s', 
                        datefmt="%Y-%m-%d %H:%M:%S")
    
    
if __name__ == "__main__":
    main()
