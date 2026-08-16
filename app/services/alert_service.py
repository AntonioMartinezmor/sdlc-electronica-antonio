import logging 
from typing import Optional 
from app.schemas.reading import ReadingCreate
from app.services.anomaly_strategies import Anomaly_Detection_Strategy, Unit_Boundary_Strategy

logger = logging.getLogger("SensorHubAlerts")


class AlertService: 
    def __init__(self, strategy: Optional[Anomaly_Detection_Strategy]= None):
        self.strategy = strategy or Unit_Boundary_Strategy()

    def process_reading(self, reading: ReadingCreate) -> dict: 

        is_anomaly, reason = self.strategy.evaluate(reading)

        result={
            "sensor_id": reading.sensor_id,
            "value": reading.value,
            "is_anomaly": is_anomaly,
            "alert_triggered": False,
            "reason": reason
        }
        if is_anomaly:
            result["alert_triggered"]=True
            logger.warning(
                f"Alerta de anomalia | Sensor: {reading.sensor_id} | "
                f"valor: {reading.value} | Razon: {reason}"

 
            )
            return result