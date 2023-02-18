from Models.ship import Ship


class Bullet:
    
    BULLET_HEIGHT = 4
    BULLET_WIDTH = 10

    BULLET_MAX_AMOUNT = 6
    
    BULLET_SPEED = Ship.MOVE_SPEED + 2
    
    def __init__(self) -> None:
        pass