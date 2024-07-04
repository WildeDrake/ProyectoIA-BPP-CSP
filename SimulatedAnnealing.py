import math
import matplotlib.pyplot as plt
from numpy.random import *
import numpy.random as random
from scipy.spatial.distance import pdist
import numpy as np
import Global
import Contenedor
import Objetos


class simulated_annealing:
    # Contructor
    def __init__(self, ConjObjetos, t0, alpha, show, heuristic: callable):
        # Parametros del Simulating annealing.
        self.t0 = t0                        # Temperatura inicial.
        self.alpha = alpha                  # Factor de Enfriamiento de la Temperatura.
        self.outIte = 300                   # Numero de iteraciones en las que se reduce la Temperatura.
        self.inIte = 20                     # Numero de vecinos evaluados antes de bajar la Temperatura.
        self.p = np.array([0.3, 0.3, 0.4])  # Probabilidad de las operaciones swap/reversion/insertion.
        # Parametros del problema.
        self.heuristic = heuristic      # Heuris tica que evalua la solucion.
        self.ConjObjetos = ConjObjetos  # Lista de objetos.
        self.n = len(ConjObjetos)       # Numero de objetos.
        # Esto es para la animacion
        self.show_animation = show

    # Función principal del Simulated Annealing.
    def search(self):
        punActual = self.get_function_value(self.ConjObjetos)   # Evaluamos el conjuntos actual y guardamos su puntaje.
        bestConj = self.ConjObjetos.copy()      # Guarda la mejor permutacion encontrada hasta el momento.
        bestPun = punActual     # Guarda el puntaje de la mejor permutación hasta el momento.
        puntajes = [bestPun]    # Guarda el valor de la funcion para cada iteracion.
        T = self.t0     # Inicializamos la Temperatura.

        # Bucle principal del Simulated Annealing, en el cual disminuira la Temperatura.
        for outite in range(self.outIte):

            # Bucle interno del Simulated Annealing, en el cual se evaluaran los vecinos de la permutacion actual.
            for inite in range(self.inIte):
                nuevoConj = self.get_neighbor(self.ConjObjetos)     # Busca un vecino de ConjObjetos.
                nuevoPun = self.get_function_value(nuevoConj)       # Guarda el puntaje del vecino.
                # Si el vecino es mejor que el conjunto actual nos quedamos con el nuevo conjunto.
                if nuevoPun <= punActual:
                    self.ConjObjetos = nuevoConj
                    punActual = nuevoPun
                # Si el vecino no es mejor que el conjunto actual reemplazamos con una probabilidad p.
                else:
                    delta = (nuevoPun - punActual) / punActual  # Calcula el delta.
                    p = np.exp(-delta / T)                      # Calcula la probabilidad p.
                    if random.random() <= p:         # Reemplazamos segun p.
                        self.ConjObjetos = nuevoConj
                        punActual = nuevoPun
                # Si esta solucion es la mejor hasta el momento, la guardamos.
                if punActual < bestPun:
                    bestConj = self.ConjObjetos
                    bestPun = punActual

            T = self.alpha * T          # Baja la temperatura.
            puntajes.append(bestPun)  # Guarda el valor de la funcion para cada iteracion. (Esto es para graficar)

            # print(f'ite={outite}, f_value = {bestPun}\n')
        """# Animacion del Grafico.
            # Ignorar, esto es solo para animacion.
            if self.show_animation:
                plt.cla()
                route = ConjObjetos.copy()
                plt.title('simulated_annealing')
                plt.plot(puntajes)
                a1 = plt.annotate(f'step:{outite}\n f:{round(bestPun, 2)}', xy=(0.85, 0.9), xycoords='axes fraction',
                                  color='black')
                plt.axis('equal')
                plt.pause(0.001)
                if outite != self.outIte - 1:
                    a1.remove()
                    
        if self.show_animation:
            plt.pause(0)
        """


    # Esta funcion evalua el conjunto actual segun la heuristica seleccionada.
    def get_function_value(self, conj):
        cont = Contenedor.Contenedor(Global.dimContenedor)
        self.heuristic(cont, conj)
        return Global.area - cont.valor

    # Esta funcion nos da un vecino de x. En nuestro caso esta por definirse lo que consideraremos vecino. (¿sera una permuitacion cercana?)
    def get_neighbor(self, conj):
        tipo = choice([1, 2, 3], p=self.p.ravel()) # Elige un tipo de vecino segun las probabilidades de p.
        if tipo == 1:
            nuevoConj = self.swap(conj)
        elif tipo == 2:
            nuevoConj = self.reversion(conj)
        else:
            nuevoConj = self.insertion(conj)
        return nuevoConj

    # Esta funcion invierte el camino entre dos puntos aleatorios.
    def reversion(self, conj):
        nuevoConj = conj.copy()     # Copia de el camino conj.
        tmp = permutation(self.n)   # Permutacion aleatoria de los numeros del 0 al n-1.
        s1 = min(tmp[:2])   # El minimo de los dos primeros numeros de la permutacion.
        s2 = max(tmp[:2])   # El maximo de los dos primeros numeros de la permutacion.
        nuevoConj[s1:s2] = nuevoConj[s1:s2][::-1]    # Invierte el camino entre s1 y s2.
        return nuevoConj

    # Esta funcion intercambia dos puntos aleatorios.
    def swap(self, conj):
        nuevoConj = conj.copy()     # Copia de el camino conj.
        tmp = permutation(self.n)   # Permutacion aleatoria de los numeros del 0 al n-1.
        s1 = min(tmp[:2])       # El minimo de los dos primeros numeros de la permutacion.
        s2 = max(tmp[:2])       # El maximo de los dos primeros numeros de la permutacion.
        # Swap.
        tmp = nuevoConj[s1]
        nuevoConj[s1] = nuevoConj[s2]
        nuevoConj[s2] = tmp
        return nuevoConj

    # Esta funcion quita un objeto de un punto aleatorio y lo inserta en otro punto aleatorio.
    def insertion(self, conj):
        nuevoConj = conj.copy()     # Copia de el camino conj.
        tmp = permutation(self.n)   # Permutacion aleatoria de los numeros del 0 al n-1.
        s1 = tmp[0]     # El primer numero de la permutacion.
        s2 = tmp[1]     # El segundo numero de la permutacion.
        to_insert = nuevoConj[s1]             # Guarda el valor de nuevoConj[s1].
        nuevoConj = np.delete(nuevoConj, s1)  # Elimina el valor de nuevoConj[s1].
        # Si s1 es menor que s2.
        if s1 < s2:
            nuevoConj = np.insert(nuevoConj, s2, to_insert)     # Inserta el valor de to_insert en la posicion s2.
        else:
            nuevoConj = np.insert(nuevoConj, s2 + 1, to_insert) # Inserta el valor de to_insert en la posicion s2 + 1.
        return nuevoConj
