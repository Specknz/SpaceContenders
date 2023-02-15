import pygame
import event_handler
import ui_logic
import ship_logic
from settings_manager import SettingsManager
from ships_store import ShipsStore




def main():
    settings = SettingsManager()
    ships_store = ShipsStore()
    
    pyg = pygame
    
    pyg.display.set_caption("Space Contenders")
    clock = pyg.time.Clock()
    

    
    while event_handler.check_events(pyg=pyg, ships=ships_store.ships):
        
        clock.tick(settings.settings["FPS"])

        ship_logic.move_bullets(ships=ships_store.ships)
        
        ship_logic.move_ships(ships=ships_store.ships, keys_pressed=pyg.key.get_pressed())

        ui_logic.draw_window(ships=ships_store.ships, pyg=pyg)
    
    


if __name__ == "__main__":
    main()