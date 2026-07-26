Estos son los principios que debo cuidar. 
Como [rol del usuario, ej. Operador de bodega]
Quiero [funcionalidad que necesita, ej. recibir una alerta cuando la temperatura supere los 35 °C]
Para [beneficio o meta, ej. evitar que la mercancía se eche a perder].
Dado que (Given): El contexto inicial o condición previa.
Cuando (When): La acción que realiza el usuario o el sistema.
Entonces (Then): El resultado esperado.
1 o 2: Tarea muy sencilla (ej. definir una clase simple).
3 o 5: Tarea de complejidad media (ej. lógica de alertas o guardar en archivo).
8 o 13: Tarea muy compleja (si mide 8 o más, se recomienda dividirla en dos más pequeñas).
Must have, Should have, Could have, Won't have
eres el único desarrollador de un sistema de monitoreo IoT para una bodega industrial: 10 sensores de temperatura y humedad cada 30 segundos, detección de anomalías (T > 35 °C o H > 80%) y alertas.
------------------------------------------------------------------------------------------------------
story 1: 
Como operador de la bodega, quiero que el sistema valide que los datos capturados de temperatura y humedad estén dentro de rangos físicamente posibles, para evitar falsas alarmas provocadas por errores o descalibración en los sensores.

Escenario: Lectura fuera de rango físico por fallo de sensor.
Dado que el sensor de temperatura genera una lectura anómala de -50 °C o 100 °C cuando el sistema procesa la lectura de la clase SensorReading entonces la lectura debe ser marcada como inválida (error de calibración/sensor) y no debe registrarse como un dato válido para el monitoreo.


Estimación y Prioridad: 3 pts | should have

----------------------------------------------------------------------------------------------------------------

story 2: 
Como usuario del sistema, quiero que la salida de la consola presente la información formateada y limpia en lugar de texto plano desordenado, para facilitar la lectura rápida del estado de la bodega durante el monitoreo.

Escenario: Visualización limpia de datos en pantalla.
Dado que el sistema recibe un evento de lectura normal o de alerta cuando la clase AlertManager imprime la salida en la consola entonces los datos de temperatura y humedad deben incluir unidades claros (°C y %)
Y la marca de tiempo (timestamp) debe tener un formato legible.

Estimación y Prioridad: 1 pts | Could have

*En la auditoria realizada por parte de la IA se recomendo de no ser aplicada para e sprint darle un Won't have

----------------------------------------------------------------------------------------------------------------

story 3: 
Como operador de la bodega, quiero monitorear de forma continua las lecturas periódicas de los 10 sensores de la bodega,para garantizar la recolección constante de datos y detectar cualquier anomalía a tiempo.

Escenario: Lectura periódica de sensores
Dado que los 10 sensores están activos en la bodega cuando transcurre el intervalo de tiempo configurado de 30 segundos entonces la clase SensorReading debe capturar los valores de temperatura y humedad y debe ponerlos a disposición del detector de anomalías.

Estimación y Prioridad: 3 pts | Must have

----------------------------------------------------------------------------------------------------------------

story 4: 
Como operador de la bodega quiero tener una bitacora de las anomalias presentes en los datos recabados, para tener un mapeo claro de las areas a trabajar. 

Escenario: Agrupación de anomalías por área
Dado que la clase AnomalyDetector identifica lecturas fuera de rango cuando se registra una anomalía en un sensor específico entonces la clase AlertManager debe almacenar el evento en la bitácora con la ubicación del sensor y clasificarlo para el historial de mantenimiento por área.

Estimación y Prioridad: 2 pts | Should have

---------------------------------------------------------------------------------------------------------------

story 5: 
Como operador de la bodega, quiero saber cuando el sistema no recibe los datos en tiempo, para tener unindicio en futuros diagnosticos de mantenimiento.

Escenario: Detección de pérdida de datos o emision incompleta
Dado que un sensor debe enviar datos cada 30 segundos cuando el centro de monitoreo no recibe la lectura en el tiempo esperado entonces el sistema debe registrar una alerta de "Pérdida de señal" y marcar la transmisión como incompleta en el historial de mantenimiento.

Estimación y Prioridad: 2 pts | Should have

----------------------------------------------------------------------------------------------------------------

story 6:
Como operador de la bodega, quiero que el sistema active automáticamente la ventilación o climatización al detectar anomalías, para mantener las condiciones óptimas sin depender de intervención manual inmediata.

Escenario: Regulación automática por anomalía de temperatura
Dado que el AnomalyDetector registra una temperatura superior a 35 °C cuando el sistema procesa la alerta de anomalía entonces debe enviar una señal para activar el sistema de enfriamiento de la bodega y registrar el evento de regulación automática.

Estimación y Prioridad: 5 pts | Could have

*Despues de ser auditado este story, la IA lo ubico en Won't have debido a la implementacion de hardware real.

--------------------------------------------------------------------------------------------------------------

story 7:
Como usuario, quiero recibir alertas cuando se regule la calefacion o climatizacion en la bodega para estar enterado del cambio y confirmar que la acción fue correcta. 

Escenario: Emisión de alerta por cambio de climatización
Dado que el sistema ha activado la regulación automática de la bodega cuando se efectúa el cambio en la climatización entonces la clase AlertManager debe emitir una notificación al usuario y solicitar una confirmación manual de la acción realizada.

Estimación y Prioridad: 3 pts | Could have / Won't have

----------------------------------------------------------------------------------------------------------------

story 8:
Como operador de la bodega, quiero que el sistema valide la coherencia de datos entre sensores cercanos, para detectar lecturas erróneas por descalibración y entregar información cercana a la realidad.

Escenario: Discrepancia entre sensores próximos 
Dado que dos sensores están instalados en la misma área de la bodega cuando las lecturas registradas entre ambos difieren significativamente entonces el sistema debe clasificar la discrepancia como una posible anomalía y emitir un aviso de revisión de sensor. 

Estimación y Prioridad: 3 pts | Should have

----------------------------------------------------------------------------------------------------------------

story 9:
Como operador de la bodega, quiero que el sistema ejecute un análisis de funcionalidad al arrancar, para verificar la integridad de los sensores y la comunicación antes de operar de forma autónoma.

Escenario: Verificación de integridad al iniciar el sistema
Dado que el sistema se enciende tras un reinicio o corte de energía cuando se ejecuta la función de autodiagnóstico inicial entonces el sistema debe revisar el estado de los sensores y el enlace de comunicación
y mostrar en consola el mensaje de que el análisis se completó correctamente.

Estimación y Prioridad: 2 pts | Could have

----------------------------------------------------------------------------------------------------------------
story 10: 
Como usuario del sistema, quiero modificar manualmente los límites de temperatura y humedad, para adaptar las condiciones de monitoreo según el tipo de producto almacenado.

Escenario: Actualización manual de umbrales para nuevos materiales 
Dado que se ingresa un producto con requerimientos diferentes como madera cuando el usuario actualiza los valores límite de temperatura y humedad en la configuración entonces el sistema debe aplicar los nuevos umbrales para la detección de anomalías y ajustar la emisión de alertas a estos nuevos parámetros.

Estimación y Prioridad: 2 pts | Should have