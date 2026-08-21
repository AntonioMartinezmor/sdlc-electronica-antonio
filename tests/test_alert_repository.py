from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.db import Base
from app.models.alert import Alert
from app.repositories.alert_repository import AlertRepository


def _get_session():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def test_create_alert():
    db = _get_session()
    repo = AlertRepository(db)
    alert = Alert(sensor_id="SENSOR_01", reading_id=1, message="fuera de rango")
    creada = repo.create(alert)
    assert creada.id is not None
    assert creada.status == "open"


def test_get_all_filtra_por_status():
    db = _get_session()
    repo = AlertRepository(db)
    repo.create(Alert(sensor_id="S1", reading_id=1, message="a"))
    resuelta = Alert(sensor_id="S1", reading_id=2, message="b", status="resolved")
    repo.create(resuelta)

    abiertas = repo.get_all(status="open")
    assert len(abiertas) == 1
    assert abiertas[0].message == "a"


def test_update_status():
    db = _get_session()
    repo = AlertRepository(db)
    alert = repo.create(Alert(sensor_id="S1", reading_id=1, message="a"))
    actualizada = repo.update_status(alert.id, "acknowledged")
    assert actualizada.status == "acknowledged"