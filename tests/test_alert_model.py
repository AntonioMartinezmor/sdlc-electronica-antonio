from app.models.alert import Alert
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base

def test_alert_OCPD():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db = Session()

    alert = Alert(sensor_id="SENSOR_01", reading_id=1, message="Valor fuera de rango")
    db.add(alert)
    db.commit()
    db.refresh(alert)

    assert alert.status == "open"
    
