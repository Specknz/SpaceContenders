import pygame
from Models.ui import UI
from Models.ship import Ship
from Models.bullet import Bullet
from Stores.game_state_store import GameStateStore


class EventHandler:
    def __init__(self, pyg: pygame, ui: UI, game_state_store: GameStateStore, ships: list[Ship]):
        self.__pyg = pyg
        self.__ui = ui
        self.__game_state_store = game_state_store
        self.__ships = ships


    def handle_events(self) -> None:
        for event in self.__pyg.event.get():
                if self.__handle_quit(event):
                    return False
                self.__handle_key_down(event)      
        self.__handle_movement()
        self.__handle_bullet_collision()
        
        if self.__handle_ship_health_depleted():
            self.__game_state_store.GAME_RESTART_MENU = True
            
        return True
        
               
    def __handle_quit(self, event) -> bool:
        if event.type == self.__pyg.QUIT:
            self.__pyg.quit()
            return True
        return False


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
                bullet.move(ship.spawn_side)
                         
    
    def __handle_bullet_collision(self):
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
                
                
    def __handle_ship_health_depleted(self):
        for ship in self.__ships:
            if ship.health <= 0:
                self.__handle_win(ship)
                return True
            
            
    def __handle_win(self, ship: Ship):
        losing_side = ship.spawn_side
        winning_ships = " ".join([str(ship) for ship in self.__ships if ship.spawn_side != losing_side]) 
        win_text = winning_ships + " win the match!"
        self.__ui.draw_winner_text(win_text)
        
        