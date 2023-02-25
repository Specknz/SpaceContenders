import pygame
from UI.game_ui import GameUI
from Models.ship import Ship
from Models.bullet import Bullet
from dataclasses import dataclass
import Services.ship_shoot_service as ShipShootService
import Services.ship_movement_service as ShipMovementService
import Helpers.events_helper as EventsHelper
from UI.main_window import MainWindow


@dataclass
class GameEventHandler():
    pyg: pygame
    ui: GameUI
    
    def __init__(self, ships: list[Ship]):
        self.__ships = ships


    def handle_events(self):
        for event in self.pyg.event.get():
            if EventsHelper.quit_pressed(self.pyg, event.type):
                self.pyg.quit()
            if EventsHelper.key_pressed(self.pyg, event.type):
                if EventsHelper.go_back(self.pyg, event.key):
                    return False
                
                self.__key_down()
                 
        self.__movement()
        self.__bullet_collision()
        
        if self.__ship_health_zero():
            pass
            
        return True


    def __key_down(self, event_key) -> None:
        for ship in self.__ships:
            if self.__shoot_key_pressed(event_key, ship):
                ShipShootService.shoot(ship)
                    
    
    def __shoot_key_pressed(self, key, ship: Ship) -> bool:
        return key == ship.control_scheme["SHOOT"]


    def __movement(self):
        for ship in self.__ships:
            ShipMovementService.move(ship, self.pyg.key.get_pressed())  
            for bullet in ship.shot_bullets:
                bullet.move(ship.spawn_side)
                         
    
    def __bullet_collision(self):
        for bullet_owner in self.__ships:
            for bullet in bullet_owner.shot_bullets:
                self.__handle_bullet_wall_collision(bullet_owner, bullet)
                if (bullet in bullet_owner.shot_bullets):
                    self.__handle_bullet_ship_collision(bullet_owner, bullet)
    
    
    def __handle_bullet_wall_collision(self, bullet_owner: Ship, bullet: Bullet) -> None:
        if bullet.rect.x < 0 or (bullet.rect.x + bullet.WIDTH) >= MainWindow.WIDTH:
            bullet_owner.shot_bullets.remove(bullet)


    def __handle_bullet_ship_collision(self, bullet_owner: Ship, bullet: Bullet) -> None:        
        enemy_ships = [ship for ship in self.__ships if ship.spawn_side != bullet_owner.spawn_side]
        for enemy_ship in enemy_ships:
            if bullet.rect.colliderect(enemy_ship.rect):
                enemy_ship.damage()
                bullet_owner.shot_bullets.remove(bullet)
                
                
    def __ship_health_zero(self):
        for ship in self.__ships:
            if ship.health <= 0:
                self.__handle_win(ship)
                return True
            
            
    def __handle_win(self, ship: Ship):
        losing_side = ship.spawn_side
        winning_ships = " ".join([str(ship) for ship in self.__ships if ship.spawn_side != losing_side]) 
        win_text = winning_ships + " win the match!"
        self.ui.draw_winner_text(win_text)
        
        