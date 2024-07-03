import SimulatedAnnealing
import Contenedor
import Objetos
import Global

# Variables globales.
contenedor = Contenedor.Contenedor(Global.dimContenedor)
ConjObjetos = Objetos.CrearObjetos(Global.dimContenedor, 16)

# Las heuristicas reciben una lista de objetos en un orden y los colocan uno a uno en el contenedor.
def heuristica1(cont: Contenedor.Contenedor, objs: list):
    for obj in objs:
        pass


# Agente
def Agente():
    global contenedor
    global ConjObjetos

