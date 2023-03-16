import logging
from Models.ship import Ship
import Factories.bullet_factory as BulletFactory
from Services.audio_service import AudioService


def shoot(ship: Ship, audio_service: AudioService):
    if len(ship.shot_bullets) < ship.MAX_BULLETS:
        audio_service.shoot()
        bullet = BulletFactory.create_bullet(ship)
        ship.shot_bullets.append(bullet)
        logging.debug(f"{ship.color_text} ship shot")