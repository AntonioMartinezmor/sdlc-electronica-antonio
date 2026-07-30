#Este archivo divide el trabajo que en readings se empleo para 
#guardar los datos que se reciban, buscando respetar los
# principios solid aprendidos en la primera semana.
from sqlalchemy.orm import Session
from app.models.reading import Reading

class ReadingRepository: # definimos una clase molde, para base de datos 
    #en readings
    def __init__(self, db:Session):
        self.db = db # guardamos la sesion creada como un objeto de la clase  

    def create(self, reading: Reading) -> Reading: # diseñamos una funcion que
        #recibe un reading y devuelve un Reading 
        self.db.add(reading)# marca el objeto reading como objeto a guardar  
        self.db.commit()#confirmamos la escritura del dato en la base de datos
        self.db.refresh(reading)#se actualizan los datos de reading a los que se 
        # registraron en la base de datos 
        return reading #devuelve el reading recibido y guardado, tambien el ID 
    

