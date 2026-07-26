import pytest
from ps.src.sensor import SensorReading

@pytest.fixture
def valid_reading_data():
    return{
        "sensor_id":"BODEGA_NORTE_01",
        "temperature":21.5,
        "humidity":45.0
    }
def test_sensor_reading_valid_data(valid_reading_data):
    reading = SensorReading(**valid_reading_data)
    assert reading.sensor_id == valid_reading_data["sensor_id"]
    assert reading.temperature == valid_reading_data["temperature"]
    assert reading.humidity ==valid_reading_data["humidity"]

def test_sensor_reading_invalid_humidity():
    with pytest.raises(ValueError,match="Humedad fuera de rango"):
        SensorReading(sensor_id="BODEGA_NORTE_01", temperature=20.0, humidity= 105.0)
