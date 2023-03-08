from abc import ABC, abstractmethod

from Handlers.ievent_handler import IEventHandler


class IState(ABC):
    event_handler: IEventHandler
    
    @abstractmethod
    def run(self):
        ...