import pygame
import logging
from Factories.ship_factory import ShipFactory
from Handlers.main_menu_event_handler import MainMenuEventHandler
from UI.game_ui import GameUI
from UI.main_menu_ui import MainMenuUI
from Handlers.game_event_handler import GameEventHandler
from Stores.ships_store import ShipsStore
from Settings.settings_manager import SettingsManager
from UI.main_window import MainWindow


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
    MainWindow.SURFACE.fill((0,0,0))
    ui = MainMenuUI(pyg)
    event_handler = MainMenuEventHandler(pyg, ui)
    
    while event_handler.in_menu:
        event_handler.game_clicked = False
        ui.draw()
        event_handler.handle_events()
        if event_handler.game_clicked:
            game(pyg, settings, ships_store, clock)
        clock.tick(settings.fps)


def game_setup_menu(pyg: pygame, settings: SettingsManager, clock: pygame.time.Clock):
    pass
        

def game(pyg: pygame, settings: SettingsManager, ships_store: ShipsStore, clock: pygame.time.Clock):
    MainWindow.SURFACE.fill((0,0,0))
    ui = GameUI(pyg, ships_store.ships)
    event_handler = GameEventHandler(pyg, ui, ships_store.ships)

    while event_handler.game_running:
        ui.draw() 
        event_handler.handle_events()
        clock.tick(settings.fps)
        
        
def options_menu():
    pass
    
    
def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s:%(asctime)s: %(message)s', 
                        datefmt="%Y-%m-%d %H:%M:%S")
    
    
if __name__ == "__main__":
    main()
