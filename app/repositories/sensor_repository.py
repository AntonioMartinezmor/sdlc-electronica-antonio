#se desarrollo un repositorio para el nuevo sensor siguiendo la guia de readings repositorio 
from typing import Optional 
from sqlalchemy import select
from sqlalchemy.orm import Session 
from app.models.sensor import Sensor
from app.schemas.sensor import SensorCreate

class SensorRepository:
    def __init__(self,db:Session):
        self.db=db

    def create(self,sensor:Sensor)->Sensor: 
        self.db.add(sensor)
        self.db.commit()
        self.db.refresh(sensor)
        return sensor 

    def get_all(self,limit:int=10, offset: int=0) -> list[Sensor]:
        stmt = select(Sensor).limit(limit).offset(offset)
        return list(self.db.scalars(stmt))

    def get_by_id(self,sensor_id: int) -> Optional[Sensor]:
        return self.db.get(Sensor, sensor_id)

    def update(self,sensor: Sensor, data:SensorCreate) -> Sensor: 
        sensor.name = data.name
        sensor.sensor_type = data.sensor_type
        sensor.location = data.location 
        self.db.commit()
        self.db.refresh(sensor)
        return sensor

    def delete(self,sensor: Sensor) ->None:
        self.db.delete(sensor)
        self.db.commit()
