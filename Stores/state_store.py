from Stores.istore import IStore
from States.istate import IState


class StateStore(IStore):
    
    def __init__(self):
        self.current_state: IState
    
    def update(self, new_state: IState):
        self.current_state = new_state
        
    def run_current_state(self):
        self.current_state.run()
        
    def get_stored_item(self) -> IState:
        return self.current_state