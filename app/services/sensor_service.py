from typing import Optional 
from app.models.sensor import Sensor 
from app.schemas.sensor import SensorCreate
from app.repositories.sensor_repository import SensorRepository

class SensorService: 
    def __init__(self,repository: SensorRepository):
        self.repository = repository

    def create_sensor(self, data: SensorCreate) ->Sensor: 
        sensor = Sensor(name=data.name, sensor_type=data.sensor_type, location= data.location, alert_threshold=data.alert_threshold,)
        return self.repository.create(sensor)

    def get_sensors(self, limit: int=10, offset:int=0) ->list[Sensor]:
        return self.repository.get_all(limit,offset)

    def get_sensor_by_id(self,sensor_id:int) -> Optional[Sensor]:
        return self.repository.get_by_id(sensor_id)

    def update_sensor(self,sensor_id:int, data:SensorCreate) -> Optional[Sensor]:
        sensor = self.repository.get_by_id(sensor_id)
        if sensor is None: 
            return None
        return self.repository.update(sensor,data)

    def delete_sensor(self, sensor_id: int) -> bool:
        sensor = self.repository.get_by_id(sensor_id)
        if sensor is None: 
            return False
        self.repository.delete(sensor)
        return True