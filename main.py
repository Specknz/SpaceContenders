import pygame
import logging
from Factories.ship_factory import ShipFactory
from Services.state_service import StateService
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
    
    ship_factory = ShipFactory(settings)
    ship_store = ShipStore()
    ship_store.store(ship_factory.create_1v1_ships)
    state_store = StateStore()
    state_service = StateService(state_store)
    state_factory = StateFactory(pyg, clock, settings, state_service, ship_store)
    state_store.Update(state_factory.create_main_menu_state())
      
    while True:
        state_store.RunCurrentState()
    
    
    # main_menu(pyg, settings, ship_store, ships_factory, clock)

    
# def main_menu(pyg: pygame, settings: SettingsManager, ship_store: ShipsStore, ship_factory: ShipFactory, clock: pygame.time.Clock):
#     MainWindow.SURFACE.fill((0,0,0))
    
#     view = MainMenuView(pyg)
#     event_handler = MainMenuEventHandler(pyg, view)
    
#     while event_handler.loop_running:
#         event_handler.game_clicked = False
#         view.draw()
#         event_handler.handle_events()
        
#         if event_handler.game_clicked:
#             ship_store.store_ships(ship_factory.create_1v1_ships)
#             game(pyg, settings, ship_store, clock)
            
#         clock.tick(settings.fps)
        
#     MainWindow.SURFACE.fill((0,0,0))
    


# def game_setup_menu(pyg: pygame, settings: SettingsManager, clock: pygame.time.Clock):
#     pass
        

# def game(pyg: pygame, settings: SettingsManager, ships_store: ShipsStore, clock: pygame.time.Clock):
#     MainWindow.SURFACE.fill((0,0,0))
#     ui = GameView(pyg, ships_store.ships)
#     event_handler = GameEventHandler(pyg, ui, ships_store.ships)

#     while event_handler.game_running:
#         ui.draw() 
#         event_handler.handle_events()
#         clock.tick(settings.fps)
        
#     MainWindow.SURFACE.fill((0,0,0))
        
        
# def options_menu():
#     pass
    
    
def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s:%(asctime)s: %(message)s', 
                        datefmt="%Y-%m-%d %H:%M:%S")
    
    
if __name__ == "__main__":
    main()
