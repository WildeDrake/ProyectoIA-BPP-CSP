# Proyecto IA - Problema de la Mochila
<p style="text-align: center;">Semestre : 2024-1 </p>

<p style="text-align: center;"> - Francy Pilar Jélvez Jen.</p>
<p style="text-align: center;"> - Pedro Ignacio Palacios Rossi.</p>
<p style="text-align: center;"> - Diego Joaquín Andrés Venegas Anabalón.</p>
El Bin Packing Problem es un problema clásico en informática y matemáticas, especialmente en la teoría de la optimización y la combinatoria.

Consiste en que, dado un conjunto de elementos, cada uno con un volumen y un valor, y una capacidad máxima para unos contenedores, se debe determinar la combinación de elementos que maximice el valor total sin exceder la capacidad máxima del contenedor. En otras palabras, se trata de maximizar el valor de los objetos seleccionados, haciendo que quepan los objetos de la mejor forma en el contenedor.

Existen varios algoritmos para resolver este problema, como el algoritmo de fuerza bruta, programación dinámica u otros, cada uno con sus ventajas y desventajas en términos de eficiencia y precisión. Nosotros en particular, tenemos pensado hacer uso de diferentes métodos de inteligencia artificial para afrontar este problema y comparar sus resultados.

Ambiente: El ambiente de nuestro proyecto será:
- Observable (Se va a poder ver todas las elecciones a elegir).
- Determinista (No tiene componentes aleatorios).
- Secuencial (Pasa fase por fase).
- Estático (El espacio de la mochila y de las variables a elegir no va a cambiar de las preestablecidas).
- Discreto (Sólo hay tres acciones en total; Agregar/Quitar objetos de contenedor e ir al destino).
- Agente singular.

El agente, como antes mencionado, va a ser singular y dinámico.

El contenedor consiste en una matriz rectangular con espacios en blanco y espacios ocupados. 
Los objetos tendrán una forma (similar a una figura de Tetris), una posición dentro o fuera de la mochila y un color. 

Las acciones consisten en poner un objeto en el contenenedor (objeto, posición, rotación) y hacer un viaje con la mochila.



## Requerimientos:
- Python 3.8.2
- Pygame 2.5.2