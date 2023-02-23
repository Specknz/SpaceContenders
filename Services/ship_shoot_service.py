import logging
from Models.ship import Ship
import Factories.bullet_factory as BulletFactory


def shoot(ship: Ship):
    if len(ship.shot_bullets) < ship.MAX_BULLETS:
        bullet = BulletFactory.create_bullet(ship)
        ship.shot_bullets.append(bullet)
        logging.debug(f"{ship.color_text} ship shot")