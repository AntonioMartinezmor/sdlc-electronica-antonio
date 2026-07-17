from abc import ABC, abstractmethod

#MALO 

class BadTxtLogger:
    def log(self, message:str ) -> None:
        with open("log_malo.txt","a") as f:
            f.write(f"{message}\n")

class BadDataProcessor: 
    def __init__(self) -> None:
        self.logger = BadTxtLogger()

    def process(self, value:float)->None: 
        message = f"{value} procesado "
        self.logger.log(message)

#BUENO

class ILogger(ABC):
    @abstractmethod
    def log(self,message:str) -> None:
        pass
class GoodTxtLogger(ILogger):
    def log(self, message:str)->None:
        with open("log_bueno.txt","a") as f:
            f.write(f"{message}\n")

class GoodConsoleLogger(ILogger):
    def log(self, message:str)->None:
        print(f"acceso a la consola: {message}")
class GoodDataProcessor: 
    def __init__(self, logger:ILogger) -> None:
        self.logger = logger
    def process (self, value:float)-> None:
        message = f"{value} procesado"
        self.logger.log(message)



