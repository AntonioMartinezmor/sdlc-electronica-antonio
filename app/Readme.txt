SE AGREGA TEXTO PARA PODERAGREGAR LA COMPARATIVA
# SensorHub

API REST para gestión de sensores y lecturas IoT, construida con FastAPI y SQLAlchemy 2.x.

## Estructura
- Arquitectura en 4 capas: routers → services → repositories → models
- CRUD completo de `sensores` y `lecturas`
- Validación de datos con Pydantic (unidades y rangos por tipo de sensor)
- Paginación y filtro por fecha en `/readings`

## Levantar el proyecto
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Documentación interactiva disponible en `/docs`.