#La funcion dentro de este router cambio, para dar paso al tabajo en capas es decir
#delega trabajo a otras instancias para no manejar la base de datos desde aqui
#recurriendo ahora a principios SOLID; esta version cuenta con un router con verbo GET
from datetime import datetime
from typing import Optional 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.reading import ReadingCreate
from app.repositories.reading_repository import ReadingRepository
from app.services.reading_service import ReadingService
from app.dependencies import get_db
from app.services.alert_service import AlertService
from app.services.anomaly_strategies import Threshold_Anomaly_Strategy

router= APIRouter()#creamos un servidor (mini) para utilizar un endpoint
@router.post("/readings")
def create_reading(reading: ReadingCreate, db: Session = Depends(get_db)):
    # 1. Evaluamos la anomalía con las clases nuevas
    strategy = Threshold_Anomaly_Strategy(min_threshold=-20.0, max_threshold=80.0)
    alert_service = AlertService(strategy=strategy)
    anomaly_result = alert_service.process_reading(reading)

    # 2. Guardamos mediante la capa de repositorio/servicio
    repository = ReadingRepository(db)
    service = ReadingService(repository)
    saved_reading = service.create_reading(reading)

    # 3. Retornamos la lectura guardada directamente para mantener la compatibilidad con test_readings.py
    # Y si ocurrió anomalía, podemos adjuntar el flag en la entidad o retornarla limpia
    return saved_reading


@router.get("/readings")
def list_readings(
    limit: int=10,
    offset: int = 0,
    start_date: Optional[datetime]=None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db),

):#ademas con ayuda de fastapi al tener parametros simples son interpretados como parte del url 
    repository = ReadingRepository(db)
    service = ReadingService(repository)
    return service.get_readings(limit,offset, start_date, end_date)

@router.get( "/readings/{reading_id}")#con las llaves le decimos al metodo 
# que tomemos una parte especifica del url para usarlo aqui
def get_reading(reading_id: int, db: Session= Depends(get_db)):
    repository = ReadingRepository(db)
    service = ReadingService(repository)
    reading = service.get_reading_by_id (reading_id)
    if reading is None:
        raise HTTPException(status_code=404, detail="Reading not found")
        #con ayuda de HTTP logramos detener la ejecucion para responder con un 
        # codigo especifico
    return reading

@router.put("/readings/{reading_id}")
def update_reading(reading_id:int, data:ReadingCreate, db:Session=Depends(get_db)):
    repository = ReadingRepository(db)
    service = ReadingService(repository)
    reading = service.update_reading(reading_id, data)
    if reading is None: 
        raise HTTPException(status_code=404,detail="Reading not found")

    return reading

@router.delete("/readings/{reading_id}")
def delete_reading(reading_id: int, db:Session = Depends(get_db)):
    repository = ReadingRepository(db)
    service = ReadingService(repository)
    success = service.delete_reading(reading_id)
    if not success: 
        raise HTTPException(status_code=404,detail="Reading not found")
    return {"message": "Reading deleted successfully"}

