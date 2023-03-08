from Factories.state_factory import StateFactory
from Services.app_service import AppService

from Services.logger_setup_service import setup_logger
from Services.pygame_setup_service import setup_pygame
from Settings.settings import Settings
from Stores.state_store import StateStore


def main():
    setup_logger()
    
    pyg = setup_pygame()
    clock = pyg.time.Clock()
    settings = Settings()
    state_store = StateStore()
    state_factory: IFactory
    
    app_service = AppService()
    app_service.setup()
    app_service.run()
    

if __name__ == "__main__":
    main()
