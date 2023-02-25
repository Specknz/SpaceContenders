import pygame
from dataclasses import dataclass
from UI.main_menu_ui import MainMenuUI
import Helpers.event_helper as EventsHelper

@dataclass
class MainMenuEventHandler:
    pyg: pygame
    ui: MainMenuUI
    game_clicked = False 
    in_menu = True
    
    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        
        for event in self.pyg.event.get():
            if EventsHelper.quit_pressed(self.pyg, event.type):
                self.pyg.quit()
            if EventsHelper.key_pressed(self.pyg, event.type):
                if EventsHelper.escape_pressed(self.pyg, event.key):
                    return False
            if EventsHelper.mouse_click(self.pyg, event.type):
                if event.button == 1 and self.ui.game_button.collidepoint(mouse_pos):
                    self.game_clicked = True
                if event.button == 1 and self.ui.quit_button.collidepoint(mouse_pos):
                    self.in_menu = False
        return True

                