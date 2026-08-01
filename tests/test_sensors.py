from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.main import app 
from app.db import Base
from app.routers.sensor import get_db

test_engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread":False},
    poolclass=StaticPool,
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

def test_create_sensor_success():
    response = client.post("/sensors", json={
        "name":"Sensor Bodega Norte",
        "sensor_type": "temperature",
        "location": "Bodega Norte"

    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Sensor Bodega Norte"
    assert "id" in data

def test_get_sensor_by_id_success():
    create_response = client.post("/sensors", json={
        "name": "Sensor Test Get",
        "sensor_type": "humidity",
        "location": "Bodega Sur"
    })
    sensor_id = create_response.json()["id"]
    response = client.get(f"/sensors/{sensor_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "Sensor Test Get"
    
def test_get_sensor_by_id_not_found():
    response = client.get("/sensors/999999")
    assert response.status_code == 404

def test_udate_sensor_success():
    create_response = client.post("/sensors", json={
        "name": "Sensor Original",
        "sensor_type": "temperature",
        "location": "Ubicacion Original"
    })
    sensor_id = create_response.json()["id"]
    
    response = client.put(f"/sensores/{sensor_id}", json={
        "name": "Sensor Actualizado",
        "sensor_type": "temperature",
        "location": "Nueva Ubicacion"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Sensor Actualizado"

def test_update_sensor_not_found():
    response = client.put("/sensors/999999", json={
        "name": "No Existe", 
        "sensor_type": "temperature",
        "location": "Nada"
    })
    assert response.status_code == 404

def test_delete_sensor_success():
    create_response = client.post("/sensor", json={
        "name": "Sensor A Borrar", 
        "sensor_type": "humidity",
        "location": "Temporal"
    })
    sensor_id = create_response.json()["id"]

    response = client.delete(f"/sensors/{sensor_id}")
    assert response.status_code == 200 

    confirm_response = client.get(f"/sensors/{sensor_id}")
    assert confirm_response.status_code == 404

def test_delete_sensor_not_found():
    response = client.delete("/sensors/999999")
    assert response.status_code == 404

def test_list_sensors():
    client.post("/sensors", json={
        "name": "Sensor Lista 1", 
        "sensor_type": "temperature",
        "location": "A"
    })
    response = client.get("/sensors")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
