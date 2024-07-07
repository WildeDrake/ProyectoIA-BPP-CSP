import SimulatedAnnealing
import Contenedor
import Objetos
import Global
import Dibujar
import pygame


####################### Funciones y clases utilizadas por las heuristicas #######################
def verificarColision(cont: Contenedor.Contenedor, obj: Objetos.Objeto, pos: tuple):
    for i in range(obj.tamano()[0]):
        for j in range(obj.tamano()[1]):
            if obj.matriz[i][j] != 0 and cont.matriz[pos[0] + i][pos[1] + j] != 0:
                return False
    return True


def crearListaColision(obj: Objetos.Objeto):
    # verificador más eficiente, crea una lista de los cuadrados por revisar
    cuadrados = []
    for i in range(obj.tamano()[1]):  # inicializa la lista con el primer cuadrado de la primera fila
        if obj.matriz[0][i] != 0:
            cuadrados.append((0, i))
            break

    for y, x in cuadrados:  # recorre la lista hasta que este vacía
        for ay, ax in [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]:  # revisa los cuadrados adyacentes
            if (ay, ax) not in cuadrados and 0 <= ay < obj.tamano()[0] \
                    and 0 <= ax < obj.tamano()[1] and obj.matriz[ay][ax] != 0:
                cuadrados.append((ay, ax))  # si el cuadrado es parte del objeto, lo añade a la lista

    return cuadrados


def verificarColisionConLista(cont: Contenedor.Contenedor, obj: Objetos.Objeto, pos: tuple, listaColision: list = None):
    if listaColision is None:
        listaColision = crearListaColision(obj)

    for y, x in listaColision:  # recorre la lista hasta que este vacía
        if cont.matriz[pos[0] + y][pos[1] + x] != 0:  # si el cuadrado colisiona con otro objeto
            return False

    return True


def crearListaContacto(obj: Objetos.Objeto, listaColision: list = None):
    if listaColision is None:
        listaColision = crearListaColision(obj)

    adyacentes = []

    for y, x in listaColision:  # recorre la lista hasta que este vacía
        for ay, ax in [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]:  # revisa los cuadrados adyacentes
            if (ay, ax) not in listaColision and (ay, ax) not in adyacentes:
                adyacentes.append((ay, ax))

    return adyacentes


def contarContactos2(cont: Contenedor.Contenedor, obj: Objetos.Objeto, pos: tuple, listaContactos: list = None):
    if listaContactos is None:
        listaContactos = crearListaContacto(obj)

    count = 0
    for y, x in listaContactos:  # recorre la lista hasta que este vacía
        ny, nx = pos[0] + y, pos[1] + x
        if not 0 < ny < cont.tamano[0] or not 0 < nx < cont.tamano[1] or cont.matriz[ny][nx] != 0:
            # si el cuadrado colisiona con el borde u otro objeto
            count += 1

    return count


def colocarObjeto(cont: Contenedor.Contenedor, obj: Objetos.Objeto, pos: tuple):
    count = 0
    for i in range(obj.tamano()[0]):
        for j in range(obj.tamano()[1]):
            if obj.matriz[i][j] != 0:
                cont.matriz[pos[0] + i][pos[1] + j] = obj.id
                count += 1
                if count == obj.valor:
                    cont.valor += obj.valor
                    return


def QuitarObjeto(contenedor, pos):
    # Encontrar el objeto.
    id = contenedor.matriz[pos[0]][pos[1]]
    if id == 0:
        return False
    # Quitar matriz del objeto.
    for i in range(contenedor.tamano[0]):
        for j in range(contenedor.tamano[1]):
            if contenedor.matriz[i][j] == id:
                contenedor.matriz[i][j] = 0
    # Quitar objeto del contenedor y añadirlo al conjunto.
    for objeto in contenedor.objetos:
        if objeto.id == id:
            aux = objeto
            contenedor.valor -= objeto.valor
            contenedor.objetos.remove(objeto)
            break
    return True


""" Aun no utilizo esto pero lo dejo por aca :v
class Esquinas:
    def __init__(self):
        # Esquinas externas.
        self.esqSupIzqEx = []
        self.esqSupDerEx = []
        self.esqInfIzqEx = []
        self.esqInfDerEx = []
        # Esquinas internas.
        self.esqSupIzqEx = []
        self.esqSupDerEx = []
        self.esqInfIzqEx = []
        self.esqInfDerEx = []
"""


