from abc import ABC


class ISettings(ABC):
    ship_health: int
    fps: int
    font_path: str
    