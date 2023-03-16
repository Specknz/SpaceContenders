import pygame
import Factories.store_factory as StoreFactory

from Factories.app_factory import AppFactory
from dataclasses import dataclass
from Models.istate import IState


@dataclass
class AppService():
    pyg: pygame
    clock: pygame.time.Clock
    app_factory = AppFactory(pyg, clock)
    state_store = StoreFactory.state()

    def setup(self):
        self.state_factory = self.app_factory.state_factory(self.state_store)
        self.state_store.update(self.state_factory.main_menu())

    def run(self):
        while True:
            current_state: IState = self.state_store.get_stored_item()
            current_state.run()
