import pygame
from Config.isettings import ISettings
from Services.audio_service import AudioService


def audio_service(pyg: pygame, settings: ISettings):
    return AudioService(pyg, settings)