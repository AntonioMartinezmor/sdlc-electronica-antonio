from typing import Dict,Any
from ps.src.sensor import SensorReading

class SensorFormatter: 
    def format_summary(self, reading:SensorReading) ->str:
        return (
            f"^^^^^^^^^^ RESUMEN DE LECTURA ^^^^^^^^^^\n"
            f"SENSOR: {reading.sensor_id}\n"
            f"Temp: {reading.temperature}°C\n"
            f"Hum: {reading.humidity}%\n"
             f"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
        )

    def to_dict(self,reading:SensorReading) -> Dict[str,Any]: 
        return{
            "sensor_id":reading.sensor_id,
            "temperature":f"{reading.temperature} °C",
            "humidity":f"{reading.humidity}%"
        }