from app.models.alert import Alert
def test_alert_CPD():
    alert = Alert(sensor_id="SENSOR_01",message="Valor fuera de rango")
    assert alert.status == "open"
    