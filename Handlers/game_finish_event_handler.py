import pygame

from typing import Callable
from dataclasses import dataclass
from States.istate import IState
from Handlers.ievent_handler import IEventHandler
from Views.game_finish_view import GameFinishView
from Handlers.event_handler_base import EventHandlerBase


@dataclass
class GameFinishEventHandler(IEventHandler, EventHandlerBase):
    pyg: pygame
    view: GameFinishView
    update_state_store_func: Callable[[IState], None]
    main_menu_state_factory_func: Callable[[], IState]
    running = True
    
    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        
        for event in self.pyg.event.get():
            
            self.handle_quit(self.pyg, event.type)
            if self.escape_pressed(self.pyg, event):
                self.running = False
                exit()
                
            if self.mouse_click(self.pyg, event.type):
                if event.button == 1 and self.view.continue_button.collides(mouse_pos):
                    self.running = False
                    self.update_state_store_func(self.main_menu_state_factory_func())
                    return
                    
        return True
