from pydantic import BaseModel 

class ReadingCreate(BaseModel):
    sensor_id: str 
    value: float 
    unit: str 
