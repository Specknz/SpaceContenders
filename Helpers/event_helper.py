import pygame


def handle_quit(pyg: pygame, event_type):
    if quit_pressed(pyg, event_type):
        pyg.quit()
        
        
def handle_return(pyg: pygame, event, runner: bool):
    if key_pressed(pyg, event.type):
        if escape_pressed(pyg, event.key):
            runner = False


def key_pressed(pyg: pygame, event_type) -> bool:
    return event_type == pyg.KEYDOWN 


def escape_pressed(pyg: pygame, event_key):
    return event_key == pyg.K_ESCAPE


def mouse_click(pyg: pygame, event_type):
        return event_type == pyg.MOUSEBUTTONDOWN
    
    
def quit_pressed(pyg: pygame, event_type):
    return event_type == pyg.QUIT