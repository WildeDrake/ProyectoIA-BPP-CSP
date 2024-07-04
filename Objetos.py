import random
import math
import Global
from looplist import looplist


if Global.randConj != 0:
    random.seed(Global.randConj)

class Objeto():
    def __init__(self, id, area=None, tmno_max=(1000, 1000), matriz=None, color=None):
        self.id = id
        if color is None:
            color = (random.randint(50, 250),
                     random.randint(50, 250),
                     random.randint(50, 250))
        self.color = color
        if area is not None:
            self.valor = area
            self.matriz = self.ConstruirMatriz(area, tmno_max)
        elif matriz is not None:
            self.matriz = matriz
            self.valor = 0
            for i in range(len(self.matriz)):
                for j in range(len(self.matriz[0])):
                    if self.matriz[i][j] == self.id:
                        self.valor += 1

    def ConstruirMatriz(self, area, tmno_max):  # metodo feo y penca
        tmno_max = (tmno_max[0] // 2, tmno_max[1] // 2)  # dividir por 2, más facil de manejar
        lista_cuadrados = []  # Lista de cuadrados que forman el objeto.
        lista_posibles_cuadrados = [(0, 0)]  # Lista de cuadrados que pueden ser añadidos.
        for _ in range(area):
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
    areas = []
    vol_sum = 0
    while vol_sum < tmno_contenedor[0] * tmno_contenedor[1] * 3:
        areas.append(math.ceil(random.triangular(1, min(tmno_contenedor[0] * tmno_contenedor[1], vol_max), 4)))
        vol_sum += areas[-1]

    objetos = []
    for i in range(len(areas)):
        objetos.append(Objeto(i + 1, areas[i], tmno_contenedor))

    return objetos


def crearObjetosRellenoPerfecto(tmno_contenedor, numTrazos=60, maxVol=16):
    def armarMatrizObjeto(cuadradoInicial, id, maxVol):
        lista_cuadrados = []
        cuadrados = [cuadradoInicial]
        matrizContenedor[cuadradoInicial[0]][cuadradoInicial[1]] = 1
        while len(cuadrados) > 0:
            cuadrado = cuadrados.pop(0)
            lista_cuadrados.append(cuadrado)
            if not grilla[0][cuadrado[0]][cuadrado[1]] and maxVol > 0:
                maxVol -= 1
                c = cuadrado[0] - 1, cuadrado[1]
                if matrizContenedor[c[0]][c[1]] == 0:
                    matrizContenedor[c[0]][c[1]] = 1
                    cuadrados.append(c)
            if not grilla[1][cuadrado[0]][cuadrado[1]] and maxVol > 0:
                maxVol -= 1
                c = cuadrado[0], cuadrado[1] - 1
                if matrizContenedor[c[0]][c[1]] == 0:
                    matrizContenedor[c[0]][c[1]] = 1
                    cuadrados.append(c)
            if not grilla[0][cuadrado[0] + 1][cuadrado[1]] and maxVol > 0:
                maxVol -= 1
                c = cuadrado[0] + 1, cuadrado[1]
                if matrizContenedor[c[0]][c[1]] == 0:
                    matrizContenedor[c[0]][c[1]] = 1
                    cuadrados.append(c)
            if not grilla[1][cuadrado[0]][cuadrado[1] + 1] and maxVol > 0:
                maxVol -= 1
                c = cuadrado[0], cuadrado[1] + 1
                if matrizContenedor[c[0]][c[1]] == 0:
                    matrizContenedor[c[0]][c[1]] = 1
                    cuadrados.append(c)
        # crear matriz a partir de puntos
        min_x = min([c[0] for c in lista_cuadrados])
        max_x = max([c[0] for c in lista_cuadrados])
        min_y = min([c[1] for c in lista_cuadrados])
        max_y = max([c[1] for c in lista_cuadrados])
        matriz = [[0 for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
        for c in lista_cuadrados:
            matriz[c[1] - min_y][c[0] - min_x] = id
        return matriz

    grilla = looplist([looplist([looplist([0 for _ in range(tmno_contenedor[1])]) for _ in range(tmno_contenedor[0])])
                       for _ in range(2)])

    for i in range(tmno_contenedor[0]):
        grilla[1][i][0] = 1
    for j in range(tmno_contenedor[1]):
        grilla[0][0][j] = 1

    numTrazos = [_ for _ in range(numTrazos)]
    for _ in numTrazos:
        trazo = []
        while True:
            inic = (random.randint(0, tmno_contenedor[0] - 1), random.randint(0, tmno_contenedor[1] - 1))
            if grilla[0][inic[0]][inic[1]] == 1 or grilla[1][inic[0]][inic[1]] == 1:
                trazo.append(inic)
                break

        direccion = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        signt = inic
        while True:
            if random.random() < 0.4:
                direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                direcciones.remove((direccion[0] * -1, direccion[1] * -1))
                direccion = random.choice(direcciones)

            signt = (signt[0] + direccion[0], signt[1] + direccion[1])
            trazo.append(signt)

            if grilla[0][signt[0]][signt[1]] == 1 or grilla[1][signt[0]][signt[1]] == 1:
                break
            elif signt in trazo[:-1]:
                for _ in range(trazo.index(signt) - 1):
                    trazo.pop(0)
                break

        # si el trazo es muy corto, probabilidad de ignorarlo
        if len(trazo) < 6 and random.random() < 0.9:
            numTrazos.append(_)
            continue

        # grabar trazo en la grilla
        for i in range(len(trazo) - 1):
            if trazo[i][0] == trazo[i + 1][0]:
                if trazo[i][1] < trazo[i + 1][1]:
                    grilla[0][trazo[i][0]][trazo[i][1]] = 1
                else:
                    grilla[0][trazo[i + 1][0]][trazo[i + 1][1]] = 1
            else:
                if trazo[i][0] < trazo[i + 1][0]:
                    grilla[1][trazo[i][0]][trazo[i][1]] = 1
                else:
                    grilla[1][trazo[i + 1][0]][trazo[i + 1][1]] = 1
    """
    # print grilla
    for i in range(tmno_contenedor[0]):
        for j in range(tmno_contenedor[1]):
            if grilla[0][i][j] == 1 and grilla[1][i][j] == 1:
                print("+", end="")
            elif grilla[0][i][j] == 1:
                print("-", end="")
            elif grilla[1][i][j] == 1:
                print("|", end="")
            else:
                print(" ", end="")
        print()
    """

    objetos = []
    matrizContenedor = [[0 for _ in range(tmno_contenedor[1])] for _ in range(tmno_contenedor[0])]
    for i in range(tmno_contenedor[0]):
        for j in range(tmno_contenedor[1]):
            if matrizContenedor[i][j] == 0:
                matriz = armarMatrizObjeto((i, j), len(objetos) + 1, maxVol)
                objetos.append(Objeto(len(objetos) + 1, matriz=matriz))

    return objetos


def findInList(lista, id) -> Objeto:
    for i in range(len(lista)):
        if lista[i].id == id:
            return lista[i]
