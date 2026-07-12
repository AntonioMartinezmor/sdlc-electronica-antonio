# Usamos una imagen oficial de Python ligera
FROM python:3.10-slim

# Creamos una carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos (lo crearemos en el siguiente paso)
COPY requirements.txt .

# Instalamos las librerías necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código del sensor al contenedor
COPY . .

# Comando para ejecutar el script principal cuando el contenedor arranque
CMD ["python", "main.py"]