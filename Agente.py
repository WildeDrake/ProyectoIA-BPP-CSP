import SimulatedAnnealing
import Contenedor
import Objetos
import Global


####################### Funciones utilizadas por las heuristicas #######################
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
def heuristica2():

    pass




############################# Agente #############################
def Agente():
    ConjObjetos = Objetos.crearObjetosRellenoPerfecto(Global.dimContenedor)
    contenedor = Contenedor.Contenedor(Global.dimContenedor)

    readingOrder(contenedor, ConjObjetos)
    print(contenedor.valor)
    """
    SA = SimulatedAnnealing.simulated_annealing(ConjObjetos, 0.05, 0.99, False, readingOrder)  # t0=0.05, alpha=0.99, show=False
    SA.search()
    """

if __name__ == "__main__":
    Agente()
