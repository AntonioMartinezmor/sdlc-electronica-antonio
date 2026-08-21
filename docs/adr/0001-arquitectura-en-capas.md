# Construccion del API en capas

# Estado: Aceptado 

## Contexto: En la situacion actual en la que se encuentra el proyecto dota la estructura de sistema con la ficilidad de ubicar problemas objetivos en las clases sin inferir en las demas aunque dependa una de otra. Esto tecnicamente describe los pricipios de programacion aprendidos en las primera semanas, principios SOLID.    

## Decisión: Se decidio separar el sistema para ser adapaptado a la estructura en capas teniendo como principales las siguientes: 

* Models: Esta parte se encarga de mapear objetos python tipicamente; es la encargada de trabajar con la BD desde columnas y filas hasta relaciones, no tiene nada que ver con http.
* Repositories: Encargado de encapsular las consultas a la BD; se encarga de abstraer los datos en cuanto a guardado y lectura impidiendo que otras instancias de la app se enteren del uso de la BD.
* Routers: Es el traductor por naturaleza de la app; se encarga de interpretar lo que en http este las llamadas del sistema.
* Schemas: Se encarga del formato de los datos de entrada y de salida; se encarga de separar el modelo de dominio y de transporte; no tiene nada que ver directamente con la BD.     
* Services: Es la parte encargada de la logica de la app; es donde se inyectan dependencias y es el punto clave del testeo de la app. 

## Consecuencias Positivas: Doto el sistema de mas profesionalismo, ademas de que facilito varios testeos del sistema con el encapsulamiento de los procesos que en la app se llevan, al trabajar en capas. 

## Consecuencias Negativas / Desafíos: En ocasiones el tener dividido todo provoca que al haber un problema haya que checar diferentes instancias de haber problemas, de no saber leer los errores deriva en mayores problemas.  