import pygame
from dataclasses import dataclass
from Handlers.ievent_handler import IEventHandler
from Views.main_menu_view import MainMenuView
from Handlers.event_handler_base import EventHandlerBase

@dataclass
class MainMenuEventHandler(IEventHandler, EventHandlerBase):
    pyg: pygame
    view: MainMenuView
    game_clicked = False 
    in_menu = True
    
    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        
        for event in self.pyg.event.get():
            
            self.handle_quit(self.pyg, event.type)
            if self.escape_pressed(self.pyg, event):
                self.in_menu = False
                
            if self.mouse_click(self.pyg, event.type):
                if event.button == 1 and self.view.game_button.rect.collidepoint(mouse_pos):
                    self.game_clicked = True
                if event.button == 1 and self.view.quit_button.rect.collidepoint(mouse_pos):
                    self.in_menu = False
                    
        return True
       