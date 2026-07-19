from abc import  ABC, abstractmethod
class MessageParser(ABC):
    @abstractmethod
    def encode(self, message:str)-> bytes:
        pass

class ModbusParser(MessageParser):
    def encode(self, message:str)->bytes:
        return message.encode("ascii")

class NMEAParser(MessageParser):
    def encode(self,message:str)->bytes:
        return(message+"\r\n").encode("ascii")
    
    