import pygame
from Models.ui import UI
import ship_logic
from event_handler import EventHandler
from Settings.settings_manager import SettingsManager
from Stores.ships_store import ShipsStore


def main():
    pyg = pygame
    pyg.display.set_caption("Space Contenders")
    clock = pyg.time.Clock()
    
    settings = SettingsManager()
    ships_store = ShipsStore()
    event_handler = EventHandler(pyg, ships_store)
    ui = UI(pyg, ships_store.ships)
    
    game_running = True

    while game_running:
        
        ui.draw_window()
        
        clock.tick(settings.fps)
        
        event_handler.check_events()

        ship_logic.move_bullets(ships=ships_store.ships)
        
        ship_logic.move_ships(ships=ships_store.ships, keys_pressed=pyg.key.get_pressed())



if __name__ == "__main__":
    main()
