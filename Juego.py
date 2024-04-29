import Mochila
import Objetos
import movs
import Controles
import random

def Juego():
    mochila = Mochila.Mochila(100, (6, 6))
    ConjObjetos = CrearObjetos(mochila)
    # Ciclo de juego
    while True:
        # Ciclo de juego - Seleccionar un objeto.
        waaa = True
        while True:
            objetoseleccionado = 0
            while True:
                if Controles.controles() == "derecha":
                    objeto = movs.Objeto_der(ConjObjetos, objetoseleccionado)
                elif Controles.controles() == "izquierda":
                    objeto = movs.Objeto_izq(ConjObjetos, objetoseleccionado)
                elif Controles.controles() == "rotar":
                    movs.RotarObjeto(objeto)
                elif Controles.controles() == "invertir":
                    movs.InvertirObjeto(objeto)
                elif Controles.controles() == "seleccionar":
                    movs.SacarObjeto(ConjObjetos, objeto.id)
                    waaa = True
                    break
                elif Controles.controles() == "retroceder":
                    waaa = False
                    break
            pos = 0, 0
            # Ciclo de juego - Colocar un objeto.
            if waaa is True:
                while True:
                    if Controles.controles() == "derecha":
                        pos = movs.Mover_der(mochila, objeto, pos)
                    elif Controles.controles() == "izquierda":
                        pos = movs.Mover_izq(pos)
                    elif Controles.controles() == "arriba":
                        pos = movs.Mover_arr(pos)
                    elif Controles.controles() == "abajo":
                        pos = movs.Mover_aba(mochila, objeto, pos)
                    elif Controles.controles() == "rotar":
                        movs.RotarObjeto(objeto)
                    elif Controles.controles() == "invertir":
                        movs.InvertirObjeto(objeto)
                    elif Controles.controles() == "seleccionar":
                        if movs.ColocarObjeto(mochila, objeto, pos):
                            break
                    elif Controles.controles() == "retroceder":
                        ConjObjetos.append(objeto)
                        break
            # Ciclo de juego - Quitar un objeto.
            else:
                while True:
                    if Controles.controles() == "derecha":
                        pos = movs.Mover_der(mochila, objeto, pos)
                    elif Controles.controles() == "izquierda":
                        pos = movs.Mover_izq(pos)
                    elif Controles.controles() == "arriba":
                        pos = movs.Mover_arr(pos)
                    elif Controles.controles() == "abajo":
                        pos = movs.Mover_aba(mochila, objeto, pos)
                    elif Controles.controles() == "seleccionar":
                        movs.QuitarObjeto(mochila, pos, ConjObjetos)
                        break
                    elif Controles.controles() == "retroceder":
                        break






def CrearObjetos(mochila):
    id , i = 1 , 0
    ConjObjetos = []
    while i <= mochila.tamano[0] * mochila.tamano[1]:
        razonTamano = random.randint(2, mochila.tamano[0]-1), random.randint(2, mochila.tamano[1]-1)
        razonValor = random.randint(1, 100)
        ConjObjetos.append( Objetos.Objeto(id, None, razonTamano, razonValor) )
        i += ConjObjetos[id-1].cuadraditos
        id += 1
    for objeto in ConjObjetos:
        objeto.peso = (mochila.peso//len(ConjObjetos)) + random.randint(-mochila.peso//5, mochila.peso//5)
    return ConjObjetos




