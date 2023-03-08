from Stores.istore import IStore
from States.istate import IState


class StateStore(IStore):
    
    def __init__(self):
        self.__current_state: IState
    
    def update(self, new_state: IState):
        self.__current_state = new_state
        
    def get_stored_item(self) -> IState:
        return self.__current_state