from enum import Enum,auto
from dataclasses import dataclass
from datetime import datetime

class SensorType(Enum):#Enum es una clase que nos permite crear enumeraciones, 
   #estas dos son las enumeraciones que vamos a usar para definir el tipo de sensor
    TEMPERATURE = auto()
    HUMIDITY = auto()

@dataclass(frozen=True)#decorador que nos permite crear una clase inmutable (una vez creada no se puede modificar)
class Reading: #esta es la clase que definimoso construimos
    #todo lo siguente son las caracteriticas de la clase tambien conocidas como atributos
    #una instacia de la clase es un objeto que tiene las caracteristicas definidas en la clase
    sensor_id: str
    sensor_type: SensorType
    value: float
    timestamp: datetime

#acontinuacion definimos las funciones que trabajaran con la clase reading
def is_over_limit(reading: Reading, limit: float) -> bool:
    return reading.value > limit
 
def to_fahrenheit(reading: Reading) -> float:
    if reading.sensor_type != SensorType.TEMPERATURE: 
        raise ValueError("Sensor type must be TEMPERATURE to convert to Fahrenheit")
    return (reading.value * 9/5) + 32

def filter_by_type(readings: list[Reading],target_type: SensorType) -> list[Reading]:
    return [r for r in readings if r.sensor_type == target_type]

def calculate_average(readings: list[Reading]) -> float:
    if not readings:
        return 0.0
    total = sum(r.value for r in readings)
    return total / len(readings)
def serialize_for_uart(reading: Reading) -> str:
    timestamp_str = reading.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    return f"{reading.sensor_id},{reading.sensor_type.name},{reading.value},{timestamp_str}"
# con esto completamos el trabajo del primer dia/semana 1 para poder echarlo
#a andar se debe de utilizar una parte de codigo extra que se encargara de 
# dare uso a la clase definida

