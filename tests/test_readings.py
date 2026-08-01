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

def test_get_reading_by_id_success():
    create_response = client.post("/readings", json={
        "sensor_id": "TEST_GET_01",
        "value": 15.0,
        "unit":"celsius"
    })
    reading_id = create_response.json()["id"]

    response = client.get(f"/readings/{reading_id}")
    assert response.status_code == 200
    assert response.json()["sensor_id"] =="TEST_GET_01"


def test_get_reading_by_id_not_found():
    response = client.get("/readings/999999")
    assert response.status_code == 404

def test_update_reading_success():
    create_response = client.post("/readings", json={
        "sensor_id": "TEST_UPDATE_01",
        "value": 10.0,
        "unit": "celsius"
    })
    reading_id = create_response.json()["id"]
    response = client.put(f"/readings/{reading_id}", json={
        "sensor_id": "TEST_UPDATE_MODIFICADO",
        "value": 50.0, 
        "unit": "fahrenheit"
    })
    assert response.status_code == 200
    assert response.json()["sensor_id"] == "TEST_UPDATE_MODIFICADO"
    assert response.json()["value"] == 50.0

def test_update_reading_not_found():
    response = client.put("/readings/999999", json={
        "sensor_id": "NO_EXISTE",
        "value": 1.0,
        "unit": "celsius"
    })
    assert response.status_code == 404

def test_delete_reading_success():
    create_response = client.post("/readings", json={
        "sensor_id": "TEST_DELETE_01",
        "value": 5.0,
        "unit":"celsius"

    })
    reading_id = create_response.json()["id"]
    
    response = client.delete(f"/readings/{reading_id}")
    assert response.status_code == 200

    confirm_response = client.get(f"/readings/{reading_id}")
    assert confirm_response.status_code == 404

def test_delete_reading_not_found():
    response = client.delete("/readins/999999")
    assert response.status_code ==404