#este documento genera la estructura de la tabla de para la 
#base de datos para reading de datos 
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base 

class Reading(Base):
    __tablename__="readings" # le damos un nombre a la tabla 
    # donde se guardan los datos / a la base de datos 

    id: Mapped[int] = mapped_column(primary_key=True)# este es el identificador 
    # para las columnas siendo un identificador 
    sensor_id: Mapped[str]
    value: Mapped[float]
    unit: Mapped[str]
