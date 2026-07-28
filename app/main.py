from fastapi import FastAPI
from app.routers import health

app = FastAPI(title="SensorHub")

app.include_router(health.router)
