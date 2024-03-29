import pygame

from dataclasses import dataclass
from Handlers.ievent_handler import IEventHandler
from Config.isettings import ISettings
from Models.istate import IState
from Views.iview import IView
from Windows.main_window import MainWindow


@dataclass
class State(IState):
    pyg: pygame
    clock: pygame.time.Clock
    settings: ISettings
    view: IView
    event_handler: IEventHandler
    
    def run(self):
        MainWindow.clear()

        while self.event_handler.running:
            self.event_handler.handle_events()
            self.view.draw()
            self.clock.tick(self.settings.fps)
            
        MainWindow.clear()
            