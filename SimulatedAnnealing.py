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
    def __init__(self, ConjObjetos, iter, show, heuristic: callable):
        # Parametros del Simulating annealing.
        t0 = 100                                    # Temperatura inicial.
        tf = 0.05                                   # Temperatura final.
        self.T = t0                                 # Temperatura actual.
        self.beta = (t0-tf)/(iter*t0*tf)            # Factor de Enfriamiento de la Temperatura.
        self.outIte = iter                          # Numero de iteraciones en las que se reduce la Temperatura.
        self.inIte = 20                             # Numero de vecinos evaluados antes de bajar la Temperatura.
        # Parametros del problema.
        self.heuristic = heuristic      # Heuristica que evalua la solucion.
        self.ConjObjetos = ConjObjetos  # Lista de objetos.
        self.n = len(ConjObjetos)       # Numero de objetos.
        # Esto es para la animacion
        self.show_animation = show

    # Función principal del Simulated Annealing.
    def search(self):
        print("num objetos: " + str(self.n))
        Lesgo = False
        punActual = self.get_function_value(self.ConjObjetos)   # Evaluamos el conjuntos actual y guardamos su puntaje.
        bestConj = self.ConjObjetos.copy()      # Guarda la mejor permutacion encontrada hasta el momento.
        bestPun = punActual     # Guarda el puntaje de la mejor permutación hasta el momento.
        puntajes = [bestPun]    # Guarda el valor de la funcion para cada iteracion.


        # Bucle principal del Simulated Annealing, en el cual disminuira la Temperatura.
        for outite in range(self.outIte):

            uphillCount = 0
            # Bucle interno del Simulated Annealing, en el cual se evaluaran los vecinos de la permutacion actual.
            inite = 0
            while inite < self.inIte:
                nuevoConj = self.get_neighbor(self.ConjObjetos, outite)     # Busca un vecino de ConjObjetos.
                nuevoPun = self.get_function_value(nuevoConj)       # Guarda el puntaje del vecino.
                # Si el vecino es mejor que el conjunto actual nos quedamos con el nuevo conjunto.
                if nuevoPun <= punActual:
                    self.ConjObjetos = nuevoConj
                    punActual = nuevoPun
                # Si el vecino no es mejor que el conjunto actual reemplazamos con una probabilidad p.
                else:
                    delta = (nuevoPun - punActual) / punActual  # Calcula el delta.
                    p = np.exp(-delta / self.T)                      # Calcula la probabilidad p.
                    if random.random() <= p:         # Reemplazamos segun p.
                        uphillCount += 1
                        self.ConjObjetos = nuevoConj
                        punActual = nuevoPun
                # Si esta solucion es la mejor hasta el momento, la guardamos.
                if punActual < bestPun:
                    inite = 0
                    bestConj = self.ConjObjetos
                    bestPun = punActual
                # si se llego a una solucion optima, se termina el algoritmo.
                if punActual == 0:
                    Lesgo = True
                    break

                inite += 1

            print(f'\rite={outite}, f_value = {bestPun}, T = {self.T}, upHill = {uphillCount}, VD = {int(np.floor(np.exp((np.log(self.n)/self.outIte)*outite)) - 1)}', end="")

            self.T = self.T/(1 + self.beta*self.T)        # Baja la temperatura.
            puntajes.append(bestPun)  # Guarda el valor de la funcion para cada iteracion. (Esto es para graficar)

            if outite % 30 == 0:
                print()

            if(Lesgo):
                break

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
    def get_neighbor(self, conj, outite):
        VD = int(np.exp((np.log(self.n)/self.outIte)*outite) - 1)
        return self.swap(conj, VD)

    # Esta funcion intercambia dos puntos aleatorios.
    def swap(self, conj, VectorDistance):
        nuevoConj = conj.copy()     # Copia de el camino conj.
        tmp = permutation(range(VectorDistance, self.n))   # Permutacion aleatoria de los numeros del 0 al n-1.
        s1 = min(tmp[:2])       # El minimo de los dos primeros numeros de la permutacion.
        s2 = max(tmp[:2])       # El maximo de los dos primeros numeros de la permutacion.
        # Swap.
        tmp = nuevoConj[s1]
        nuevoConj[s1] = nuevoConj[s2]
        nuevoConj[s2] = tmp
        return nuevoConj
