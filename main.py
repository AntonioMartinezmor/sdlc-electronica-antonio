import time
import random
import json
import paho.mqtt.client as mqtt

# Configuración del servidor de mensajería (Broker)
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "ingenieria/sdlc/sensor_antonio"

print("=== Simulador de Sensor IoT Iniciado ===")
print(f"Conectando al servidor {BROKER}...")

# Configuración del cliente MQTT
client = mqtt.Client()

try:
    client.connect(BROKER, PORT, 60)
    print("¡Conectado exitosamente!")
except Exception as e:
    print(f"Error al conectar: {e}")
    exit(1)

# Bucle infinito para simular el sensor
try:
    while True:
        # Simulamos datos lógicos de temperatura y humedad
        temperatura = round(random.uniform(20.0, 30.0), 2)
        humedad = round(random.uniform(40.0, 60.0), 2)
        
        # Estructuramos el mensaje en formato JSON
        payload = {
            "sensor": "Sensor_Electronica_Antonio",
            "temperatura_C": temperatura,
            "humedad_porcentaje": humedad,
            "estado": "OK"
        }
        
        # Publicamos los datos en el servidor
        client.publish(TOPIC, json.dumps(payload))
        print(f"Datos enviados: {payload}")
        
        # Espera 5 segundos antes de la siguiente lectura
        time.sleep(5)

except KeyboardInterrupt:
    print("\nSimulador detenido por el usuario.")
finally:
    client.disconnect()