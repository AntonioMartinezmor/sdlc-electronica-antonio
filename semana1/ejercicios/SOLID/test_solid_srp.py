from solid_srp import CalibrationEngine, HardwareReader
def test_calibration_engine_calculates_currently() -> None:
    raw = 512.0
    expected_temp = 165.0 
    result = CalibrationEngine.to_celsius(raw)
    assert abs(result - expected_temp) < 0.001

def test_hardware_reader_returns_float() -> None:
    reader = HardwareReader(port="COM3")
    assert isinstance(reader.read_raw(), float)


