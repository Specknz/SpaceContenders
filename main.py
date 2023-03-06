import pygame
import logging

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
    
    state_store = StateStore()
    state_factory = StateFactory(pyg, 
                                 clock, 
                                 settings,
                                 state_store)
    state_store.update(state_factory.main_menu())
      
    while True:
        state_store.run_current_state()
    
    
def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s:%(asctime)s: %(message)s', 
                        datefmt="%Y-%m-%d %H:%M:%S")
    
    
if __name__ == "__main__":
    main()
