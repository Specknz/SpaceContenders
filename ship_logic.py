# from Models.ship import Ship
# from Models.ui import UI
# from Stores.ships_store import ShipsStore


# def move_ships(ship_store: ShipsStore, keys_pressed) -> None:
#     ships = ship_store.ships

#     for ship in ships:
#         # Move Ship LEFT
#         if keys_pressed[ship.control_scheme["LEFT"]] and (ship.rect.x - Ship.MOVE_SPEED) > 0:

#             if ship.spawn_side == "left":
#                 ship.rect.x -= Ship.MOVE_SPEED

#             elif ship.rect.x - Ship.MOVE_SPEED > UI.CENTER_LINE.x + UI.CENTER_LINE_WIDTH:
#                 ship.rect.x -= Ship.MOVE_SPEED

#         # Move Ship RIGHT
#         if keys_pressed[ship.control_scheme["RIGHT"]] and (ship.rect.x + Ship.MOVE_SPEED) + Ship.HEIGHT < UI.WIN_WIDTH:

#             if ship.spawn_side == "right":
#                 ship.rect.x += Ship.MOVE_SPEED

#             elif ship.rect.x + Ship.MOVE_SPEED < UI.CENTER_LINE.x - Ship.HEIGHT:
#                 ship.rect.x += Ship.MOVE_SPEED


#         # Move Ship UP
#         if keys_pressed[ship.control_scheme["UP"]] and (ship.rect.y - Ship.MOVE_SPEED) > 0:
#             ship.rect.y -= Ship.MOVE_SPEED

#         if keys_pressed[ship.control_scheme["DOWN"]] and (ship.rect.y + Ship.MOVE_SPEED) + Ship.WIDTH < UI.WIN_HEIGHT:
#             ship.rect.y += Ship.MOVE_SPEED

