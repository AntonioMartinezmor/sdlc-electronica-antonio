from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.schemas.sensor import SensorCreate
from app.repositories.sensor_repository import SensorRepository
from app.services.sensor_service import SensorService
from app.db import SessionLocal 

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sensors")
def create_sensor(sensor:SensorCreate, db:Session=Depends(get_db)):
    repository = SensorRepository(db)
    service = SensorService(repository)
    return service.create_sensor(sensor)


@router.get("/sensors")
def list_sensors(limit:int=10, offset:int=0, db: Session=Depends(get_db)):
    repository = SensorRepository(db)
    service = SensorService(repository)
    return service.get_sensors(limit,offset)

@router.get("/sensors/{sensor_id}")
def get_sensor(sensor_id:int,db:Session=Depends(get_db)):
    repository= SensorRepository(db)
    service = SensorService(repository)
    sensor = service.get_sensor_by_id(sensor_id)
    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor 

@router.put("/sensors/{sensor_id}")
def update_sensor(sensor_id: int, data: SensorCreate, db: Session=Depends(get_db)):
    repository=SensorRepository(db)
    service = SensorService(repository)
    sensor = service.update_sensor(sensor_id,data)
    if sensor is None:
        raise HTTPException(status_code=404,detail="Sensor not found")
    return sensor 

@router.delete("/sensors/{sensor_id}")
def delete_sensor(sensor_id:int,db:Session=Depends(get_db)):
    repository = SensorRepository(db)
    service = SensorService(repository)
    succes = service.delete_sensor(sensor_id)
    if not succes:
        raise HTTPException(status_code=404, detail="sensor not found")

    return{"message": "sensor deleted successfully"}