def contarContactos(cont: Contenedor.Contenedor, pos: tuple):
    count = 0
    # Revisar si el cuadrado tiene un vecino a la izquierda.
    if (pos[0] == 0):
        count += 1
    else:
        if (cont.matriz[pos[0] - 1][pos[1]] != 0):
            count += 1
    # Revisar si el cuadrado tiene un vecino a la derecha.
    if (pos[0] == cont.tamano[0] - 1):
        count += 1
    else:
        if (cont.matriz[pos[0] + 1][pos[1]] != 0):
            count += 1
    # Revisar si el cuadrado tiene un vecino arriba.
    if (pos[1] == 0):
        count += 1
    else:
        if (cont.matriz[pos[0]][pos[1] - 1] != 0):
            count += 1
    # Revisar si el cuadrado tiene un vecino abajo.
    if (pos[1] == cont.tamano[1] - 1):
        count += 1
    else:
        if (cont.matriz[pos[0]][pos[1] + 1] != 0):
            count += 1
    return count


def contarContactosObj(cont: Contenedor.Contenedor, obj: Objetos.Objeto, pos: tuple):
    count = 0
    for i in range(obj.tamano()[0]):
        for j in range(obj.tamano()[1]):
            if obj.matriz[i][j] != 0:
                count += contarContactos(cont, (pos[0] + i, pos[1] + j))
    return count


############################# Heuristica 1 #############################
def readingOrder(cont: Contenedor.Contenedor, objs: list, showAnimation=False, screen=None):
    # Se coloca objeto por objeto en el contenedor.
    for obj in objs:
        listColis = crearListaColision(obj)
        flag = False
        # Se recorre el contenedor de izq a der, se baja una unidad y se repite.
        for i in range(cont.tamano[0] - obj.tamano()[0] + 1):
            for j in range(cont.tamano[1] - obj.tamano()[1] + 1):
                if verificarColisionConLista(cont, obj, (i, j), listColis):
                    colocarObjeto(cont, obj, (i, j))
                    # Animacion
                    if showAnimation:
                        cont.objetos.append(obj)
                        screen.fill((0, 0, 0))
                        Dibujar.dibujar_background(screen)
                        Dibujar.dibujar_contenedor(screen, cont)
                        pygame.display.flip()
                    # Fin animacion
                    flag = True
                    break
            if flag:
                break


############################# Heuristica 2 #############################
def heuristica2(cont: Contenedor.Contenedor, objs: list, showAnimation=False, screen=None):
    # Se coloca objeto por objeto en el contenedor.
    for obj in objs:
        listColis = crearListaColision(obj)
        listConta = crearListaContacto(obj, listColis)
        max = -1
        # Se recorre el contenedor de izq a der, se baja una unidad y se repite.
        for i in range(cont.tamano[0] - obj.tamano()[0] + 1):
            for j in range(cont.tamano[1] - obj.tamano()[1] + 1):
                if verificarColisionConLista(cont, obj, (i, j), listColis):
                    contactos = contarContactos2(cont, obj, (i, j), listConta)
                    if max < contactos:
                        max = contactos
                        pos = (i, j)
        if max != -1:
            colocarObjeto(cont, obj, pos)
        # Animacion
        if showAnimation:
            cont.objetos.append(obj)
            screen.fill((0, 0, 0))
            Dibujar.dibujar_background(screen)
            Dibujar.dibujar_contenedor(screen, cont)
            pygame.display.flip()
        # Fin animacion


############################# Agente #############################
def Agente(modo, heuristica, showAnimation, Problem, screen=None):
    # Para Problema.
    if Problem == 0:
        ConjObjetos = Objetos.crearObjetosRellenoPerfecto(Global.dimContenedor)
    else:
        ConjObjetos = Objetos.CrearObjetos(Global.dimContenedor, 16)
    # Para el modo.
    if modo == 1:  # Modo Heuristica.
        cont = Contenedor.Contenedor(Global.dimContenedor)
        if heuristica == 0:
            readingOrder(cont, ConjObjetos, showAnimation, screen)
        else:
            heuristica2(cont, ConjObjetos, showAnimation, screen)
        print("Valor total: ", cont.valor)
    else:  # Modo Simulated Annealing.
        if heuristica == 0:
            SA = SimulatedAnnealing.simulated_annealing(ConjObjetos, 300, showAnimation, readingOrder)
        else:
            SA = SimulatedAnnealing.simulated_annealing(ConjObjetos, 300, showAnimation, heuristica2)
        SA.search()
