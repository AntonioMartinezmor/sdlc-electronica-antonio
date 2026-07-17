import pytest 
from solid_isp import BadSimpleWaterSensor, GoodSimpleWaterSensor

def test_bad_sensor_forces_unused_methods() -> None: 
    sensor= BadSimpleWaterSensor()
    with pytest.raises(NotImplementedError):
        sensor.calibrate_sensor()

def test_good_sensor_only_implements_what_it_needs() -> None:
    sensor = GoodSimpleWaterSensor()
    result = sensor.read_value()
    assert result==1.0
    assert not hasattr(sensor, 'calibreted_sensor ')
    assert not hasattr(sensor, 'trigger_alarm')