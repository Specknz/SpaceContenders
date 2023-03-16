import logging
import pygame

from typing import Callable
from dataclasses import dataclass
from Models.istate import IState
from Views.main_menu_view import MainMenuView
from Handlers.ievent_handler import IEventHandler
from Handlers.event_handler_base import EventHandlerBase

@dataclass
class MainMenuEventHandler(IEventHandler, EventHandlerBase):
    pyg: pygame
    view: MainMenuView
    update_state_store_func: Callable[[IState], None]
    game_state_factory_func: Callable[[], IState]
    running = True
    
    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        
        for event in self.pyg.event.get():
            self.handle_quit(self.pyg, event.type)
            if self.check_for_escape_pressed(self.pyg, event):
                self.running = False
                exit()
                
            if self.mouse_click(self.pyg, event.type):
                if event.button == 1 and self.view.game_button.collides(mouse_pos):
                    self.running = False
                    self.update_state_store_func(self.game_state_factory_func())
                    return
                    
                if event.button == 1 and self.view.quit_button.collides(mouse_pos):
                    self.running = False
                    exit()
                    
        return True
       