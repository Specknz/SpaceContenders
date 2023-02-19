import pygame
import ship_logic
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
    event_handler = EventHandler(pyg, ships_store.ships)
    ui = UI(pyg, ships_store.ships)
    
    game_running = True

    while game_running:
        
        ui.draw_window()
        
        clock.tick(settings.fps)
        
        event_handler.handle_events()

        bullet_logic.move_bullets(ships_store)
        
        ship_logic.move_ships(ships_store, keys_pressed = pyg.key.get_pressed())



if __name__ == "__main__":
    main()
