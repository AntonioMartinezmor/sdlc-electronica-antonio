import pytest 
from ps.src.sensor import SensorReading
from ps.src.formatter import SensorFormatter

def test_format_summary_normal_reading(): 
    reading = SensorReading(sensor_id="BODEGA_01", temperature=22.5, humidity=55.0) 
    formatter= SensorFormatter()

    summary = formatter.format_summary(reading)

    assert "SENSOR:BODEGA_01" in summary
    assert "Temp: 22.5 °C" in summary 
    assert "Hum: 55.0%" in summary

def test_format_json_export():
    reading=SensorReading(sensor_id="BODEGA_02", temperature=18.0,humidity=40.0)
    formatter = SensorFormatter()
    data = formatter.to_dict(reading)

    assert data["sensor_id"] == "BODEGA_02"
    assert data["temperature"] == "18.0 °C"
    assert data ["humidity"] == "40.0%"
    
