from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base 

class Alert(Base):
    __tablename__ = "alerts"

    id: Mapped[int] = mapped_column(primary_key=True)
    sensor_id: Mapped[str] = mapped_column(index=True)
    reading_id: Mapped[int]
    message: Mapped[str]
    status: Mapped[str]=mapped_column(default="open")
    created_at: Mapped[datetime] = mapped_column(default=lambda:datetime.now(timezone.utc))
    