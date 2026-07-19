import pytest
from solid_lsp import BadFaultySensor, GoodFailsafeSensor

def test_bad_sensor_violates_lps() -> None:
    sensor = BadFaultySensor()
    with pytest.raises(ConnectionError):
        sensor.get_reading()

def test_good_sensor_obeys_lsp() ->None:
    sensor = GoodFailsafeSensor()
    result = sensor.get_reading()
    assert isinstance(result, float)
    assert result == 0.0
    