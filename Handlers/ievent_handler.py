from abc import ABC, abstractmethod


class IEventHandler(ABC):
    running: bool
    navigated: bool
    
    @abstractmethod
    def handle_events():
        ...
        
    # @abstractmethod
    # def navigate():
    #     ...