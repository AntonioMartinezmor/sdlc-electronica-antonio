from fastapi import FastAPI
from app.routers import health , readings

app = FastAPI(title="SensorHub")

app.include_router(health.router)
app.include_router(readings.router)