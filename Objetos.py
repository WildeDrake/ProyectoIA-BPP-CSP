import random
import math
import Global
import Contenedor
from looplist import looplist

if Global.randConj != 0:
    random.seed(Global.randConj)

# crear matriz a partir de puntos
def matrizDesdePuntos(puntos, id):
    min_x = min([c[0] for c in puntos])
    max_x = max([c[0] for c in puntos])
    min_y = min([c[1] for c in puntos])
    max_y = max([c[1] for c in puntos])
    matriz = [[0 for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for c in puntos:
        matriz[c[1] - min_y][c[0] - min_x] = id
    return matriz

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
        self.listColis = None
        self.listCont = None

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

        matriz = matrizDesdePuntos(lista_cuadrados, self.id)
        return matriz

    def tamano(self):
        return len(self.matriz), len(self.matriz[0])

    def crearListaColision(self):
        self.listColis = []
        for i in range(self.tamano()[1]):  # inicializa la lista con el primer cuadrado de la primera fila
            if self.matriz[0][i] != 0:
                self.listColis.append((0, i))
                break
    
        for y, x in self.listColis:  # recorre la lista mientras esta va creciendo
            for ay, ax in [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]:  # revisa los cuadrados adyacentes
                if (ay, ax) not in self.listColis and 0 <= ay < self.tamano()[0] \
                        and 0 <= ax < self.tamano()[1] and self.matriz[ay][ax] != 0:
                    self.listColis.append((ay, ax))  # si el cuadrado es parte del objeto, lo añade a la lista
    
    def verificarColisionConLista(self, cont, pos: tuple):
        # verificador eficiente, usa una checklist de los cuadrados a revisar
        if self.listColis is None:
            self.crearListaColision()

        for y, x in self.listColis:  # recorre la lista
            if cont.matriz[pos[0] + y][pos[1] + x] != 0:  # si el cuadrado colisiona con otro objeto
                return False
    
        return True

    def crearListaContacto(self):
        if self.listColis is None:
            self.crearListaColision()
    
        self.listCont = []
        for y, x in self.listColis:  # recorre la lista de cuadrados pertenecientes al objeto
            for ay, ax in [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]:  # revisa los cuadrados self.listCont
                if (ay, ax) not in self.listColis and (ay, ax) not in self.listCont:
                    self.listCont.append((ay, ax))
    
    
    def contarContactosConLista(self, cont, pos: tuple):
        # verificador eficiente, usa una checklist de los cuadrados a revisar
        if self.listCont is None:
            self.crearListaContacto()
    
        count = 0
        for y, x in self.listCont:  # recorre la lista
            ny, nx = pos[0] + y, pos[1] + x
            if not 0 < ny < cont.tamano[0] or not 0 < nx < cont.tamano[1] or cont.matriz[ny][nx] != 0:
                # si el cuadrado colisiona con el borde u otro objeto
                count += 1
    
        return count


def CrearObjetos(tmno_contenedor, area_max):
    areas = []
    vol_sum = 0
    while vol_sum < tmno_contenedor[0] * tmno_contenedor[1] * 3:
        areas.append(math.ceil(random.triangular(1, min(tmno_contenedor[0] * tmno_contenedor[1], area_max), 4)))
        vol_sum += areas[-1]

    objetos = []
    for i in range(len(areas)):
        objetos.append(Objeto(i + 1, areas[i], tmno_contenedor))

    return objetos


def crearObjetosRellenoPerfecto(tmno_contenedor, maxArea=16, numTrazos=None):
    if numTrazos is None:
        numTrazos = tmno_contenedor[0] * tmno_contenedor[1] // 8

    def armarMatrizObjeto(cuadradoInicial, id, maxArea):
        lista_cuadrados = []
        cuadrados = [cuadradoInicial]
        matrizContenedor[cuadradoInicial[0]][cuadradoInicial[1]] = 1
        while len(cuadrados) > 0:
            cuadrado = cuadrados.pop(0)
            lista_cuadrados.append(cuadrado)
            if not grilla[0][cuadrado[0]][cuadrado[1]]:
                c = cuadrado[0] - 1, cuadrado[1]
                if matrizContenedor[c[0]][c[1]] == 0:
                    matrizContenedor[c[0]][c[1]] = 1
                    cuadrados.append(c)
            if not grilla[1][cuadrado[0]][cuadrado[1]]:
                c = cuadrado[0], cuadrado[1] - 1
                if matrizContenedor[c[0]][c[1]] == 0:
                    matrizContenedor[c[0]][c[1]] = 1
                    cuadrados.append(c)
            if not grilla[0][cuadrado[0] + 1][cuadrado[1]]:
                c = cuadrado[0] + 1, cuadrado[1]
                if matrizContenedor[c[0]][c[1]] == 0:
                    matrizContenedor[c[0]][c[1]] = 1
                    cuadrados.append(c)
            if not grilla[1][cuadrado[0]][cuadrado[1] + 1]:
                c = cuadrado[0], cuadrado[1] + 1
                if matrizContenedor[c[0]][c[1]] == 0:
                    matrizContenedor[c[0]][c[1]] = 1
                    cuadrados.append(c)

        while len(lista_cuadrados) > maxArea:
            half = len(lista_cuadrados) // 2
            for c in lista_cuadrados[half:]:
                matrizContenedor[c[0]][c[1]] = 0
            lista_cuadrados = lista_cuadrados[:half]

        if len(lista_cuadrados) == 1:
            print(cuadradoInicial, lista_cuadrados[0])

        return matrizDesdePuntos(lista_cuadrados, id)


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

            if (grilla[0][signt[0]][signt[1]] == 1 or grilla[1][signt[0]][signt[1]] == 1
                    or grilla[0][signt[0]][signt[1] - 1] == 1 or grilla[1][signt[0] - 1][signt[1]] == 1):
                break
            elif signt in trazo[:-1]:
                for _ in range(trazo.index(signt) - 1):
                    trazo.pop(0)
                break

        # si el trazo es muy corto, probabilidad de ignorarlo
        if len(trazo) <= 6 and random.random() < 0.9:
            numTrazos.append(_)
            continue
        elif len(trazo) <= 5 and random.random() < 0.99:
            numTrazos.append(_)
            continue
        elif len(trazo) <= 3 and random.random() < 0.99:
            numTrazos.append(_)
            continue
        elif len(trazo) <= 2 and random.random() < 0.99:
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
                matriz = armarMatrizObjeto((i, j), len(objetos) + 1, maxArea)
                objetos.append(Objeto(len(objetos) + 1, matriz=matriz))

    return objetos


def findInList(lista, id) -> Objeto:
    for i in range(len(lista)):
        if lista[i].id == id:
            return lista[i]
