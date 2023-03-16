from Models.ship import Ship
from Models.bullet import Bullet
from Models.spawn_side import SpawnSide

 
def create_bullet(ship: Ship):
    x_adjust = __get_bullet_x_spawn_adjustment(ship)

    x = ship.rect.x + x_adjust - (Bullet.WIDTH/2)
    y = ship.rect.y + (ship.HEIGHT/2) - (Bullet.HEIGHT/2)
        
    return Bullet(x, y)


def __get_bullet_x_spawn_adjustment(ship: Ship):
        if ship.spawn_side == SpawnSide.Left:
            return ship.WIDTH
        
        return 0