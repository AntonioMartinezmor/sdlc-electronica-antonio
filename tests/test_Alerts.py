import pytest
from datetime import datetime, timezone
from fastapi.testclient import TestClient

from app.main import app
from app.schemas.reading import ReadingCreate
from app.services.alert_service import AlertService
from app.services.anomaly_strategies import (
    Threshold_Anomaly_Strategy,
    Unit_Boundary_Strategy,
)

client = TestClient(app)


def test_threshold_anomaly_strategy_evaluation():
    # Estrategia con umbral de 0.0 a 50.0
    strategy = Threshold_Anomaly_Strategy(min_threshold=0.0, max_threshold=50.0)

    # Caso Normal: 30.0 °C
    normal_reading = ReadingCreate(
        sensor_id="sensor-01",
        value=30.0,
        unit="celsius",
        timestamp=datetime.now(timezone.utc),
    )
    is_anomaly, reason = strategy.evaluate(normal_reading)
    assert is_anomaly is False
    assert reason is None

    # Caso Anómalo: 75.0 °C (Pydantic lo permite por ser <= 80.0, pero supera el umbral 50.0)
    high_reading = ReadingCreate(
        sensor_id="sensor-01",
        value=75.0,
        unit="celsius",
        timestamp=datetime.now(timezone.utc),
    )
    is_anomaly, reason = strategy.evaluate(high_reading)
    assert is_anomaly is True
    assert "excede el limite maximo" in reason


def test_unit_boundary_strategy_evaluation():
    strategy = Unit_Boundary_Strategy()

    # Evaluamos un valor dentro de los límites de Pydantic (0.0 a 100.0)
    normal_percentage = ReadingCreate(
        sensor_id="sensor-02",
        value=50.0,
        unit="percent",
        timestamp=datetime.now(timezone.utc),
    )
    is_anomaly, reason = strategy.evaluate(normal_percentage)
    assert is_anomaly is False


def test_alert_service_process_reading():
    strategy = Threshold_Anomaly_Strategy(min_threshold=0.0, max_threshold=40.0)
    service = AlertService(strategy=strategy)

    reading = ReadingCreate(
        sensor_id="sensor-03",
        value=50.0,
        unit="celsius",
        timestamp=datetime.now(timezone.utc),
    )

    result = service.process_reading(reading)
    assert result["sensor_id"] == "sensor-03"
    assert result["value"] == 50.0
    assert result["is_anomaly"] is True
    assert result["alert_triggered"] is True


def test_create_reading_endpoint_with_anomaly_detection():
    # 70.0 °C es aceptado por el Schema de FastAPI (retorna 200 en lugar de 422)
    payload = {
        "sensor_id": "sensor-test-01",
        "value": 70.0,
        "unit": "celsius",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    response = client.post("/readings", json=payload)
    assert response.status_code == 200 or response.status_code == 201