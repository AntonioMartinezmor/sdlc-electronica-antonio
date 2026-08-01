#sentamos las bases para la BD, definiendo los 
#datos en las columnas
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base

class Sensor(Base):
    __tablename__="sensor"#le damos el nombre de sensor 

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    sensor_type: Mapped[str]
    location: Mapped[str]
