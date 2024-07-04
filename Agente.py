import SimulatedAnnealing
import Contenedor
import Objetos
import Global

# Las heuristicas reciben una lista de objetos en un orden y los colocan uno a uno en el contenedor.
def heuristica1(cont: Contenedor.Contenedor, objs: list):
    for obj in objs:
        pass


############################# Heuristica Diego AAAAAAAA :v #############################

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
                cont.matriz[pos[0] + i][pos[1] + j] = obj.matriz[i][j]
                count += 1
                if count == obj.valor:
                    cont.valor += obj.valor
                    return

def heuristica777(cont: Contenedor.Contenedor, objs: list):
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

########################### Fin Heuristica Diego AAAAAAAA :v ###########################


# Agente
def Agente():
    ConjObjetos = Objetos.crearObjetosRellenoPerfecto(Global.dimContenedor)
    SA = SimulatedAnnealing.simulated_annealing(ConjObjetos, 0.05, 0.99, False, heuristica777)  # t0=0.05, alpha=0.99, show=False
    SA.search()


if __name__ == "__main__":
    Agente()