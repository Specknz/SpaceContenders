import pygame
from Models.bullet import Bullet
from Models.ship import Ship
from Models.ui import UI


def move_ships(ships: list[Ship], keys_pressed) -> None:

    for ship in ships:
        # Move Ship LEFT
        if keys_pressed[ship.control_scheme["LEFT"]] and (ship.ship_rect.x - Ship.MOVE_SPEED) > 0:

            if ship.spawn_side == "left":
                ship.ship_rect.x -= Ship.MOVE_SPEED

            elif ship.ship_rect.x - Ship.MOVE_SPEED > UI.CENTER_LINE.x + UI.CENTER_LINE_WIDTH:
                ship.ship_rect.x -= Ship.MOVE_SPEED

        # Move Ship RIGHT
        if keys_pressed[ship.control_scheme["RIGHT"]] and (ship.ship_rect.x + Ship.MOVE_SPEED) + Ship.HEIGHT < UI.WIN_WIDTH:

            if ship.spawn_side == "right":
                ship.ship_rect.x += Ship.MOVE_SPEED

            elif ship.ship_rect.x + Ship.MOVE_SPEED < UI.CENTER_LINE.x - Ship.HEIGHT:
                ship.ship_rect.x += Ship.MOVE_SPEED


        # Move Ship UP
        if keys_pressed[ship.control_scheme["UP"]] and (ship.ship_rect.y - Ship.MOVE_SPEED) > 0:
            ship.ship_rect.y -= Ship.MOVE_SPEED

        if keys_pressed[ship.control_scheme["DOWN"]] and (ship.ship_rect.y + Ship.MOVE_SPEED) + Ship.WIDTH < UI.WIN_HEIGHT:
            ship.ship_rect.y += Ship.MOVE_SPEED


def shoot_ships(ships: list[Ship], key_pressed):

    for ship in ships:
        if key_pressed == ship.control_scheme["SHOOT"] and len(ship.shot_bullets) < Bullet.BULLET_MAX_AMOUNT:

            if ship.spawn_side == "left":
                x = ship.ship_rect.x + Ship.HEIGHT
                y = ship.ship_rect.y + (Ship.WIDTH/2) - (Bullet.BULLET_HEIGHT/2)

            if ship.spawn_side == "right":
                x = ship.ship_rect.x
                y = ship.ship_rect.y + (Ship.WIDTH/2) - (Bullet.BULLET_HEIGHT/2)
                
            bullet = pygame.Rect(x, y, Bullet.BULLET_WIDTH, Bullet.BULLET_HEIGHT)

            ship.shot_bullets.append(bullet)


def move_bullets(ships: list[Ship]):

    def __check_bullet_wall_collision() -> None:
        if bullet.x < 0 or (bullet.x + Bullet.BULLET_WIDTH) >= UI.WIN_WIDTH:
            ship.shot_bullets.remove(bullet)

    def __check_bullet_player_collision() -> None:
        if ship.spawn_side == "left":
            if (bullet.x + Bullet.BULLET_WIDTH) >= enemy_ship.ship_rect.x and bullet.x <= (enemy_ship.ship_rect.x + Ship.HEIGHT):
                if bullet.y >= enemy_ship.ship_rect.y and bullet.y <= (enemy_ship.ship_rect.y + Ship.WIDTH):
                    enemy_ship.health -= 1
                    ship.shot_bullets.remove(bullet)

        if ship.spawn_side == "right":
            if bullet.x >= enemy_ship.ship_rect.x and bullet.x <= (enemy_ship.ship_rect.x + Ship.HEIGHT):
                if bullet.y >= enemy_ship.ship_rect.y and bullet.y <= (enemy_ship.ship_rect.y + Ship.WIDTH):
                    enemy_ship.health -= 1
                    ship.shot_bullets.remove(bullet)
                    
    for ship in ships:
        if ship == ships[0]:
            enemy_ship = ships[1]
        else:
            enemy_ship = ships[0]

        for bullet in ship.shot_bullets:

            if ship.spawn_side == "left":
                bullet.x += Bullet.BULLET_SPEED

            if ship.spawn_side == "right":
                bullet.x -= Bullet.BULLET_SPEED

            __check_bullet_wall_collision()
            __check_bullet_player_collision() 