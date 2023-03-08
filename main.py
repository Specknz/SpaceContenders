import Factories.store_factory as StoreFactory
import Factories.settings_factory as SettingsFactory

from Services.logger_setup_service import setup_logger
from Services.pygame_setup_service import setup_pygame
from Settings.isettings import ISettings
from Factories.state_factory import StateFactory


def main():
    setup_logger()
    
    pyg = setup_pygame()
    
    clock = pyg.time.Clock()
    settings: ISettings = SettingsFactory.settings()
    
    state_store = StoreFactory.state_store()
    state_factory = StateFactory(pyg, 
                                 clock, 
                                 settings,
                                 state_store)
    state_store.update(state_factory.main_menu())
      
    while True:
        state_store.run_current_state()
    

if __name__ == "__main__":
    main()
