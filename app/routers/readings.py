#este es el segundo endpoint creado; busca tener relacion con el  
#pasada con sensores, logrando lectura de datos  a manera de lectura 
from fastapi import APIRouter
from app.schemas.reading import ReadingCreate
from app.repositories.reading_repository import ReadingRepository
from app.services.reading_service import ReadingService
from app.db import SessionLocal # aqui tenemos la aparicion del creador de sesiones

router= APIRouter()#creamos un servidor (mini) para utilizar un endpoint

@router.post("/readings")#establece el uso de este router para que responda a peticiones post
def create_reading(reading: ReadingCreate): # validacion de JSON y entrega de datos como
    #objeto python 
    db = SessionLocal()#inicia la comunicacion con la base de datos
    repository = ReadingRepository(db)
    service = ReadingService(repository)
    return service.create_reading(reading)
