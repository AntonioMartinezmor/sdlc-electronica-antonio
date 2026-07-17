from abc import ABC, abstractmethod
#MALO
class BadSensorReader: 
    def read_sensor(self, sensor_type: str) ->float:
        if sensor_type == "DHT11":
            return 24.5
        elif sensor_type == "LDR":
            return 512.0
        else:
            raise ValueError(f"sensor{sensor_type} no encontrado")
        
#BUENO
class SensorBase(ABC):
    @abstractmethod
    def read(self)-> float: 
        pass
class DHT11Sensor(SensorBase):
    def read(self) -> float:
        return 24.5
    
class LDRSensor(SensorBase):
    def read(self) -> float:
        return 512.0
    
class GoodSensorReader:
    def read_sensor(self, sensor: SensorBase) -> float:
        return sensor.read()