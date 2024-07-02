import Contenedor
import Objetos
import Global

# Variables globales.
contenedor = Contenedor.Contenedor(Global.dimContenedor)
ConjObjetos = Objetos.CrearObjetos(Global.dimContenedor, 16)



class Esquinas:
    def __init__(self):
        # Esquinas del contenedor.
        self.supIzqEx = [(0, 0)]
        self.supDerEx = [(Global.dimContenedor[0]-1, 0)]
        self.infIzqEx = [(0, Global.dimContenedor[1]-1)]
        self.infDerEx = [(Global.dimContenedor[0]-1, Global.dimContenedor[1]-1)]
        # Esquinas de objetos.
        self.supIzqIn = []
        self.supDerIn = []
        self.infIzqIn = []
        self.infDerIn = []


# Agente 1
esquinas = []
def Agente1():
    global contenedor
    global ConjObjetos
    global esquinas

    esquinas = Esquinas()




