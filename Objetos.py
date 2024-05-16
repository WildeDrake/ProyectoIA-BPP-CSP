import random
import math
import pygame

import Global
import Contenedor


class Objeto():
    def __init__(self, id, valor, volumen, tmno_max=(1000, 1000), color=None):
        self.id = id
        self.valor = valor
        if color is None:
            color = (random.randint(100, 250),
                     random.randint(100, 250),
                     random.randint(100, 250))
        self.color = color
        # Crear la forma con volumen cuadraditos.
        self.matriz = self.ConstruirMatriz(volumen, tmno_max)

    def ConstruirMatriz(self, volumen, tmno_max):  # metodo feo y penca
        tmno_max = (tmno_max[0] // 2, tmno_max[1] // 2)  # dividir por 2, más facil de manejar
        lista_cuadrados = []  # Lista de cuadrados que forman el objeto.
        lista_posibles_cuadrados = [(0, 0)]  # Lista de cuadrados que pueden ser añadidos.
        for _ in range(volumen):
            # Elegir un cuadrado aleatorio.
            nuevo_cuadrado = random.choice(lista_posibles_cuadrados)
            lista_cuadrados.append(nuevo_cuadrado)
            while nuevo_cuadrado in lista_posibles_cuadrados:
                lista_posibles_cuadrados.remove(nuevo_cuadrado)
            # Añadir los cuadrados adyacentes al nuevo cuadrado.
            for c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                vecino = (nuevo_cuadrado[0] + c[0], nuevo_cuadrado[1] + c[1])
                if (vecino not in lista_cuadrados
                        and -tmno_max[0] <= vecino[0] <= tmno_max[0]
                        and -tmno_max[1] <= vecino[1] <= tmno_max[1]):
                    lista_posibles_cuadrados.append(vecino)
        # crear matriz a partir de puntos
        min_x = min([c[0] for c in lista_cuadrados])
        max_x = max([c[0] for c in lista_cuadrados])
        min_y = min([c[1] for c in lista_cuadrados])
        max_y = max([c[1] for c in lista_cuadrados])
        matriz = [[0 for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
        for c in lista_cuadrados:
            matriz[c[1] - min_y][c[0] - min_x] = self.id
        return matriz

    def tamano(self):
        return len(self.matriz), len(self.matriz[0])


def CrearObjetos(tmno_contenedor, vol_max):

    volums = []
    vol_sum = 0
    while vol_sum < tmno_contenedor[0] * tmno_contenedor[1] * 3:
        volums.append(math.ceil(random.triangular(1, min(tmno_contenedor[0] * tmno_contenedor[1], vol_max), 4)))
        vol_sum += volums[-1]

    objetos = []
    for i in range(len(volums)):
        objetos.append(Objeto(i + 1, random.randint(1, 100), volums[i], tmno_contenedor))

    return objetos


def findInList(lista, id) -> Objeto:
    for i in range(len(lista)):
        if lista[i].id == id:
            return lista[i]
