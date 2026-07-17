#MALO
class SensorManager: 
    def __init__(self, port: str) -> None:
        self.port = port
    def read_raw_value(self) -> str: 
        return 1023.0
    def calibre(self,raw_value: float) -> float:
        return (raw_value *3.3 /1024.0 ) * 100.0
    def save_to_file(self, value: float) -> None: 
        with open("sensor_data.txt", "a") as f:
            f.write(f"Reading: {value}\n")
#BUENO
class HardwareReader: 
    def __init__(self, port: str) -> None:
        self.port = port
    def read_raw(self) -> float:
        return 1023.0 
    
class CalibrationEngine: 
    @staticmethod
    def to_celsius(raw_value: float) -> float:
        return (raw_value * 3.3 / 1024.0) * 100.0
    
class LogPersister:
    def __init__(self, filename: str) -> None: 
        self.filename = filename
    def save(self, value:float) -> None: 
        with open(self.filename, "a") as f:
            f.write(f"Reading: {value}\n")
