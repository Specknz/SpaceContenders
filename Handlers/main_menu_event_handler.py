import pygame
from dataclasses import dataclass
from UI.main_menu_ui import MainMenuUI
import Helpers.events_helper as EventsHelper

@dataclass
class MainMenuEventHandler:
    pyg: pygame
    main_menu_ui: MainMenuUI
    
    def handle_events(self):
        for event in self.pyg.event.get():
            if EventsHelper.quit_pressed(self.pyg, event.type):
                self.pyg.quit()
            if EventsHelper.key_pressed(self.pyg, event.type):
                if EventsHelper.go_back(self.pyg, event.key):
                    return False
                
        return True
                    
                