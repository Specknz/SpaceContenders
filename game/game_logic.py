from ship.ship import Ship


def create_ships() -> list[Ship]:
    return (
        Ship(image_path='ship_yellow.png', spawn_side='left'), 
        Ship(image_path='ship_red.png', spawn_side='right')
    )


def ship_check_for_loss(ships: list[Ship]) -> Ship:
    for ship in ships:
        if ship.health == 0:
            return ship