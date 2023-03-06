import pygame
import logging

from abc import ABC

class EventHandlerBase(ABC):
    
    def handle_quit(self, pyg: pygame, event_type):
        if self.quit_pressed(pyg, event_type):
            pyg.quit()
            
            
    def check_for_escape_pressed(self, pyg: pygame, event):
        if self.key_pressed(pyg, event.type):
            if self.escape_pressed(pyg, event.key):
                return True


    def key_pressed(self, pyg: pygame, event_type) -> bool:
        return event_type == pyg.KEYDOWN 


    def escape_pressed(self, pyg: pygame, event_key):
        return event_key == pyg.K_ESCAPE


    def mouse_click(self, pyg: pygame, event_type):
            return event_type == pyg.MOUSEBUTTONDOWN
        
        
    def quit_pressed(self, pyg: pygame, event_type):
        return event_type == pyg.QUIT