from abc import ABC, abstractmethod


class IFactory(ABC):
    
    @abstractmethod
    def main_menu(self):
        ...
        
    @abstractmethod
    def game(self):
        ...
        
    @abstractmethod
    def game_finish(self):
        ...