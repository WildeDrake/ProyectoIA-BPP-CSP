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
        r0 = permutation(self.n) # Es una permutacion aleatoria de los números del 0 al n-1.
        f0 = self.get_function_value(r0) # Calcula el valor de la funcion para la permutacion r0.
        bestR = r0  # bestR guarda la mejor permutacion encontrada.
        bestscore = f0 # bestscore guarda el valor de la funcion para la mejor permutacion encontrada.
        scores = [bestscore] # scores guarda el valor de la funcion para cada iteracion.
        T = self.t0 # T es la temperatura.
        for outite in range(self.outIte): # outite es el numero de iteraciones.
            for inite in range(self.inIte): # inite es el numero de iteraciones.
                r1 = self.get_neighbor(r0) # r1 es un vecino de r0.
                f1 = self.get_function_value(r1) # f1 es el valor de la funcion para la permutacion r1.
                if f1 <= f0: # Si f1 es menor o igual a f0.
                    r0 = r1 # Swap por que r1 es mejor camino que r0.
                    f0 = f1
                else: # Si f0 es menor a f1, es decir no es mejor.
                    delta = (f1 - f0) / f0 # Calcula el delta.
                    p = np.exp(-delta / T) # Calcula la probabilidad.
                    if random.random() <= p: # La parte aleatoria de Simulated Annealing.
                                             # Si el numero aleatorio es menor o igual a la probabilidad.
                        r0 = r1 # Swap por aleatoriedad.
                        f0 = f1
                if f0 < bestscore: # Si f0 es menor a bestscore.
                    bestR = r0 # Swap por que f0 es mejor que bestscore.
                    bestscore = f0
            scores.append(bestscore)
            print(f'ite={outite}, f_value = {bestscore}\n')
            T = self.alpha * T # Baja la temperatura.


            # Ignorar, esto es solo para animacion.
            if self.show_animation:
                plt.cla()
                route = r0.copy()
                route = np.append(route, r0[0])
                # plt.plot(np.array(self.x)[route.astype(int)],np.array(self.y)[route.astype(int)],'o-', lw=2, color='orange')
                # plt.plot(self.x,self.y,'o',color='red')
                plt.title('simulated_annealing')
                plt.plot(scores)
                a1 = plt.annotate(f'step:{outite}\n f:{round(bestscore, 2)}', xy=(0.85, 0.9), xycoords='axes fraction',
                                  color='black')
                # a2 = plt.annotate(f'T={self.t0}', xy=(0.5, 1.05), xycoords='axes fraction',color='black')
                plt.axis('equal')
                plt.pause(0.001)
                if outite != self.outIte - 1:
                    a1.remove()
                    # a2.remove()
        # Esto igual es animacion kkkkkkkkkkk.
        if self.show_animation:
            plt.pause(0)


# Esta funcion calcula el camino r que le damos, en nuestro caso sera diferente.
    def get_function_value(self, x0):
        '''
        here the function value (what we are going to minimize) is the total length of path
        '''

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

# Esto es pal TSP.
def point(x0, y0, r):
    theta = random.random() * 2 * math.pi
    return [x0 + math.cos(theta) * r, y0 + math.sin(theta) * r]


def main():
    random.seed(10)
    n = 30
    xy = [point(0, 0, 2) for _ in range(n)] # 30 puntos aleatorios.
    x = [point[0] for point in xy]
    y = [point[1] for point in xy]
    # plt.scatter(x,y)
    # plt.axis("equal")
    # plt.show()
    sl = simulated_annealing(x, y, t0=0.05, alpha=0.99, show=True)
    sl.search()


if __name__ == '__main__':
    main()