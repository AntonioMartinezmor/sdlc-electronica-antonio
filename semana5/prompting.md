#Buena practica de prompting

#Prompt vago(mala practica)1

Quiero que me ayudes a dividir el creado de la tabla para la base de datos de los repositorios.

#Respuesta obtenida
Para separar adecuadamente la **creación/definición de las tablas** (la estructura de la base de datos) de los **repositorios** (la lógica de acceso a datos), la mejor práctica en aplicaciones con FastAPI y SQLAlchemy es seguir un patrón de arquitectura limpia dividiendo el código en **Modelos (`models`)**, **Esquemas (`schemas`)** y **Repositorios (`repositories`)**.

A continuación tienes la estructura recomendada y el código refactorizado.

---

### 1. Definición de la Tabla (Modelo SQLAlchemy)

Crea o revisa tu archivo `app/models/reading.py`. Aquí se define **únicamente** la estructura de la tabla de la base de datos (columnas, tipos de datos y llaves).

```python
# app/models/reading.py
from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime
from app.db.base import Base  # Tu DeclarativeBase de SQLAlchemy

class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, nullable=False, index=True)
    value = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
```

---

### Observaciones y Mejoras Aplicadas (Principios SOLID) 

1. **Responsabilidad Única (SRP):**
* **`app/models/`**: Solo define cómo luce la tabla en la base de datos.
* **`app/schemas/`**: Solo define la validación de entrada/salida de la API.
* **`app/repositories/`**: Solo se encarga de ejecutar operaciones SQL mediante SQLAlchemy.


2. **Inversión de Dependencias (DIP):**
* El repositorio recibe la instancia `db: Session` a través de su constructor (`__init__`), permitiendo inyectar dependencias fácilmente en pruebas unitarias o en los endpoints.


3. **Mejora en `update`:**
* Se utilizó `ReadingUpdate` con `exclude_unset=True` en lugar de sobrescribir campos manualmente. Esto permite realizar actualizaciones parciales de manera limpia y flexible.
---
-------------------------------------------------------------------------------------------

###Prompt bien estructurado(buena practica)1
En los codigos que te comparto se combina en una sola clase la interfaz y la implementación con SQLAlchemy. Quiero aplicar el Principio de Inversión de Dependencias (DIP) de forma más estricta, separando en dos archivos: una interfaz usando typing.Protocol (sin implementación), y una clase concreta SQLAlchemyReadingRepository que la implemente. No se requiere ninguna librería nueva, Protocol es parte de la librería estándar. Antes de darme el código, explícame cómo funciona Protocol en Python y por qué esta separación fortalece DIP en mi proyecto. 

#Respuesta Obtenida

En Python, **`typing.Protocol`** permite implementar lo que se conoce como **tipado pato estructural** (*structural duck typing*).

A diferencia de las clases base abstractas tradicionales (`abc.ABC`), donde una clase debe heredar explícitamente de la interfaz (herencia nominal), con `Protocol` una clase satisface la interfaz simplemente **implementando los mismos métodos y variables con los mismos tipos**, sin necesidad de heredar explícitamente de ella.

* **Sin implementación:** Los métodos dentro del `Protocol` solo definen la firma (parámetros y tipo de retorno) y llevan `...` (pass/ellipsis) en su cuerpo.
* **Verificación estática:** Herramientas como `mypy` o el linter de tu IDE verifiquen en tiempo de desarrollo que la clase concreta implemente todos los métodos requeridos por el `Protocol`. Si a tu clase concreta le falta un método o firma, el linter lanzará un error de tipado.
...

---

### ¿Por qué esta separación fortalece el Principio de Inversión de Dependencias (DIP)?

El Principio de Inversión de Dependencias (el último principio de SOLID) establece dos reglas principales:

1. **Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.**
2. **Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones.**

#### 1. Desacoplamiento de la base de datos

