from abc  import ABC, abstractmethod
#MALO
class BadMultiFunctionSensor(ABC):
    @abstractmethod
    def read_value(self) -> float:
        pass
    @abstractmethod 
    def calibrate_sensor(self)-> None: 
        pass
    @abstractmethod 
    def trigger_alarm(self)-> None:
        pass

class BadSimpleWaterSensor(BadMultiFunctionSensor):
    def read_value(self) -> float:
        return 1.0
    def calibrate_sensor(self) -> None:
        raise NotImplementedError("No soportado")
    def trigger_alarm(self):
        raise NotADirectoryError("No soportado")

#BUENO
class Readable(ABC):
    @abstractmethod
    def read_value(self) -> float:
        pass

class Calibratable(ABC):
    @abstractmethod
    def calibrate_sensor(self) ->None:
        pass

class Alarmable(ABC):
    @abstractmethod
    def trigger_alarm(self) -> None:
        pass

class GoodSimpleWaterSensor(Readable):
    def read_value(self) -> float:
        return 1.0

class GoodSmartThermalSensor(Readable, Calibratable, Alarmable):
    def read_value(self) -> float:
        return 24.5
    def calibrate_sensor(self) -> None:
        pass
    def trigger_alarm(self) -> None: 
        pass
