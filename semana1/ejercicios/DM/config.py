from dataclasses import dataclass
@dataclass(frozen=True)
class UartConfing:
    baudrate: int
    def __post_init__(self): #despues de crear un objeto con dataclass procede a verificar en funcion de este, de ahi post init 
        if self.baudrate not in [9600, 19200, 115200]:
            raise ValueError("Rango comunicacion invalido")

        