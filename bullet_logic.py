from Models.bullet import Bullet
from Models.ship import Ship
from Models.ui import UI
from Stores.ships_store import ShipsStore


def move_bullets(ship_store: ShipsStore):
    ships = ship_store.ships
    
    for ship in ships:
        if ship == ships[0]:
            enemy_ship = ships[1]
        else:
            enemy_ship = ships[0]

        for bullet in ship.shot_bullets:

            if ship.spawn_side == "left":
                bullet.rect.x += Bullet.SPEED

            if ship.spawn_side == "right":
                bullet.rect.x -= Bullet.SPEED

            __check_bullet_wall_collision(ship, bullet)
            __check_bullet_player_collision(ship, bullet, enemy_ship) 
            
            
def __check_bullet_wall_collision(ship, bullet) -> None:
        if bullet.rect.x < 0 or (bullet.rect.x + Bullet.WIDTH) >= UI.WIN_WIDTH:
            ship.shot_bullets.remove(bullet)


def __check_bullet_player_collision(ship, bullet, enemy_ship) -> None:
    if ship.spawn_side == "left":
        if (bullet.rect.x + Bullet.WIDTH) >= enemy_ship.rect.x and bullet.rect.x <= (enemy_ship.rect.x + Ship.HEIGHT):
            if bullet.rect.y >= enemy_ship.rect.y and bullet.rect.y <= (enemy_ship.rect.y + Ship.WIDTH):
                enemy_ship.health -= 1
                ship.shot_bullets.remove(bullet)

    if ship.spawn_side == "right":
        if bullet.rect.x >= enemy_ship.rect.x and bullet.rect.x <= (enemy_ship.rect.x + Ship.HEIGHT):
            if bullet.rect.y >= enemy_ship.rect.y and bullet.rect.y <= (enemy_ship.rect.y + Ship.WIDTH):
                enemy_ship.health -= 1
                ship.shot_bullets.remove(bullet)
                    