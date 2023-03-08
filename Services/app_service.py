import pygame
import Factories.store_factory as StoreFactory

from Factories.app_factory import AppFactory
from dataclasses import dataclass
from States.istate import IState


@dataclass
class AppService():
    pyg: pygame
    clock: pygame.time.Clock
    app_factory: AppFactory

    def setup(self):
        self.state_store = StoreFactory.state()
        self.state_factory = self.app_factory.state(self.pyg, self.state_store)
        self.state_store.update(self.state_factory.main_menu())

    def run(self):
        while True:
            current_state: IState = self.state_store.get_stored_item()
            current_state.run()