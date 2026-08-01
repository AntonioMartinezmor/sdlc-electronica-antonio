#Este archivo divide el trabajo que en readings se empleo para 
#guardar los datos que se reciban, buscando respetar los
# principios solid aprendidos en la primera semana. Ademas se agregan filtros 
# para paginacion de las lecturas.
from datetime import datetime 
from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.reading import Reading
from app.schemas.reading import ReadingCreate

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

     #definimos el siguente metodo a manera de filtro  
    def get_all(
        self,
        limit: int= 10, #valores determinados de respuestas 
        offset: int = 0, #ofrecidas
        start_date: Optional[datetime] = None, #de manera opcional se recibe la fecha 
        end_date: Optional[datetime] = None, # en la que se pretende buscar los datos
    ) ->list[Reading]: # el metodo nos devuelve una lista de las lecturas 
        stmt = select(Reading)  # es un constructor de consultas que por ahora define aun nada.
    

        if start_date is not None:  #esta es una condicion de busqueda, si nos 
            #dieron fecha aqui inicia la busqueda 
            stmt = stmt.where(Reading.created_at >= start_date)

        if end_date is not None:  #lo mismo que el de arriba pero con el final 
         #indice de busqueda
            stmt = stmt.where(Reading.created_at <= end_date)

        stmt = stmt.limit(limit).offset(offset)  #en esta linea se agrega la paginacion, ya 
        # con los limites impuestos 

        return list(self.db.scalars(stmt)) # por ultimo ejecutamos la consulta
        # contra la base de datos
    def get_by_id(self, reading_id: int)->Optional[Reading]:#recibimos la llave primaria 
        return self.db.get(Reading, reading_id)#recibe una posicion de la tabla y con
        #ayuda de SQLAlchemy encuentra la fila que corresponde a la llave primaria id 
        # si no recibe la llave primaria regresa un none

    #recibiendo el objeto reading y data de parte de http 
    def update(self , reading: Reading, data: ReadingCreate) -> Reading: 
        reading.sensor_id =  data.sensor_id
        reading.value = data.value
        reading.unit = data.unit
        self.db.commit()#confirmamos los cambios asignados en las anteriores lineas 
        self.db.refresh(reading)# sincronizamos los datos que habia como los que se asignaron ahora
        return reading
    #en este caso recibira el objeto ubicado 
    def delete(self, reading: Reading) -> None: 
        self.db.delete(reading)# marca el objeto para borrar 
        self.db.commit()




