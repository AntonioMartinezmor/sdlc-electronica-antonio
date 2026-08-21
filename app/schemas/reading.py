from typing import Literal
from pydantic import BaseModel, Field, model_validator

RANGOS_POR_UNIDAD = {
    "celsius": (-50.0, 80.0),
    "fahrenheit": (-58.0, 176.0),
    "percent": (0.0, 100.0),
}

class ReadingCreate(BaseModel):
    sensor_id: str = Field(..., min_length=1, max_length=64)
    unit: Literal["celsius", "fahrenheit", "percent"]
    value: float = Field(..., allow_inf_nan=False)

    @model_validator(mode="after")
    def valor_dentro_de_rango(self) -> "ReadingCreate":
        minimo, maximo = RANGOS_POR_UNIDAD[self.unit]
        if not (minimo <= self.value <= maximo):
            raise ValueError(
                f"value {self.value} fuera de rango para '{self.unit}' "
                f"(esperando entre {minimo} y {maximo})"
            )
        return self