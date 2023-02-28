import pygame

from dataclasses import dataclass
from Views.iview import IView
from States.istate import IState
from Windows.main_window import MainWindow
from Handlers.ievent_handler import IEventHandler
from Settings.settings_manager import SettingsManager


@dataclass
class MainMenuState(IState):
    pyg: pygame
    clock: pygame.time.Clock
    settings: SettingsManager
    view: IView
    event_handler: IEventHandler
      
    def run(self):
        MainWindow.clear()
        
        while self.event_handler.running:
            self.event_handler.handle_events()  
            self.view.draw()
            self.clock.tick(self.settings.fps)
            
        MainWindow.clear()