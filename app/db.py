# a partir de este archivo creamos la clase madre para todos los modelos del proyecto 
import os
from sqlalchemy import create_engine 
from sqlalchemy.orm import DeclarativeBase, sessionmaker 

class Base(DeclarativeBase):#clase madre/se usara en distintas partes del API
    pass 

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///sensorhub.db")#con ayuda de os y environ. get obtenemos 
#la direccion url de la base de datos, ademas nos da una opcion de no funcionar environ.get gracias a get 

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
#establezco los parametros de conexion, deshabilitando el bloqueo de uso de multiples threads en sqlite
# y evaluando que DATABASE_URL comience con  sqlite, de no hacerlo los parametros quedan en blanco
engine = create_engine(DATABASE_URL, echo=True, connect_args= connect_args)
#con engine arrancamos en si la base de datos, donde la variable engine es una 
#base de conexiones donde se traducen comando a sql

SessionLocal = sessionmaker(bind=engine)
#assignamos a sessionlocal una conexion creada por sessionmaker ocupando como motor
# y base a conectar la que en engine este 
  
