import pygame

from dataclasses import dataclass
from States.istate import IState
from Stores.istore import IStore
from Factories.ifactory import IFactory
from Settings.isettings import ISettings


@dataclass
class AppService():
    pyg: pygame
    clock: pygame.time.Clock
    settings: ISettings
    state_store: IStore
    state_factory: IFactory

    def setup(self):
        self.state_store.update(self.state_factory.main_menu())

    def run(self):
        while True:
            current_state: IState = self.state_store.get_stored_item()
            current_state.run()
