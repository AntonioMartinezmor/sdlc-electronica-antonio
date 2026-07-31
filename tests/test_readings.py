#se crea este codigo para testear el router readigns
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.main import app 
from app.db import Base
from app.routers.readings import get_db

test_engine = create_engine("sqlite:///:memory:", 
     connect_args= { "check_same_thread": False},
     poolclass= StaticPool                                                 
) 
TestSessionLocal = sessionmaker(bind=test_engine)
Base.metadata.create_all(bind=test_engine)

def override_get_db():
    db = TestSessionLocal()
    try: 
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_reading_success():
    response = client.post("/readings", json={
        "sensor_id": "TEST_SENSOR_01",
        "value":22.5,
        "unit":"celsius"

    })

    assert response.status_code == 200
    data = response.json()
    assert data["sensor_id"] == "TEST_SENSOR_01"
    assert data["value"] == 22.5
    assert "id" in data 

def test_create_reading_invalid_value():
    response =client.post("/readings", json={
        "sensor_id": "TEST_SENSOR_01",
        "value": "no soy un numero",
        "unit": "celsius"
    })
    assert response.status_code == 422