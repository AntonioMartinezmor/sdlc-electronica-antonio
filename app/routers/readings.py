#este es el segundo endpoint creado; busca tener relacion con el  
#pasada con sensores, logrando lectura de datos  a manera de lectura 
from fastapi import APIRouter
from app.schemas.reading import ReadingCreate
from app.models.reading import Reading
from app.db import SessionLocal # aqui tenemos la aparicion del creador de sesiones

router= APIRouter()#creamos un servidor (mini) para utilizar un endpoint

@router.post("/readings")#establece el uso de este router para que responda a peticiones post
def create_reading(reading: ReadingCreate): # validacion de JSON y entrega de datos como
    #objeto python 
    db = SessionLocal()#inicia la comunicacion con la base de datos
    try: #a traves de try ejecutamos parte de codigo que sin importa funcione o no 
        #finally al final se ejecuta; dentro de try encontramos la traduccion de los 
        #datos recibidos 
        new_reading = Reading(
            sensor_id = reading.sensor_id,
            value = reading.value,
            unit = reading.unit,
        )
        db.add(new_reading)#prepara los datos para ser guardados 
        db.commit()#se escribe la informacion
        db.refresh(new_reading)# se actualiza lainformacion en memoria para
        # dar lugar al id asignado al dato
        return {"id": new_reading.id, "sensor_id": new_reading.sensor_id,
                "value": new_reading.value, "unit": new_reading.unit} # se regreasa la id como
                #prueba del exito del sistema
    finally:
        db.close()#se cierra sesion sin importar si haya funcionado o no