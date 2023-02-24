import pygame
from UI.game_ui import GameUI
from Models.ship import Ship
from Models.bullet import Bullet
from Stores.game_state_store import GameStateStore
import Services.ship_shoot_service as ShipShootService
import Services.ship_movement_service as ShipMovementService


class GameEventHandler:
    def __init__(self, pyg: pygame, ui: GameUI, ships: list[Ship]):
        self.__pyg = pyg
        self.__ui = ui
        self.__ships = ships


    def handle_events(self):
        for event in self.__pyg.event.get():
            
                if self.__quit(event):
                    return False
                
                self.__key_down(event)
                 
        self.__movement()
        self.__bullet_collision()
        
        if self.__ship_health_zero():
            pass
            
        return True
        
               
    def __quit(self, event) -> bool:
        
        if event.type == self.__pyg.QUIT:
            self.__pyg.quit()
            return True
        
        if self.__key_pressed(event.type):
            if event.key == self.__pyg.K_ESCAPE:
                self.__pyg.quit()
                return True
            
        return False


    def __key_down(self, event) -> None:
        if self.__key_pressed(event.type):
            for ship in self.__ships:
                if self.__shoot_key_pressed(event.key, ship):
                    ShipShootService.shoot(ship)
      
                    
    def __key_pressed(self, event_type) -> bool:
        return event_type == self.__pyg.KEYDOWN   
                    
    
    def __shoot_key_pressed(self, key, ship: Ship) -> bool:
        return key == ship.control_scheme["SHOOT"]


    def __movement(self):
        for ship in self.__ships:
            ShipMovementService.move(ship, self.__pyg.key.get_pressed())  
            for bullet in ship.shot_bullets:
                bullet.move(ship.spawn_side)
                         
    
    def __bullet_collision(self):
        for bullet_owner in self.__ships:
            for bullet in bullet_owner.shot_bullets:
                self.__handle_bullet_wall_collision(bullet_owner, bullet)
                if (bullet in bullet_owner.shot_bullets):
                    self.__handle_bullet_ship_collision(bullet_owner, bullet)
    
    
    def __handle_bullet_wall_collision(self, bullet_owner: Ship, bullet: Bullet) -> None:
        if bullet.rect.x < 0 or (bullet.rect.x + bullet.WIDTH) >= self.__ui.WIN_WIDTH:
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
        self.__ui.draw_winner_text(win_text)
        
        