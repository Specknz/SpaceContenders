from abc import ABC, abstractmethod


class IState(ABC):
    
    @abstractmethod
    def run():
        ...