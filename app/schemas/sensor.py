#desarrollamos este nuevo sensor como identidad propia 
#aprovechando que ya creamos diferentes bases 
#orientadas a los sensores ya utilizados
from pydantic import BaseModel

class SensorCreate(BaseModel): 
    name:str
    sensor_type: str
    location: str
    alert_threshold: float = 100.0