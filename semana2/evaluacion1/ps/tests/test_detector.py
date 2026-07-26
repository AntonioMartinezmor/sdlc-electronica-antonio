import pytest
from ps.src.sensor import SensorReading
from ps.src.detector import AnomalyDetector,  ConsoleAlertStrategy,FileAlertStrategy, AlertManager

@pytest.fixture
def detector_config():
    return{
        "max_temp":35.0,
        "max_humidity":80.0

    }
def test_anomaly_detector_temperature(detector_config):
    detector =AnomalyDetector(**detector_config)
    reading = SensorReading(sensor_id="BODEGA_NORTE_01", temperature= 36.5, humidity=50.0)
    assert detector.is_anomaly(reading) is True

def test_anomaly_detector_normal_reading(detector_config):
    detector = AnomalyDetector(**detector_config)
    reading = SensorReading(sensor_id="BODEGA_NORTE_01", temperature= 20.0, humidity=50.0)
    assert detector.is_anomaly(reading) is False 

def test_alert_manager_console(capsys):
    strategy = ConsoleAlertStrategy()
    manager = AlertManager(strategy=strategy)
    reading = SensorReading(sensor_id="BODEGA_NORTE_01", temperature= 38.0 , humidity= 85.0)
    manager.notify(reading,message="Anomalia detectada")
    captured = capsys.readouterr()
    assert "BODEGA_NORTE_01" in captured.out 
    assert "Anomalia detectada" in captured.out 

def test_alert_manager_file(tmp_path):
    log_file = tmp_path/ "bitacora_alertas.log"
    strategy = FileAlertStrategy(file_path=str(log_file))
    manager = AlertManager(strategy=strategy)
    reading = SensorReading(sensor_id="BODEGA_SUR_02", temperature=40.0, humidity=90.0)
    manager.notify(reading, message="Anomalia de temperatura y humedad")
    assert log_file.exists()
    content = log_file.read_text()
    assert "BODEGA_SUR_02" in content
    assert "Anomalia de temperatura y humedad" in content 
