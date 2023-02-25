import pygame


def key_pressed(pyg: pygame, event_type) -> bool:
    return event_type == pyg.KEYDOWN 


def quit_pressed(pyg: pygame, event_type):
    return event_type == pyg.QUIT


def go_back(pyg: pygame, event_key):
    return event_key == pyg.K_ESCAPE