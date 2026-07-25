from abc import ABC, abstractmethod
from ps.src.sensor import SensorReading

class AnomalyDetector: 
    def __init__(self, max_temp:float =35.0, max_humidity: float= 80.0):
        self.max_temp = max_temp
        self.max_humidity = max_humidity

    def is_anomaly(self, reading: SensorReading)->bool: 
        return (
            reading.temperature > self.max_temp or
            reading.humidity >  self.max_humidity
        )

class AlertStrategy(ABC):
    @abstractmethod
    def send_alert(self, reading: SensorReading, message:str) -> None:
        pass

class ConsoleAlertStrategy(AlertStrategy):
    def send_alert(self, reading:SensorReading, message:str)-> None:
        print(f"[ALERTA CONSOLA] Sensor: {reading.sensor_id} | Mensaje: {message} | Temp: {reading.temperature} C | Hum: {reading.humidity}%")


class FileAlertStrategy(AlertStrategy):
    def __init__(self, file_path:str = "bitacora_alerts.log"):
        self.file_path=file_path
    def send_alert(self,reading: SensorReading,message:str)->None: 
        log_line = f"[BITACORA]Sensor:{reading.sensor_id}-{message} - Temp: {reading.temperature} C, Hum:{reading.humidity} %\n"
        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(log_line)

class AlertManager: 
    def __init__(self, strategy:AlertStrategy):
        self.strategy = strategy 
    def notify(self,reading:SensorReading, message:str) -> None:
        self.strategy.send_alert(reading,message)
        