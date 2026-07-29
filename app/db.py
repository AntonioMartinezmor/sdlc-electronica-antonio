# a partir de este archivo creamos la clase madre para todos los modelos del proyecto 
from sqlalchemy import create_engine 
from sqlalchemy.orm import DeclarativeBase, sessionmaker 

class Base(DeclarativeBase):#clase madre/se usara en distintas partes del API
    pass 

engine = create_engine("sqlite:///sensorhub.db", echo= True)#crea el enlace con sensorhub

SessionLocal = sessionmaker(bind = engine)#genera sesiones cada vez que se necesite comunicar
# con la base de datos  
