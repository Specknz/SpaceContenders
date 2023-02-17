import pygame
import event_handler
import ui_logic
import ship_logic
from Settings.settings_manager import SettingsManager
from ships_store import ShipsStore


def main():
    pyg = pygame
    pyg.display.set_caption("Space Contenders")
    
    settings = SettingsManager()
    ships_store = ShipsStore()
    
    clock = pyg.time.Clock()
    
    game_running = True

    while game_running:
        event_handler.check_events(pyg=pyg, ships=ships_store.ships)

        clock.tick(settings.fps)

        ship_logic.move_bullets(ships=ships_store.ships)
        
        ship_logic.move_ships(ships=ships_store.ships, keys_pressed=pyg.key.get_pressed())

        ui_logic.draw_window(ships=ships_store.ships, pyg=pyg)


if __name__ == "__main__":
    main()
