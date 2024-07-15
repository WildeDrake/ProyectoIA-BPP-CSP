# Proyecto IA - Bin Packing Problem / Cutting Stock Problem
<p style="text-align: center;">Semestre : 2024-1 </p>

<p style="text-align: center;"> - Francy Pilar Jélvez Jen.</p>
<p style="text-align: center;"> - Pedro Ignacio Palacios Rossi.</p>
<p style="text-align: center;"> - Diego Joaquín Andrés Venegas Anabalón.</p>

Este programa es una variante del conocido ‘Bin Packing Problem’, un problema clásico en informática y matemáticas, especialmente en la teoría de la optimización combinatoria.
Consiste en que, dado un conjunto de elementos, cada uno con un volumen, y una capacidad máxima para unos contenedores, se debe determinar la combinación de elementos que maximice el uso del espacio total sin exceder la capacidad máxima del contenedor. Nuestro programa tiene objetos con un valor que equivale al área del objeto, es representable en 2 dimensiones y constará de un sólo contenedor. 

Aparte del Bin Packing Problem, nuestro programa también busca resolver el también conocido 'Cutting Stock Problem'. Este problema consiste en que, dado una pieza de papel y una cantidad de cortes que
se deben cortar si o si, se busca minimizar los espacios vacíos que quedan en dicho papel por los cortes, también llamado como 'Trim loss'. La variante de Cutting Stock que buscamos resolver es la de 2 dimensiones sin guillotina (Que no hace un corte completo de ancho y largo, lo que le da más variedad de forma a los objetos, tomando formas parecidas a las piezas de Tetris)

Ambiente: El ambiente de nuestro proyecto será:
- Observable (Se va a poder ver todas las elecciones a elegir).
- Determinista (No tiene componentes aleatorios).
- Secuencial (Pasa fase por fase).
- Estático (El espacio de la mochila y de las variables a elegir no va a cambiar de las preestablecidas).
- Discreto (Sólo hay tres acciones en total; Agregar/Quitar objetos de contenedor e ir al destino).

El agente va a ser singular y dinámico, y ocupará el método de búsqueda local de Simulated Annealing, con dos heurísticas: readingOrder y contactSurface. Su funcionamiento está detallado en el informe adjunto.

El contenedor consiste en una matriz rectangular con espacios en blanco y espacios ocupados. 

Los objetos tendrán una posición dentro o fuera de la mochila y un color. 

Las restricciones del problema serán:
 - No se pueden superponer objetos sobre otros en el contenedor. 
 - Todos los objetos en el contenedor deben estar completamente dentro de este.
 - No se permitirá la rotación de objetos. 


## Requerimientos:
- Python 3.8.2
- Pygame 2.5.2

## Instrucciones:
**Para correr el juego, ejecutar main.py.** 
En main.py se encontrarán cuatro variables entre las líneas 10 - 17 que determinan como se ejecutará el programa:
	- mode: Para elegir el modo del programa. Si se desea “Jugar” (Manualmente colocar los objetos en el contenedor), se elige mode = 0. Si se desea correr una sola iteración de Simulated Annealing (El primer episodio del algoritmo), se elige mode = 1. Si se desea ejecutar todas las iteraciones de Simulated Annealing hasta encontrar la solución del problema elegido, se elige mode = 2. 
  - heuristic: Para elegir la heurística a utilizar. Si se desea ocupar countingOrder, se elige heuristic = 0. En cambio, si se desea ocupar ContactSurface se elige heuristic = 1. 
	- showAnimation: Mostrar o no la animación de la interfaz mientras es resuelta por el agente. Si se desea ver sin la animación, se elige showAnimation = 0, y si se desea ver la animación se elige showAnimation = 1. 
	- Problem: Elegir el problema a resolver. Si se desea solucionar el de Cutting Stock, se elige Problem = 0. Si se desea solucionar Bin Packing Problem, se elige Problem = 1.
Otras variables importantes se encuentran en Global.py, en la líneas 2-5:
  - WIDTH, HEIGHT = El ancho y el alto de la resolución de la ventana, respectivamente.
  - dimContenedor = Las dimensiones de ancho y alto del contenedor.
  - randConj = Semilla con la cual se crean los objetos. Si se desea una seed aleatoria, se elige
  randConj = 0.
  - bg = Fondo ilustrado del juego. Fondo de gatito en bg = 0 y fondo de ajolote en bg = 1
