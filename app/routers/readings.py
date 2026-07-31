#La funcion dentro de este router cambio, para dar paso al tabajo en capas es decir
#delega trabajo a otras instancias para no manejar la base de datos desde aqui
#recurriendo ahora a principios SOLID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.reading import ReadingCreate
from app.repositories.reading_repository import ReadingRepository
from app.services.reading_service import ReadingService
from app.db import SessionLocal # aqui tenemos la aparicion del creador de sesiones

router= APIRouter()#creamos un servidor (mini) para utilizar un endpoint

def get_db(): #funcion necesaria para el test
    db = SessionLocal()
    try: 
        yield db #parte clabe, de ser solicitado entrega
        # un session diferente que lleva a una base de datos diferente a la 
        # original para el test 

    finally:
        db.close()


@router.post("/readings")#establece el uso de este router para que responda a peticiones post
def create_reading(reading: ReadingCreate, db: Session = Depends(get_db)): # validacion de JSON y entrega de datos como
    #objeto python 
    repository = ReadingRepository(db) #se crea un objeto readingrepository y se entrega db 
    service = ReadingService(repository)# se crea otro objeto al que se le entrega el repository
    return service.create_reading(reading) # envia al servicio los datos validados, regresando 
    # que servicio devuelve
