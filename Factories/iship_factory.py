from abc import ABC, abstractmethod


class IShipFactory(ABC):
    
    @abstractmethod
    def create_1v1_ships(self):
        ...