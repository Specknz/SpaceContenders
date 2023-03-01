from typing import Callable
import pygame

from dataclasses import dataclass
from States.istate import IState
from Views.main_menu_view import MainMenuView
from Handlers.ievent_handler import IEventHandler
from Handlers.event_handler_base import EventHandlerBase

@dataclass
class MainMenuEventHandler(IEventHandler, EventHandlerBase):
    pyg: pygame
    view: MainMenuView
    game_state_factory: Callable[[], IState]
    update_state_store: Callable[[IState], None]
    running = True
    
    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        
        for event in self.pyg.event.get():
            
            self.handle_quit(self.pyg, event.type)
            if self.escape_pressed(self.pyg, event):
                self.running = False
                exit()
                
            if self.mouse_click(self.pyg, event.type):
                if event.button == 1 and self.view.game_button.rect.collidepoint(mouse_pos):
                    self.running = False
                    self.update_state_store(self.game_state_factory())
                    return
                    
                if event.button == 1 and self.view.quit_button.rect.collidepoint(mouse_pos):
                    self.running = False
                    exit()
                    
        return True
       