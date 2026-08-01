#Este codigo representa para el sistema como un filtro que pregunta
# que reglas hay que aplicar antes de guardar lo recibido; busca tambien la 
# aplicacion de los principios solid.
from datetime import datetime
from typing import Optional
from app.models.reading import Reading
from app.schemas.reading import ReadingCreate #importamos para poder recibir datos ya validados
# provinientes del router
from app.repositories.reading_repository import ReadingRepository

class ReadingService:
    def __init__(self, repository: ReadingRepository):
        self.repository = repository # guarda el repositorio como parte del objeto

    def create_reading(self, data: ReadingCreate) -> Reading: # desarrollamos un metodo para llevar 
        # una traduccion de los datos recibidos para entregar un Reading 
        reading = Reading(sensor_id=data.sensor_id, value=data.value, unit=data.unit)
        #la traduccion ocurre en esta linea construyendo un objeto del modelo SQLAlchemy
        return self.repository.create(reading) #enviamos el objeto recien creado al repositorio 
        #encargado de guardar los datos

    #creamos el metodo correspondiente para recibir datos de parte del router y los reenviamos 
    #tal cual se reciben 
    def get_readings(
        self,
        limit: int = 10,
        offset: int = 0,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> list[Reading]:
        return self.repository.get_all(
            limit=limit,
            offset=offset,
            start_date=start_date,
            end_date=end_date,
        )
    #esto debido a que no tenemos aun restricciones que agregar, simplemente estamos 
    # trabajando en capas