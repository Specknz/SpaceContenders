from abc import ABC, abstractmethod

class IStore(ABC):
    
    @abstractmethod
    def update(self):
        ...
        
    @abstractmethod
    def get_stored_item(self):
        ...