En tu código actual, tu capa de negocio/servicios depende directamente de SQLAlchemy (que es un detalle de infraestructura de bajo nivel). Si el día de mañana decides cambiar SQLAlchemy por otro ORM (como Tortoise ORM), o usar una base de datos NoSQL (MongoDB), o hacer mocks en pruebas unitarias, tendrías que modificar la lógica existente.

Con `Protocol`, tu capa de servicios o controladores dependerá de la abstracción `ReadingRepositoryProtocol`. No le importará *cómo* se guardan los datos, solo que exista un objeto capaz de responder a `.create()`, `.get_all()`, etc.

#### 2. Facilidad para Pruebas Unitarias (Testing)

Al depender de un `Protocol`, puedes crear un `MemoryReadingRepository` (un repositorio en memoria usando listas o diccionarios) sin levantar una base de datos ni configurar SQLAlchemy para probar tu lógica de negocio de manera ultrarrápida.

---

### Propuesta de Estructura de Archivos

Separaremos tu código en dos componentes limpios:

1. `app/repositories/reading_protocol.py`: Contiene únicamente la interfaz (el contrato).
2. `app/repositories/sqlalchemy_reading_repository.py`: Contiene la implementación concreta basada en SQLAlchemy.

---

#### Archivo 1: Interfaz / Contrato (`app/repositories/reading_protocol.py`)

```python
from datetime import datetime
from typing import Optional, Protocol
from app.models.reading import Reading
from app.schemas.reading import ReadingCreate


class ReadingRepositoryProtocol(Protocol):
    """
    Interfaz que define las operaciones permitidas sobre el repositorio de Reading.
    Aplica DIP al desacoplar la lógica de negocio del ORM específico.
    """

    def create(self, reading: Reading) -> Reading:
        ...

    def get_all(
        self,
        limit: int = 10,
        offset: int = 0,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> list[Reading]:
        ...

    def get_by_id(self, reading_id: int) -> Optional[Reading]:
        ...

    def update(self, reading: Reading, data: ReadingCreate) -> Reading:
        ...

    def delete(self, reading: Reading) -> None:
        ...

```

---

#### Archivo 2: Implementación Concreta (`app/repositories/sqlalchemy_reading_repository.py`)

```python
from datetime import datetime
from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.reading import Reading
from app.schemas.reading import ReadingCreate


class SQLAlchemyReadingRepository:
    """
    Implementación concreta del repositorio usando SQLAlchemy.
    Satisface ReadingRepositoryProtocol mediante tipado estructural.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(self, reading: Reading) -> Reading:
    ...

```

---
-------------------------------------------------------------------------------------------

###Comparativa

Viendo ambas respuestas encuetro que lo que puede ofrecer la respuesta vaga es mas que ineficiente en cuanto a los cambios que aplica al codigo proporcionado; en esencia podemos decir que es por que no se le ofrece ningun tipo de instruccion precisa, esto hablando de que sedeshace de distintas partes del codigo violando por completo la estructura presente lo que produce aun mas problemas de los que ya se tenia en el codigo por modificar. Algo a destacar de esta primera prueba fue que creo distintas rutas de las que pretendia obtener paquetes de fuciones las cuales no existian en mi proyecto; ademas desactualizo algunos metodos y funciones aplicadas en la construccion del repositorio atacando la estrctura solicitada en semanas pasadas. 

Ahora bien el segundo prompt aporta precision y mas que nada contexto de lo que estamos haciendo lo que propicia que la respuesta del asistente de IA sea mas objetiva y practica; aunque, para este caso mi prompt se volvio a quedar corto ya que no especifique que se mantubiera el nombre o sintaxis de las clases para evitar problemas con las demas estructuras del API. Sin embargo fue capaz de separarar sin mayor problema la interfaz de la creacion de la base de datos.

---------------------------------------------------------------------------------------------------------------

###Prompt vago(mala practica)2 
Anaiza los dos codigos que te comparto y arreglalos para que no sean repetitivos. 

