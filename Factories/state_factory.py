import pygame
import Factories.view_factory as ViewFactory
import Factories.event_handler_factory as EventHandlerFactory

from dataclasses import dataclass
from States.game_state import GameState
from States.main_menu_state import MainMenuState
from Settings.settings_manager import SettingsManager


@dataclass
class StateFactory:
    pyg: pygame
    clock: pygame.time.Clock
    settings: SettingsManager
    

    def create_main_menu_state(self) -> MainMenuState:
        view = ViewFactory.create_main_menu_view(self.pyg)
        event_handler = EventHandlerFactory.create_main_menu_event_handler(self.pyg, view)
        
        return MainMenuState(self.pyg,
                             self.clock,
                             self.settings,
                             view,
                             event_handler)
        
        
    def create_game_state(self):
        return GameState(self.pyg,
                         self.clock,
                         self.settings,
                         ViewFactory.create_game_view(self.pyg),
                         EventHandlerFactory.create_game_event_handler(self.pyg))
