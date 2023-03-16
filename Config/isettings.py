from abc import ABC


class ISettings(ABC):
    ship_health: int
    fps: int
    font_path: str
    shoot_sfx_path: str
    explosion_sfx_path: str
    