import math
import matplotlib.pyplot as plt
from numpy.random import *
import numpy.random as random
from scipy.spatial.distance import pdist
import numpy as np

import Global
import Contenedor
import Objetos

"""
t0: un int, la temperatura inicial
alpha: un int, el factor de enfriamiento
n:  un int, el número de nodos
x:  list N size: position x
y:  list N size: position y 
"""


class simulated_annealing:
    def __init__(self, ConjObjetos, t0, alpha, show, heuristic: callable):
        self.t0 = t0 # Temperatura inicial.
        self.alpha = alpha # Factor de enfriamiento.
        self.outIte = 300   # Numero de iteraciones.
        self.inIte = 20    # Numero de iteraciones.
        self.p = np.array([0.3, 0.3, 0.4])  # swap/reversion/insertion
        self.show_animation = show
        self.heuristic = heuristic
        self.n = len(ConjObjetos) # Numero de nodos.
        self.ConjObjetos = ConjObjetos # Lista de objetos.

    def search(self):
        PunActual = self.get_function_value() # Calcula el valor de la funcion para la permutacion ConjObjetos.
        bestConj = self.ConjObjetos.copy()  # bestConj guarda la mejor permutacion encontrada.
        bestscore = PunActual # bestscore guarda el valor de la funcion para la mejor permutacion encontrada.
        scores = [bestscore] # scores guarda el valor de la funcion para cada iteracion.
        T = self.t0 # T es la temperatura.

        for outite in range(self.outIte): # outite es el numero de iteraciones.

            for inite in range(self.inIte): # inite es el numero de iteraciones.
                NuevoConj = self.get_neighbor(self.ConjObjetos) # NuevoConj es un vecino de self.ConjObjetos.
                NuevoPun = self.get_function_value(NuevoConj) # NuevoPun es el valor de la funcion para la permutacion NuevoConj.
                if NuevoPun <= PunActual: # Si NuevoPun es menor o igual a PunActual.
                    self.ConjObjetos = NuevoConj # Swap por que NuevoConj es mejor camino que self.ConjObjetos.
                    PunActual = NuevoPun
                else: # Si PunActual es menor a NuevoPun, es decir no es mejor.
                    delta = (NuevoPun - PunActual) / PunActual # Calcula el delta.
                    p = np.exp(-delta / T) # Calcula la probabilidad.
                    if random.random() <= p: # La parte aleatoria de Simulated Annealing.
                                             # Si el numero aleatorio es menor o igual a la probabilidad.
                        self.ConjObjetos = NuevoConj # Swap por aleatoriedad.
                        PunActual = NuevoPun
                if PunActual < bestscore: # Si PunActual es menor a bestscore.
                    bestConj = self.ConjObjetos # Swap por que PunActual es mejor que bestscore.
                    bestscore = PunActual

            scores.append(bestscore)
            T = self.alpha * T # Baja la temperatura.

        """
            # print(f'ite={outite}, f_value = {bestscore}\n')
            # Ignorar, esto es solo para animacion.
            if self.show_animation:
                plt.cla()
                route = ConjObjetos.copy()
                plt.title('simulated_annealing')
                plt.plot(scores)
                a1 = plt.annotate(f'step:{outite}\n f:{round(bestscore, 2)}', xy=(0.85, 0.9), xycoords='axes fraction',
                                  color='black')
                plt.axis('equal')
                plt.pause(0.001)
                if outite != self.outIte - 1:
                    a1.remove()
        # Esto igual es animacion kkkkkkkkkkk.
        if self.show_animation:
            plt.pause(0)
        """


# Esta funcion calcula el camino r que le damos, en nuestro caso sera diferente.
    def get_function_value(self):
        cont = Contenedor.Contenedor(Global.dimContenedor)
        self.heuristic(cont, self.ConjObjetos)
        return Global.volumen - cont.valor

# Esta funcion nos da un vecino de x. En nuestro caso esta por definirse lo que consideraremos vecino. (¿sera una permuitacion cercana?)
    def get_neighbor(self, x):
        index = choice([1, 2, 3], p=self.p.ravel())
        if index == 1:
            # print('swap')
            newx = self.swap(x)
        elif index == 2:
            # print('reversion')
            newx = self.reversion(x)
        else:
            # print('insertion')
            newx = self.insertion(x)
        return newx

# Esta funcion invierte el camino entre dos puntos aleatorios.
    def reversion(self, x):
        newx = x.copy() # Copia de el camino x.
        tmp = permutation(self.n) # Permutacion aleatoria de los numeros del 0 al n-1.
        s1 = min(tmp[:2]) # El minimo de los dos primeros numeros de la permutacion.
        s2 = max(tmp[:2]) # El maximo de los dos primeros numeros de la permutacion.
        newx[s1:s2] = newx[s1:s2][::-1] # Invierte el camino entre s1 y s2.
        return newx

# Esta funcion intercambia dos puntos aleatorios.
    def swap(self, x):
        newx = x.copy() # Copia de el camino x.
        tmp = permutation(self.n) # Permutacion aleatoria de los numeros del 0 al n-1.
        s1 = min(tmp[:2]) # El minimo de los dos primeros numeros de la permutacion.
        s2 = max(tmp[:2]) # El maximo de los dos primeros numeros de la permutacion.
        tmp = newx[s1] # Guarda el valor de newx[s1].
        newx[s1] = newx[s2] # Cambia el valor de newx[s1] por el valor de newx[s2].
        newx[s2] = tmp # Cambia el valor de newx[s2] por el valor de tmp.
        return newx


    def insertion(self, x):
        newx = x.copy() # Copia de el camino x.
        tmp = permutation(self.n) # Permutacion aleatoria de los numeros del 0 al n-1.
        s1 = tmp[0] # El primer numero de la permutacion.
        s2 = tmp[1] # El segundo numero de la permutacion.
        to_insert = newx[s1] # Guarda el valor de newx[s1].
        newx = np.delete(newx, s1) # Elimina el valor de newx[s1].
        if s1 < s2: # Si s1 es menor que s2.
            newx = np.insert(newx, s2, to_insert) # Inserta el valor de to_insert en la posicion s2.
        else:
            newx = np.insert(newx, s2 + 1, to_insert) # Inserta el valor de to_insert en la posicion s2 + 1.
        return newx
