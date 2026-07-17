import pytest
from solid_ocp import BadSensorReader, DHT11Sensor, LDRSensor, GoodSensorReader
def test_good_reader_with_dht11() -> None:
    reader = GoodSensorReader()
    sensor = DHT11Sensor()

    result = reader.read_sensor(sensor)
    assert result ==24.5

def test_good_reader_with_ldr() -> None:
    reader = GoodSensorReader()
    sensor = LDRSensor()
    result = reader.read_sensor(sensor)
    assert result == 512.0
    


