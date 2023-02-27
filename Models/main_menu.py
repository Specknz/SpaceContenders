import pygame
from typing import Callable
from Handlers.ievent_handler import IEventHandler
from Models.istate import IState
from Models.ship import Ship
from Settings.settings_manager import SettingsManager
from Views.iview import IView
from Windows.main_window import MainWindow


class MainMenu(IState):
    pyg: pygame
    clock: pygame.time.Clock
    view: IView
    goto_state: IState
    event_handler: IEventHandler
    ship_creator: Callable[[], list[Ship]]
    settings: SettingsManager
    
        
    def run(self):
        MainWindow.SURFACE.fill((0,0,0))
        
        while self.event_handler.loop_running:
            self.event_handler.game_clicked = False
            self.view.draw()
            self.event_handler.handle_events()
            
            if self.event_handler.game_clicked:
                self.goto_state.run()
                
            self.clock.tick(self.settings.fps)
            
        MainWindow.SURFACE.fill((0,0,0))