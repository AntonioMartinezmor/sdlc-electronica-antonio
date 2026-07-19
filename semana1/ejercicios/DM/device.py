from config import UartConfing
from parsers import MessageParser

class UartDevice:
    def __init__(self,config: UartConfing, parser: MessageParser):
        self.confing = config
        self.parser  = parser
    
    def send(self,message:str) ->bytes:
        data= self.parser.encode(message)
        print(f"Enviado: {data}")
        return data 
    def receive(self, raw_bytes: bytes) ->str:
        return raw_bytes.decode("ascii")
    