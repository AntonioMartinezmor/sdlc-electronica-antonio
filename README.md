# SensorHub 

![CI](https://github.com/AntonioMartinezmor/sdlc-electronica-antonio/actions/workflows/ci.yml/badge.svg)

Gestion de sensores y Lectura IoT por medio de API REST construida con FastAPI, SQLAlchemy 2 y PostgreSQL.

#Comprobacion de despliegue

-API: https://sensorhub-api-1ufb.onrender.com

-API DOCS: https://sensorhub-api-1ufb.onrender.com/docs

-API HEALTH: https://sensorhub-api-1ufb.onrender.com/health

## Estructura
-El API esta construida en una estructura de 4 capas: routers → services → repositories → models

-Para la gestion de datos la API  implementa CRUD.

-Para la validacion de datos se utiliza Pydantic( por unidades y por rangos).

-Cuenta con paginacion y filtrado. 

## Para uso local

### En terminal : Con docker

docker compose up --build

### En terminal : Sin docker

pip install -r requirements.txt

uvicorn app.main:app --reload

