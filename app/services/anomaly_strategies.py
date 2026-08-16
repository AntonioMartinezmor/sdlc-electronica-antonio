from abc import ABC, abstractmethod
from typing import Optional 
from app.schemas.reading import ReadingCreate

class Anomaly_Detection_Strategy(ABC):
    @abstractmethod
    def evaluate(self,reading:ReadingCreate) -> tuple[bool, Optional[str]]:
        pass 

class Threshold_Anomaly_Strategy(Anomaly_Detection_Strategy):
    def __init__(self, min_threshold: float, max_threshold: float):
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold

    def evaluate(self, reading: ReadingCreate) -> tuple[bool, Optional[str]]:

        if reading.value > self.max_threshold: 
            return True, f"valor {reading.value} excede el limite maximo de {self.max_threshold}"
        if reading.value < self.min_threshold: 
            return True, f"Valor {reading.value} esta por debajo del limite minimo de {self.min_threshold}"
        return False, None



class Unit_Boundary_Strategy(Anomaly_Detection_Strategy):
    DEFAULT_LIMITS = {
        "CELSIUS":(-40.0, 85.0),
        "PERCENTAGE": (0.0, 100.0),
        "PASCAL": (80000.0, 120000.0)
    }
    def evaluate(self, reading: ReadingCreate)->tuple[bool, Optional[str]]:
        unit_str = str(reading.unit).upper()

        if unit_str in self.DEFAULT_LIMITS: 
            min_val, max_val=self.DEFAULT_LIMITS[unit_str]
            if reading.value < min_val or reading.value > max_val: 
                return True, f"Valor {reading.value} fuera de rango fisico ({min_val} a {max_val}) para {unit_str}"

            return False, None