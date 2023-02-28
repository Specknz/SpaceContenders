from States.istate import IState


class StateStore:
    
    def __init__(self, initial_state: IState):
        self.current_state: IState = initial_state
    
    def UpdateState(self, new_state: IState):
        self.current_state = new_state