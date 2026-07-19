from enum import Enum, auto
class State(Enum): 
    RED = auto()
    GREEN = auto()

class TrafficlightFSM:

    def __init__(self) -> None:
        self.current_state = State.RED
        self.cycle_count: int = 0
    def transition(self) -> State:
        if self.current_state == State.RED:
            self.current_state = State.GREEN
        elif self.current_state == State.GREEN:
            self.current_state = State.RED 
            self.cycle_count += 1

        return self.current_state



