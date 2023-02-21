import pygame
from Models.bullet import Bullet
from Models.ship import Ship
from Models.ui import UI


class EventHandler:
    def __init__(self, pyg: pygame, ships: list[Ship]):
        self.__pyg: pygame = pyg
        self.__ships: list[Ship] = ships


    def handle_events(self) -> None:
        for event in self.__pyg.event.get():
                self.__handle_quit(event)
                self.__handle_key_down(event)
        self.__handle_movement()
        self.__handle_bullet_collision()
                        
    def __handle_quit(self, event) -> None:
        if event.type == self.__pyg.QUIT:
            self.__pyg.quit()
    

    def __handle_key_down(self, event) -> None:
        if self.__key_pressed(event.type):
            for ship in self.__ships:
                
                if self.__shoot_key_pressed(event.key, ship):
                    ship.shoot()
                    
    def __key_pressed(self, event_type) -> bool:
        return event_type == self.__pyg.KEYDOWN   
                    
    
    def __shoot_key_pressed(self, key, ship: Ship) -> bool:
        return key == ship.control_scheme["SHOOT"]


    def __handle_movement(self):
        for ship in self.__ships:
            ship.move(self.__pyg.key.get_pressed())  
            for bullet in ship.shot_bullets:
                bullet.move()
                
                
                
    
    def __handle_bullet_collision(self):
        
        ship_index = 0
        for ship in self.__ships:
            if ship_index % 2 == 0:
                
                
            for bullet in ship.shot_bullets:
                self.__handle_bullet_wall_collision(ship, bullet)
                if (bullet in ship.shot_bullets):
                    self.__handle_bullet_ship_collision(ship, bullet)
    
    
    def __handle_bullet_wall_collision(self, ship: Ship, bullet) -> None:
        if bullet.rect.x < 0 or (bullet.rect.x + bullet.WIDTH) >= UI.WIN_WIDTH:
            ship.shot_bullets.remove(bullet)


    def __handle_bullet_ship_collision(self, current_ship: Ship, bullet: Bullet) -> None:
        # if ship.spawn_side == "left":
        #     if (bullet.rect.x + bullet.WIDTH) >= enemy_ship.rect.x and bullet.rect.x <= (enemy_ship.rect.x + Ship.HEIGHT):
        #         if bullet.rect.y >= enemy_ship.rect.y and bullet.rect.y <= (enemy_ship.rect.y + Ship.WIDTH):
        #             enemy_ship.health -= 1
        #             ship.shot_bullets.remove(bullet)

        # if ship.spawn_side == "right":
        #     if bullet.rect.x >= enemy_ship.rect.x and bullet.rect.x <= (enemy_ship.rect.x + Ship.HEIGHT):
        #         if bullet.rect.y >= enemy_ship.rect.y and bullet.rect.y <= (enemy_ship.rect.y + Ship.WIDTH):
        #             enemy_ship.health -= 1
        #             ship.shot_bullets.remove(bullet)
        
        enemy_ships = [ship for ship in self.__ships if ship.spawn_side != current_ship.spawn_side]
        
        for ship in enemy_ships:
            if bullet.rect.colliderect(ship.rect):
                ship.health -= 1
                current_ship.shot_bullets.remove(bullet)