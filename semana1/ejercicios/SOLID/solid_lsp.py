from abc import ABC, abstractmethod
#MALO
class BadSensor(ABC): 
     
    @abstractmethod
    def get_reading(self) ->float:
        pass

class BadWorkingSensor(BadSensor):
    def get_reading(self) -> float:
        return 25.0
    
class BadFaultySensor(BadSensor):
    def get_reading(self) -> float:
        raise ConnectionError("Sensor Desconectado Fisicamente")
    
#BUENO
    
class GoodSensor(ABC):
    @abstractmethod
    def get_reading(self) -> float:
        pass 
class GoodWorkingSensor(GoodSensor):
    def get_reading(self) -> float:
        return 25.0

class GoodFailsafeSensor(GoodSensor):
    def get_reading(self) -> float:
        try: 
            raise  ConnectionError ("Falla Hardware")
        except ConnectionError:
            return 0.0
        
        
