import pygame
from Factories.ship_factory import ShipFactory
import bullet_logic
from Models.ui import UI
from event_handler import EventHandler
from Stores.ships_store import ShipsStore
from Settings.settings_manager import SettingsManager


def main():
    pyg = pygame
    pyg.display.set_caption("Space Contenders")
    clock = pyg.time.Clock()
    
    settings = SettingsManager()
    
    ships_store = ShipsStore()
    ships_factory = ShipFactory()
    
    ships_store.create_ships(ships_factory.create_1v1_ships)
    
    event_handler = EventHandler(pyg, ships_store.ships)
    ui = UI(pyg, ships_store.ships)
    
    game_running = True

    while game_running:
        
        ui.draw_window()
        
        clock.tick(settings.fps)

        event_handler.handle_events()
        
        # bullet_logic.move_bullets(ships_store)


if __name__ == "__main__":
    main()
