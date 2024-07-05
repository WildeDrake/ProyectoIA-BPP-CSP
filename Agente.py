import SimulatedAnnealing
import Contenedor
import Objetos
import Global


####################### Funciones y clases utilizadas por las heuristicas #######################
def verificarColision(cont: Contenedor.Contenedor, obj: Objetos.Objeto, pos: tuple):
    for i in range(obj.tamano()[0]):
        for j in range(obj.tamano()[1]):
            if obj.matriz[i][j] != 0 and cont.matriz[pos[0] + i][pos[1] + j] != 0:
                return False
    return True

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
    if(pos[0] == 0):
        count += 1
    else:
        if(cont.matriz[pos[0]-1][pos[1]] != 0):
            count += 1
    # Revisar si el cuadrado tiene un vecino a la derecha.
    if(pos[0] == cont.tamano[0]-1):
        count += 1
    else:
        if(cont.matriz[pos[0]+1][pos[1]] != 0):
            count += 1
    # Revisar si el cuadrado tiene un vecino arriba.
    if(pos[1] == 0):
        count += 1
    else:
        if(cont.matriz[pos[0]][pos[1]-1] != 0):
            count += 1
    # Revisar si el cuadrado tiene un vecino abajo.
    if(pos[1] == cont.tamano[1]-1):
        count += 1
    else:
        if(cont.matriz[pos[0]][pos[1]+1] != 0):
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
def readingOrder(cont: Contenedor.Contenedor, objs: list):
    # Se coloca objeto por objeto en el contenedor.
    for obj in objs:
        flag = False
        # Se recorre el contenedor de izq a der, se baja una unidad y se repite.
        for i in range(cont.tamano[0] - obj.tamano()[0] + 1):
            for j in range(cont.tamano[1] - obj.tamano()[1] + 1):
                if verificarColision(cont, obj, (i, j)):
                    colocarObjeto(cont, obj, (i, j))
                    flag = True
                    break
            if flag:
                break


############################# Heuristica 2 #############################
def heuristica2(cont: Contenedor.Contenedor, objs: list):
    # Se coloca objeto por objeto en el contenedor.
    for obj in objs:
        max = -1
        # Se recorre el contenedor de izq a der, se baja una unidad y se repite.
        for i in range(cont.tamano[0] - obj.tamano()[0] + 1):
            for j in range(cont.tamano[1] - obj.tamano()[1] + 1):
                if verificarColision(cont, obj, (i, j)):
                    contactos = contarContactosObj(cont, obj, (i, j))
                    if max < contactos:
                        max = contactos
                        pos = (i, j)
        colocarObjeto(cont, obj, pos)


############################# Agente #############################
def Agente():
    ConjObjetos = Objetos.crearObjetosRellenoPerfecto(Global.dimContenedor)
    contenedor = Contenedor.Contenedor(Global.dimContenedor)

    heuristica2(contenedor, ConjObjetos)
    print(contenedor.valor)

    """
    SA = SimulatedAnnealing.simulated_annealing(ConjObjetos, 0.05, 0.99, False, readingOrder)  # t0=0.05, alpha=0.99, show=False
    SA.search()
    """

if __name__ == "__main__":
    Agente()
