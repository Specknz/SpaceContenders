from Models.bullet import Bullet


class BulletFactory:
    
    def create_bullet(ship_x, ship_y, x_adjust, ship_width):

        x = ship_x + x_adjust - (Bullet.WIDTH/2)
        y = ship_y + (ship_width/2) - (Bullet.HEIGHT/2)
            
        return Bullet(x, y)