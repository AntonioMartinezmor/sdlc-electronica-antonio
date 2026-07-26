-**Sprint 1 Planning**-

--**Sprint Goal:
Diseñar las bases de un sistema IOT con sistema de alertas, deteccion de errores y sobre todo lectura de sensores.

*Para este primer sprint se seleccionaron 5 de las 10 historias que tengo:

-Validacion de datos capturados: Esta es uno de los users story primordilaes en el proyecto ya que sienta las bases para el diseño de las demas funciones, utlizando la recepcion de datos asi como la evaluacion de los mismos siendo una de las partes mas importantes del sistema. 

-Mejorar la visualizacion de informacion: Este story brinda facilidad en la lectura de datos y en momentos de evaluacion de funcionalidad del codigo modificar el orden y manera en la que se muestran los datos juega a favor del analisis de funcionalidad. 

-Monitoreo de lecturas: Se eligio este story por que favorece el mantenimiento del control del sistema brindadonos mas informacion de posibles errores en lecturas o lecturas incompletas por retardos de envio. 

-Monitoreo de anomalias: De la mano del anterior story y por que se cuneta con la estructura, se desarrollo una clase con la capacidad de ubicar anomalias agrupandolas por area para brindar futuro mantenimiento a los sensorespor grupo.

-Seguimiento de transmisiones incompletas: Este story trabaja de la mano con el tercero ya que este seencarga de encontrar el momento en que los datos no se comparte en tiempo, por lo que son tipados dentro del grupo de Perdida de señal, donde seran registrados y evaluados en posibles servicios.

--**Tareas 

User Story 1: Validacion de datos capturados.
T1.1: Diseñar las clases y funciones encargadas de verificar la funcionalidad de los valores leidos por los sensores.

T1.2: Crear las clases y funciones que se encargan de leer los valores entregados por los sensores asi como las encargadas de empaquetarlos para la parte procesadora.

T1.3: Adaptar ambos codigos (el de testeo y lectura de sensores) a los criterios de evaluacion solicitados usando pruebas unitarias en consola con ayuda del siguente comando python -m pytest --cov=ps/src --cov-report=term-missing.

User Story 2: Mejorar la visualizacion de informacion.
T2.1: Construir un codigo que compruebe la funcionalidad de le las clases encargadas de contruir una estructura con los datos recibido por medio del lector de sensores.

T2.2: Diseñar un codigo que construya una estructura clara con los datos recibidos. 

T2.3: Adapatar el codigo a criterios de evalucion.

User Story 3: Monitoreo de lecturas.

T3.1: Desarrollar un codigo capaz de manipular los datos leidos por sensor.py encargado de la revision de lo sensores y emision de los datos; para enviarlo al codigo a testear. 

T3.2: Diseñar un codigo por el que pasen los valores leidos provenientes de los sensores y recibidos por el tester, para mantener monitorizado el tiempo que tardan en ser enviados. 

T3.3:Adaptar a las caracteristicas solicitadas por el usuario asi como a los terminos solicitados para la colocacion en done. 

User Story 4: Monitoreo de anomalias
T4.1 Diseñar un codigo que envie los datos calculados con alguna estructura que ponga a prueba el sistema de filtrado de anomalias, los datos se siguen tomando de la clase lectora de sensores. 

T4.2 Se debe de diseñar un codigo que filtr los datos obtenido y sea capaz de clasificarlos como anomalias de lecturas, con la capacidad de poder ser editado a nivel de los criterios de clasificacion. 

T4.3 Adapatar a criterios de Done

User Story 5: Seguimiento de transmisiones incompletas. 
T5.1 Se debera construir un codigo que envie a despiemto o incompletos los valores obtenidos por el lector de sensores; buscando que se ponga a prueba el funcionamiento del filtrado de los datos incompletos.

T5.2 Se debera elaborar un codigo que busque tipar o agrupar los datos que sean recibidos a destimepos, buscando que sea documentado para futuros servicios al sistema.

T5.3 Se buscara el cumplimiento de los cirterios de evaluacion de codigo.

--**Definicion de criterios DONE 

Los criterios con los que evaluamos los codigo para ser clasificados como done son los siguentes: 

1.- Todo codigo desarrollado para los users storys debera ser testedo por su respectivo codigo test; pasando el test al 100%.

2.- Para poder pasar a done, debe de ser probado de manera unitaria el conjunto de codigos, pasando al 100% las pruebas unitarias.

3.-El analisis de cobertura del codigo debe de alcanzar minimo un 80% por medio de pytest-cov







