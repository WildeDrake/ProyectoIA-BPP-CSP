# Proyecto IA - Problema de la Mochila
<p style="text-align: center;">Semestre : 2024-1 </p>

<p style="text-align: center;"> - Francy Pilar Jélvez Jen.</p>
<p style="text-align: center;"> - Pedro Ignacio Palacios Rossi.</p>
<p style="text-align: center;"> - Diego Joaquín Andrés Venegas Anabalón.</p>
El problema de la mochila es un problema clásico en informática y matemáticas, especialmente en la teoría de la optimización y la combinatoria.

Consiste en que, dado un conjunto de elementos, cada uno con un peso y un valor, y una capacidad máxima de carga para una mochila, se debe determinar la combinación de elementos que maximice el valor total sin exceder la capacidad máxima de la mochila. En otras palabras, se trata de maximizar el valor de los objetos seleccionados, pero que la suma de sus pesos no supere el límite establecido por la capacidad de la mochila.

Existen varios algoritmos para resolver este problema, como el algoritmo de fuerza bruta, programación dinámica u otros, cada uno con sus ventajas y desventajas en términos de eficiencia y precisión. Nosotros en particular, tenemos pensado hacer uso de diferentes métodos de inteligencia artificial para afrontar este problema y comparar sus resultados.

Ambiente: El ambiente de nuestro proyecto será:
- Observable (Se va a poder ver todas las elecciones a elegir).
- Determinista (No tiene componentes aleatorios).
- Secuencial (Pasa fase por fase).
- Estático (El espacio de la mochila y de las variables a elegir no va a cambiar de las preestablecidas).
- Discreto (Sólo hay tres acciones en total; Agregar/Quitar objetos de la mochila e ir al destino).
- Agente singular.

El agente, como antes mencionado, va a ser singular y dinámico.

La mochila consiste en una matriz rectangular con espacios en blanco y espacios ocupados. 
Los objetos tendrán una forma (similar a una figura de Tetris), una posición dentro o fuera de la mochila y un color. 

Las acciones consisten en poner un objeto en la mochila (objeto, posición, rotación) y hacer un viaje con la mochila.





Versiones:
- Python 3.8.2
- Pygame 2.5.2