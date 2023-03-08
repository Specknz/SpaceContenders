from Factories.app_factory import AppFactory
from Services.app_service import AppService
from Services.logger_setup_service import setup_logger
from Services.pygame_setup_service import setup_pygame


def main():
    setup_logger()
    
    pyg = setup_pygame()
    clock = pyg.time.Clock()
    
    app_factory = AppFactory(pyg, clock)
    app_service = AppService(pyg, clock, app_factory)
    app_service.setup()
    app_service.run()
    

if __name__ == "__main__":
    main()
