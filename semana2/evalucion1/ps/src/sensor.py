class SensorReading: 

    def __init__(self, sensor_id:str, temperature: float, humidity:float):
        if not (0.0 <= humidity <=100.0):
            raise ValueError("Humedad fuera de rango (debe de estar dentro de 0% y 100%)")
        if not (-50.0 <= temperature <= 80.0):
            raise ValueError("Temperatura fuera de rango (debe de estarentre -50ºC y 80ºC)")

        self.sensor_id = sensor_id
        self.temperature = temperature
        self.humidity = humidity