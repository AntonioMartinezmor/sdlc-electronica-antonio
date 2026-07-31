#este documento genera la estructura de la tabla de para la 
#base de datos, reading de datos. Ahora con tiempo incluido
from datetime import datetime, timezone 
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base 

class Reading(Base):
    __tablename__="readings" # le damos un nombre a la tabla 
    # donde se guardan los datos / a la base de datos 

    id: Mapped[int] = mapped_column(primary_key=True)# identificador unico para 
    #cada fila
    sensor_id: Mapped[str]
    value: Mapped[float]
    unit: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(#en esta version creamos
    #una columna que guarda automaticamente la fecha y hora de creacion de la fila
        default= lambda: datetime.now(timezone.utc) #la pieza clave la encontramos
        # en timezone.utc que corresponde a tiempo universal, sin zona horaria local
    )