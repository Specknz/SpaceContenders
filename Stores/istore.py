from abc import ABC, abstractmethod

from States.istate import IState


class IStore(ABC):
    
    @abstractmethod
    def update(self, new_state: IState):
        ...
        
    @abstractmethod
    def get_stored_item(self):
        ...