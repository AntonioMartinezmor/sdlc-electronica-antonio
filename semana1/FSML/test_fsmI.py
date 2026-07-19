from fsmI import TrafficlightFSM, State

# estado inicial y contador de ciclos
def test_initial_state() -> None:
    fsm = TrafficlightFSM()
    assert fsm.current_state == State.RED
    assert fsm.cycle_count == 0

# transicion y justificacion de la transicion
def test_transition_red_to_green() -> None:
    fsm = TrafficlightFSM()
    next_state = fsm.transition()
    assert next_state == State.GREEN
    assert fsm.current_state == State.GREEN
    assert fsm.cycle_count == 0

# justificacion de transicion 
def test_full_cycle_returns_to_red() -> None:
    fsm = TrafficlightFSM()
    fsm.transition()             
    next_state = fsm.transition()  
    assert next_state == State.RED
    assert fsm.current_state == State.RED

# validacion de conteo
def test_cycle_counting() -> None:
    fsm = TrafficlightFSM()
    


    fsm.transition()
    fsm.transition()
    assert fsm.cycle_count == 1

    fsm.transition()
    fsm.transition()
    assert fsm.cycle_count == 2