Respuesta obtenida
```
---
**Problemas identificados en el código actual:**

1. **Duplicación de `get_db**`: Definiste la misma función generadora de sesión de base de datos en ambos archivos/bloques.
2. **Duplicación de instanciación**: En cada endpoint creas manualmente el repositorio y el servicio (`repository = ...`, `service = ...`), lo cual genera código repetitivo (*boilerplate*).
3. **Uso de `SensorCreate` para `PUT**`: Al actualizar (`PUT`), es preferible usar un esquema de actualización (`SensorUpdate` / `ReadingUpdate`) con campos opcionales en lugar del esquema de creación estricto.

---

### Solución Refactorizada

Para aplicar los principios **DRY (Don't Repeat Yourself)** y **SOLID**, extraemos la gestión de dependencias y dividimos la lógica en módulos limpios.

#### 1. Archivo Compartido de Dependencias (`app/api/deps.py`)

Mueve la función `get_db` y crea funciones fábrica para inyectar los servicios directamente en las rutas:

...

#### 2. Router de Sensores (`app/api/routers/sensors.py`)

```python
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.sensor import SensorCreate  # O SensorUpdate para el PUT
from app.services.sensor_service import SensorService
from app.api.deps import get_sensor_service

router = APIRouter(prefix="/sensors", tags=["Sensors"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_sensor(
    sensor: SensorCreate, 
    service: SensorService = Depends(get_sensor_service)
):
    return service.create_sensor(sensor)

@router.get("/")
def list_sensors(
    limit: int = 10, 
    offset: int = 0,
)
    ...
#### 3. Router de Lecturas (`app/api/routers/readings.py`)

```python
from datetime import datetime
from typing import Optional 
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.reading import ReadingCreate
from app.services.reading_service import ReadingService
from app.api.deps import get_reading_service

router = APIRouter(prefix="/readings", tags=["Readings"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_reading(
    reading: ReadingCreate, 
    service: ReadingService = Depends(get_reading_service)
):
    return service.create_reading(reading)

@router.get("/")
def list_readings(
    limit: int = 10,
    offset: int = 0,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    service: ReadingService = Depends(get_reading_service)
):
    return service.get_readings(limit, offset, start_date, end_date)

@router.get("/{reading_id}")
def get_reading(
    reading_id: int, 
    service: ReadingService = Depends(get_reading_service)
):
...
### Principales mejoras aplicadas:

* **Inyección de Dependencias Limpia**: Usar `Depends(get_sensor_service)` elimina la instanciación manual dentro de cada controlador.
* **Prefijos de Ruta (`prefix`)**: Se definió `prefix="/sensors"` y `prefix="/readings"` al instanciar `APIRouter()`, simplificando los decoradores (`@router.get("/")` en lugar de `@router.get("/sensors")`).
* **Códigos HTTP Correctos**: Adición de `status_code=201` (`HTTP_201_CREATED`) para las peticiones `POST`.
* **Centralización de `get_db**`: Se evita duplicar la conexión a la base de datos entre distintos archivos.






------------------------------------------------------------------------------------------
````
---
###Prompt bien estructurado(buena practica)2
Te comparto dos codigos que forman parte de los routers de un api que estoy construyendo, al ser ambos routers comparten algunas funciones que bien podrian estrar por separado, quiero que identifiques en que partes se vuelven repetitivos y si esas partes pueden volverse parte general de todos los routers para poder separarlos en un archivo distinto. No modifiques ninguna instancia ni libreria, cuida los nombres y como se referencian las dinstitas funciones que en el estan para evitar problemas con las demas partes del api; quiero que me sugieras cambios y me expliques el por que y en que me beneficiaria. 

Respuesta obtenida
```
---
Los dos routers presentan **duplicación de código** y **violaciones al principio DRY (*Don't Repeat Yourself*)**. Al centralizar y desacoplar estas responsabilidades comunes, simplificarás el mantenimiento y la escalabilidad del proyecto.

---

### 1. Puntos de Repetición Identificados

1. **La función `get_db()**`: Ambas implementaciones definen la misma dependencia para administrar la sesión de SQLAlchemy.
2. **Instanciación repetitiva de Repositorios y Servicios**: En cada endpoint reinstancias manualmente la capa de repositorio y servicio (`repository = ...`, `service = ...`), lo cual satura la lógica de las rutas y dificulta las pruebas unitarias (mocking).
3. **Manejo repetitivo de errores HTTP 404**: Todos los endpoints `GET /{id}`, `PUT /{id}` y `DELETE /{id}` repiten el chequeo `if result is None: raise HTTPException(status_code=404, ...)` o `if not success: ...`.

---

### 2. Propuestas de Refactorización y Separación

#### A. Centralizar la Dependencia de Base de Datos (`get_db`)

Mueve la función `get_db` a un archivo dedicado, como `app/db.py` o `app/dependencies.py`.

* **¿Por qué?**: Evita redefinir la conexión en cada router y centraliza la gestión de sesiones.
* **Beneficio**: Si en el futuro cambias el manejo de la base de datos (por ejemplo, transacciones asíncronas), solo modificarás ese archivo.

**`app/dependencies.py`**

```python
from app.db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```
#### B. Inyección de Dependencias para Servicios

En lugar de instanciar `SensorRepository` / `SensorService` manualmente dentro de cada endpoint, puedes definir funciones de fábrica (*factory functions*) utilizando `Depends` de FastAPI.

* **¿Por qué?**: FastAPI resuelve el árbol de dependencias automáticamente. El endpoint solo recibe la instancia del servicio lista para usarse.
* **Beneficio**:
* Código en los endpoints 60% más limpio.
* Facilita enormemente las pruebas unitarias (puedes reemplazar `get_sensor_service` por un servicio *mock* sin tocar la lógica de la ruta).



**`app/dependencies.py`** (agregando las fábricas):

```
---
#### B. Inyección de Dependencias para Servicios

En lugar de instanciar `SensorRepository` / `SensorService` manualmente dentro de cada endpoint, puedes definir funciones de fábrica (*factory functions*) utilizando `Depends` de FastAPI.

* **¿Por qué?**: FastAPI resuelve el árbol de dependencias automáticamente. El endpoint solo recibe la instancia del servicio lista para usarse.
* **Beneficio**:
* Código en los endpoints 60% más limpio.
* Facilita enormemente las pruebas unitarias (puedes reemplazar `get_sensor_service` por un servicio *mock* sin tocar la lógica de la ruta).



**`app/dependencies.py`** (agregando las fábricas):

```python



------------------------------------------------------------------------------------------




```
---

------------------------------------------------------------------------------------------
Comparativa
Para esta egunda ocasion podemos observar que el prompt vago llevo al asistente a crear instancias y carpetas fantasmas de las que tomaba elementos inexistentes en el proyecto lo que provocaria problemas al instante de correrlo; por otra parte el segundo prompt en el que se le dieron instrucciones un poco mas precisas ( basandonos en la experiencia del anterior prompt) hicimos algunos cambios en la estructura que permitieron obtener un resultado favorable pero sin ser perfecto aun, ya que aun habiendo restricciones de cambios permitidos el asistente efectuo algunos cambios menores de sintaxis que aunque entregan el mismo resultado sigue habiendo una omision por parte del asistente.  
------------------------------------------------------------------------------------------
###Prompt vago(mala practica)3
Desarrolla una interfaz de mi api para un patron de AlertStrategy

Respuesta obtenida

```
---
Esta es una implementación orientada a Clean Architecture / REST API usando **FastAPI** para exponer la lógica de tu `AlertStrategy`.

Permite recibir lecturas de sensores mediante un endpoint HTTP, seleccionar la estrategia de alerta activa dinámicamente y registrar/notificar anomalías.

```python
from enum import Enum
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# Imports de tu modelo existente
from abc import ABC, abstractmethod
from ps.src.sensor import SensorReading


# ------------------------------------------------------------------
# 1. MODELOS DE DATOS (DTOs / Pydantic)
# ------------------------------------------------------------------

class AlertStrategyType(str, Enum):
    CONSOLE = "console"
    FILE = "file"

class SensorReadingDTO(BaseModel):
    sensor_id: str = Field(..., example="SENSOR-001")
    temperature: float = Field(..., example=36.5)
    humidity: float = Field(..., example=85.0)

class AlertRequest(BaseModel):
    reading: SensorReadingDTO
    message: str = Field(default="Anomalía detectada en los parámetros del sensor.")
    strategy_type: AlertStrategyType = Field(default=AlertStrategyType.CONSOLE)

class AlertConfigDTO(BaseModel):
    max_temp: float = 35.0
    max_humidity: float = 80.0


# ------------------------------------------------------------------
# 2. FACTORY Y SERVICIO CON TU LÓGICA DE NEGOCIO
# ------------------------------------------------------------------

class AlertStrategyFactory:
    """Fabrica la estrategia elegida por el cliente o configuración."""
    @staticmethod
    def get_strategy(strategy_type: AlertStrategyType, file_path: str = "bitacora_alerts.log") -> AlertStrategy:
        if strategy_type == AlertStrategyType.CONSOLE:
            return ConsoleAlertStrategy()
        elif strategy_type == AlertStrategyType.FILE:
            return FileAlertStrategy(file_path=file_path)
        raise ValueError("Estrategia no válida")

class SensorAlertService:
    """Coordinador entre el Detector de Anomalías y el AlertManager."""
    def __init__(self, detector: AnomalyDetector):
        self.detector = detector

    def process_reading(self, reading: SensorReading, strategy_type: AlertStrategyType, custom_message: str):
        is_anomaly = self.detector.is_anomaly(reading)
        
        if is_anomaly:
            # Instanciamos la estrategia requerida usando el patrón Factory
            strategy = AlertStrategyFactory.get_strategy(strategy_type)
            manager = AlertManager(strategy)
            manager.notify(reading, custom_message)
            return True, "Alerta emitida correctamente por anomalía."
        
        return False, "Lectura dentro de rangos normales. No se generó alerta."


# ------------------------------------------------------------------
# 3. INTERFAZ DE LA API (FastAPI)
# ------------------------------------------------------------------

app = FastAPI(
    title="Sensor Alert System API",
    version="1.0.0",
    description="API REST para procesamiento de lecturas de sensores y estrategia de alertas."
)

# Instancia global del detector (en producción se manejaría mediante Inyección de Dependencias)
detector_global = AnomalyDetector(max_temp=35.0, max_humidity=80.0)
service = SensorAlertService(detector_global)


@app.post(
    "/api/v1/readings/process",
    status_code=status.HTTP_200_OK,
    summary="Procesar lectura de sensor",
    tags=["Alerts"]
)
def process_sensor_reading(payload: AlertRequest):
    """
    Recibe la lectura de un sensor, valida si es una anomalía y
    ejecuta la estrategia de alerta seleccionada (`console` o `file`).
    """
    # Mapper de DTO Pydantic a entidad SensorReading
    sensor_reading = SensorReading(
        sensor_id=payload.reading.sensor_id,
        temperature=payload.reading.temperature,
        humidity=payload.reading.humidity
    )

    alert_triggered, detail_message = service.process_reading(
        reading=sensor_reading,
        strategy_type=payload.strategy_type,
        custom_message=payload.message
    )

    return {
        "status": "success",
        "anomaly_detected": alert_triggered,
        "strategy_used": payload.strategy_type,
        "detail": detail_message
    }


@app.put(
    "/api/v1/config/thresholds",
    status_code=status.HTTP_200_OK,
    summary="Actualizar umbrales de anomalía",
    tags=["Config"]
)
def update_thresholds(config: AlertConfigDTO):
    """Actualiza los umbrales máximos de temperatura y humedad en tiempo de ejecución."""
    detector_global.max_temp = config.max_temp
    detector_global.max_humidity = config.max_humidity
    return {
        "status": "updated",
        "new_max_temp": detector_global.max_temp,
        "new_max_humidity": detector_global.max_humidity
    }

```

---

**Ejemplo de Request HTTP (POST `/api/v1/readings/process`):**

```json
{
  "reading": {
    "sensor_id": "SENSOR-SALA-01",
    "temperature": 38.2,
    "humidity": 82.5
  },
  "message": "Superó la temperatura crítica de operación",
  "strategy_type": "file"
}

```

------------------------------------------------------------------------------------------
```
---
###Prompt bien estructurado(buena practica)2
Te comparto el patron de AlertStrategy que desarrolle como parte de un sitema IoT, este  patron lo desarrolle antes de crear mi API por lo que ahora necesito implementarlo como una interfaz intercanbiable o protocolo dentro de la misma API utilizando typing.Protocol igual te comparto mi reading_repository.py como guia de implementacion del patron de AlertStrategy buscando que se pueda conectar al flujo de detección de anomalías de mi servicio de lecturas, Por ultimo te comparto también mi requirements.txt actual, para que no propongas librerías nuevas sin necesidad. Antes del código, explícame cómo encajaría esta interfaz con mi arquitectura de capas existente.

Respuesta Obtenida:

```
---

```
---
Para integrar tu patrón **Strategy** en la arquitectura actual usando `typing.Protocol`, no necesitas agregar librerías externas; aprovecharemos **Python nativo** y las capacidades de **FastAPI** para la inyección de dependencias.

---

### Integración en tu Arquitectura de Capas

En una arquitectura por capas típica para APIs (como la que estás estructurando con Repositorios y Servicios), la responsabilidad se divide de la siguiente manera:

* **Capa de Interfaces/Protocolos (`app/interfaces/alert.py`)**: Aquí vive `AlertStrategy` definido como `Protocol`. Esto permite **tipado estático** con `mypy` y **acoplamiento débil** (*Duck Typing* estructural). Cualquier clase que implemente el método `send_alert` será una estrategia válida sin necesidad de heredar explícitamente de una clase base.
* **Capa de Infraestructura (`app/services/alerts.py`)**: Implementa las estrategias concretas (`ConsoleAlertStrategy`, `FileAlertStrategy`, etc.).
* **Capa de Dominio/Servicio (`app/services/reading_service.py`)**: Es la capa intermedia entre tus endpoints de FastAPI y el `ReadingRepository`. El servicio se encarga de:
1. Recibir los datos de la nueva lectura.
2. Guardar la lectura usando `ReadingRepository`.
3. Evaluar si hay una anomalía con `AnomalyDetector`.
4. Si existe una anomalía, invocar el `AlertStrategy` inyectado para emitir la alerta.



```
       [ FastAPI Endpoint ]
                │
                ▼
      [ ReadingService ] ──(Evalúa)──► [ AnomalyDetector ]
        │            │
   (Persiste)    (Notifica)
        │            │
        ▼            ▼
[ Repository ]  [ AlertStrategy (Protocol) ]
                     ├── ConsoleAlertStrategy
                     └── FileAlertStrategy

```

---

### Código de Implementación

#### 1. Definición del Protocolo y Estrategias Concrete

Uso de `typing.Protocol` según tus dependencias actuales:

```python
# app/interfaces/alert.py
from typing import Protocol


# Adaptamos el protocolo para recibir objetos del modelo o schemas de la API
class AlertStrategy(Protocol):

    def send_alert(self, sensor_id: str, message: str, value: float) -> None:
        ...


# app/services/alerts.py
class ConsoleAlertStrategy:

    def send_alert(self, sensor_id: str, message: str, value: float) -> None:
        print(
            f"[ALERTA CONSOLA] Sensor: {sensor_id} | Mensaje: {message} | Valor: {value}"
        )


class FileAlertStrategy:

    def __init__(self, file_path: str = "bitacora_alerts.log") -> None:
        self.file_path = file_path

    def send_alert(self, sensor_id: str, message: str, value: float) -> None:
        log_entry = f"[BITACORA] Sensor: {sensor_id} - {message} - Valor: {value}\n"
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(log_entry)

```

---

#### 2. Detector de Anomalías y Servicio de Lecturas

Conectamos el detector, el repositorio y la estrategia inyectable dentro del servicio de negocio:

```python
# app/services/reading_service.py
from typing import Optional
from app.models.reading import Reading
from app.schemas.reading import ReadingCreate
from app.interfaces.alert import AlertStrategy
from app.repositories.reading_repository import ReadingRepository


class AnomalyDetector:

    def __init__(self, max_value: float = 35.0) -> None:
        self.max_value = max_value

    def is_anomaly(self, value: float) -> bool:
        return value > self.max_value


class ReadingService:

    def __init__(
        self,
        repository: ReadingRepository,
        alert_strategy: AlertStrategy,
        anomaly_detector: Optional[AnomalyDetector] = None,
    ) -> None:
        self.repository = repository
        self.alert_strategy = alert_strategy
        self.anomaly_detector = anomaly_detector or AnomalyDetector()

    def process_and_create_reading(
        self, reading_data: ReadingCreate
    ) -> Reading:
        # 1. Crear la entidad a partir del schema
        reading_entity = Reading(
            sensor_id=reading_data.sensor_id,
            value=reading_data.value,
            unit=reading_data.unit,
        )

        # 2. Persistir en la base de datos a través del repositorio
        saved_reading = self.repository.create(reading_entity)

        # 3. Evaluar anomalías e invocar la estrategia de alerta si aplica
        if self.anomaly_detector.is_anomaly(saved_reading.value):
            self.alert_strategy.send_alert(
                sensor_id=str(saved_reading.sensor_id),
                message="Lectura fuera del rango permitido",
                value=saved_reading.value,
            )

        return saved_reading

```

---

#### 3. Uso en Endpoints de FastAPI

Inyectamos las dependencias dinámicamente en los endpoints:

```python
# app/api/v1/readings.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.reading import ReadingCreate, ReadingResponse
from app.repositories.reading_repository import ReadingRepository
from app.services.alerts import ConsoleAlertStrategy, FileAlertStrategy
from app.services.reading_service import ReadingService

router = APIRouter()


# Función de fábrica para seleccionar la estrategia deseada (consola, archivo, etc.)
def get_alert_strategy():
    return ConsoleAlertStrategy()  # O intercambiar por FileAlertStrategy()


def get_reading_service(
    db: Session = Depends(get_db),
    alert_strategy=Depends(get_alert_strategy),
) -> ReadingService:
    repository = ReadingRepository(db)
    return ReadingService(repository=repository, alert_strategy=alert_strategy)


@router.post("/readings", response_model=ReadingResponse)
def create_reading(
    reading_in: ReadingCreate,
    service: ReadingService = Depends(get_reading_service),
):
    return service.process_and_create_reading(reading_in)

```

------------------------------------------------------------------------------------------

```
---
Comparativa
En este tercer caso se hizo aun mas evidente la problematica a la que se enfrenta el asistente al no contar con contexto suficiente para poder desarrollar su trabajo, es decir al darle una instruccion tan vaga coomo la del ejemplo es que se encuentra con problemas para trabjar de manera adecuada; en el primer caso creo tecnicamente un proyecto nuevo alrededor del codigo que le ofrecimos; por otra parte el prompt bien realizado le dio limitantes y herramientas suficientes en cuanto a contexto para trabajar de manera eficiente pero no perfecta ya que igual que en el anterior caso siguio perdiendose en alguna sintaxis menores; sin embargo en este caso fue mas que evidente la falta de contexto y las consecuencias de no redactar de manera correcta un prompt. 