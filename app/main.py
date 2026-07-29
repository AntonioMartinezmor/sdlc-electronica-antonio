#Este es el archivo principal, encargado de manejar todo lo que creemos por
#partes, por ello se mandan a llamar routers y los modelos
from fastapi import FastAPI
from app.routers import health , readings
from app.db import Base, engine
from app.models import reading 

Base.metadata.create_all(bind=engine)# se crea la tabla para cualquier modelo 
#se crean fisicamente en sensorhub con ayuda de bind=engine

app = FastAPI(title="SensorHub")# es encargado de generar la aplicacion 
# con el nombre de sensorhub

app.include_router(health.router)# registra los servidores que nosotros 
app.include_router(readings.router)# construimos en routers para su posterior
# arranque con uvicorn