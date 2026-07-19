Para esta primera entrega trabaje con la ayuda de la IA; Para poder 
desarrollar los programas solicitados dentro de la ruta de estudio; antes
de comenzar con la programacion di inicio a la guia de estudio con los 
links compartidos. En dichos links se nos dio un breve resumen de clases que
es tecnicamente con lo que comenzamos a estudiar; En mi caso utilice Gemini 
para guiarme en la programacion, le comparti la guia de estudio asi como
los entregables para que hiciera ura relacion de lo que trabajabamos y lo
que se tenia que entregar este sabado.

Despues de compartirle la guia de estudio me dio los programas completos para
los entregables de la semana sin embargo los ignore para empezar trabajando
con el dia uno, en el que se nos pedia crear una clase, una simple clase
que tecnicamente estaba descrita en lasa paginas compartidas en la gia de
estudio, nuevamente recurri a la IA para que me guiara y me explicara paso
por paso como funcionaba una clase; en esta ocasion el codigo me parecio el 
correcto y aplicable para la situacion y lo tome. 

La semana fue asi con la ayuda de la IA le pedia ayuda con el dia 
correspondiente, me daba un codigo lo analizaba yo si me parecia que 
relacionado con lo que veiamos lo escribia linea por linea yo; cada linea 
le pedia que me la explicara para poder comprender el funcionamiento y 
como todo lo que estudiamos en los articulos se formaba en lo solicitado.

En el caso de los principios solid: 
Me parecen que deberian ser una de las cosas mas importante que se nos 
enseñaran en los cursos de programacion de la facultad, sin embargo lo pasan
por alto o quiza solo muestran un poco de lo que realmente son; si fueran 
realmente aplicados como lo que son dentro de la facultad los trabajos 
entregables en cada una de las materias, no serian por el mero hecho de 
entregar si no de crear algo verdaderamente funcional dando puerta al 
entendimiento de otros proyectos en diversar materias. 
--------------------------------------------------------------------------------------
PROMTS, RESPUESTA DE LA IA y ELECCION

PROMT- tiene errores? from enum import Enum,auto
from dataclasses import dataclass
from datetime import datetime
from typing import List
class SensorType(Enum):#Enum es una clase que nos permite crear enumeraciones,
    #estas dos son las enumeraciones que vamos a usar para definir el tipo de sensor
    TEMPER...

RESPUESTA- Tu código está muy bien estructurado y tus comentarios explican 
perfectamente la lógica. Solo tiene tres detalles menores que causarán que mypy
o ruff te arrojen alertas de calidad o errores al ejecutar el código.
Aquí tienes los errores identificados y cómo corregirlos:
Los 3 detalles a corregir...

ELECCION- Antes de seguir los pasos que me dio decidi ejecutar por mi cuenta 
mypy y ruff para asegurarme, ademas de que estos me permiten arreglar 
los errores de consola (desde este momento lo supe).

--------------------------------------------------------------------------------------

PROMT- ayudame a entender laprimeraactividad  Lunes 13 — Python idiomático 
para ingenieros de C (3–4 h): practica enums, dataclasses frozen y Protocol 
con mini-ejercicios del dominio de sensores; 5 funciones puras sobre Reading 
con type hints, verificadas con mypy y ruff. Commit al final del día + primera 
entrada de la bitácora.

RESPUESTA- ¡Vamos a desglosarlo desde cero! Como hoy es martes 14 de julio, 
lo ideal es que dejemos completado este bloque del lunes para que hoy mismo 
puedas avanzar con la Máquina de Estados (FSM) sin arrastrar pendientes.

Para que entiendas perfectamente de qué se trata esta actividad, la vamos a 
estructurar en tres conceptos clave que un ingeniero de C necesita entender 
al migrar a Python, y luego ensamblaremos el código paso a paso.

Concepto 1: ¿Qué es una dataclass frozen? (Paso 3 de tu ruta)
En C, para agrupar variables usas un struct. Por ejemplo...

ELECCION- Despues de leer lo que me proporciono y asegurarme de que se apegara 
al conocimiento recien adquirido aplique lo que me proporciono, el relacionar 
eltrabajo con la creacion de las clases.

--------------------------------------------------------------------------------------

PROMT- cuales son las caracteristicas que debo de cuidar a la hora de crear 
una clase, osea que debo de analizar para crear una clase por ejemplo si me 
dieran instrucciones de algo que necesito que deberia de bucar hacer primero

RESPUESTA- Cuando te dan las instrucciones de un problema y necesitas diseñar 
una clase, no te lances a escribir código de inmediato. El secreto para crear
una buena clase consiste en actuar como un ingeniero de diseño electrónico: 
antes de tirar pistas en una PCB, analizas los componentes, sus entradas y sus 
salidas.

Para diseñar una clase de forma estructurada, debes aplicar un proceso de tres 
pasos: Identificar el Sujeto, Definir sus Atributos y Establecer sus Métodos.

Paso 1: Encontrar el "Sujeto" (El Sustantivo)
Lo primero que debes buscar en el texto de las instrucciones son los 
sustantivos (personas, lugares, cosas, dispositivos o conceptos). 
El sustantivo principal se convertirá en el nombre de tu clase...

ELECCION- Lo ocupe com guia para entender cuales pueden ser las aplicaciones 
de las clases en distintos ambitos, asi como la manera de poder desarrollar 
una desde cero cuando se me solicitara.








