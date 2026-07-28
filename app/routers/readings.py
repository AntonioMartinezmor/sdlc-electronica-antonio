from fastapi import APIRouter
from app.schemas.reading import ReadingCreate

router= APIRouter()

@router.post("/readings")
def create_reading(reading: ReadingCreate): 
    return{"received": reading}
