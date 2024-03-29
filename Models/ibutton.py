from abc import ABC, abstractmethod


class IButton(ABC):
    WIDTH = 200
    HEIGHT = 70
    
    @abstractmethod
    def draw(self) -> None:
        ...
       
    @abstractmethod
    def collides(self, mouse_pos: tuple[int, int]) -> bool:
        ...