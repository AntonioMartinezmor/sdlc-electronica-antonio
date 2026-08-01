from pydantic import BaseModel, field_validator, ValidationInfo
#las unidades permitidas se guardan dentro de un {} buscando eficiencia 
UNIDADES_VALIDAS = {"celsius", "fahrenheit","percent"}
#desarrollamos un diccionario con los rangos permitidos por unidad
RANGOS_POR_UNIDAD = {
    "celsius": (-50.0, 80.0),
    "fahrenheit": (-58.0,176.0),
    "percent":(0.0,100.0)

}
#modificamos la clase maestra, dotandola de selectividad, con ayuda de field validator
class ReadingCreate(BaseModel):
    sensor_id: str 
    unit: str 
    value: float 
    

    @field_validator("unit")
    @classmethod
    def unidad_debe_ser_conocida(cls,v:str)->str: #despues de validar unit por medio de 
        #field validator, esta funcion recibe unit en v de no estar en las unidades validas
        # arroja un mensaje, si no, la deja seguir
        if v not in UNIDADES_VALIDAS:
            raise ValueError(f"unidad desconocida: '{v}'. Validas: {UNIDADES_VALIDAS}")
        return v

    @field_validator("value")
    @classmethod
    def valor_dentro_de_rango(cls, v:float, info:ValidationInfo) -> float: 
        #en esta ocasion recibe el value en v, despues de ser validado;
        unit = info.data.get("unit")# toma unit si este fue validado previamente
        if unit in RANGOS_POR_UNIDAD:
            minimo, maximo = RANGOS_POR_UNIDAD[unit]#toma los rangos por unidad si fue validado 
            if not (minimo <= v <= maximo):# comparamos los valores obtenidos
                raise ValueError(
                    f"value {v} fuera de rango para '{unit}' (esperando entre{minimo} y {maximo})"
                )
        return v #retornamos informacion
