from fsmI import TrafficlightFSM, State

# Test 1: Validar el estado inicial de la FSM
def test_initial_state() -> None:
    fsm = TrafficlightFSM()
    # Al arrancar, debe estar en RED y con 0 ciclos
    assert fsm.current_state == State.RED
    assert fsm.cycle_count == 0

# Test 2: Validar la transición de RED a GREEN
def test_transition_red_to_green() -> None:
    fsm = TrafficlightFSM()
    next_state = fsm.transition()
    # Debe cambiar a GREEN y mantener el contador de ciclos en 0
    assert next_state == State.GREEN
    assert fsm.current_state == State.GREEN
    assert fsm.cycle_count == 0

# Test 3: Validar que un ciclo completo regresa a RED
def test_full_cycle_returns_to_red() -> None:
    fsm = TrafficlightFSM()
    fsm.transition()              # Primera transición: RED -> GREEN
    next_state = fsm.transition()  # Segunda transición: GREEN -> RED
    # Al regresar a RED, el estado final debe ser RED
    assert next_state == State.RED
    assert fsm.current_state == State.RED

# Test 4: Validar el conteo acumulado de ciclos completos
def test_cycle_counting() -> None:
    fsm = TrafficlightFSM()
    
    # Ciclo 1 (RED -> GREEN -> RED)
    fsm.transition()
    fsm.transition()
    assert fsm.cycle_count == 1
    
    # Ciclo 2 (RED -> GREEN -> RED)
    fsm.transition()
    fsm.transition()
    assert fsm.cycle_count == 2