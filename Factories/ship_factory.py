from ship import Ship

class ShipFactory:
    
    def create_ships() -> list[Ship]:
        return [
            Ship(image_path='ship_yellow.png', spawn_side='left'), 
            Ship(image_path='ship_red.png', spawn_side='right')
        ]