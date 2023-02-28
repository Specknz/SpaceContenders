from States.istate import IState


class StateStore:
    
    def __init__(self):
        self.__current_state: IState
    
    def Update(self, new_state: IState):
        self.__current_state = new_state
        
    def RunCurrentState(self):
        self.__current_state.run()