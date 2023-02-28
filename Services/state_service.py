from dataclasses import dataclass
from Factories.state_factory import StateFactory

from Stores.state_store import StateStore


@dataclass
class StateService:
    state_store: StateStore
    state_factory: StateFactory
    
    def ChangeToGameState(self):
        self.state_store.Update(self.state_factory.create_game_state())