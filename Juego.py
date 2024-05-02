import Mochila
import Objetos
import movs
import Controles
import Dibujar
import random

pantalla = 0        # 0 = pantalLa de seleccion de objetos.
                    # 1 = pantalla de colocacion de objetos.
                    # 2 = pantalla de quitar objetos.
mochila = Mochila.Mochila(100, (6, 6))
ConjObjetos = Objetos.CrearObjetos(mochila)
objetoseleccionado = 0
objeto = ConjObjetos[0]
pos = (0, 0)


def Juego(screen):
    global pantalla
    global mochila
    global ConjObjetos
    global objetoseleccionado
    global objeto
    global pos

    # Ciclo de juego - Seleccionar un objeto.
    if pantalla == 0:
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
            pantalla = 1
        elif Controles.controles() == "retroceder":
            pantalla = 2

    # Ciclo de juego - Colocar un objeto.
    elif pantalla == 1:
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
                pantalla = 0
        elif Controles.controles() == "retroceder":
            ConjObjetos.append(objeto)
            pantalla = 0

    # Ciclo de juego - Quitar un objeto.
    elif pantalla == 2:
        if Controles.controles() == "derecha":
            pos = movs.Mover_der(mochila, objeto, pos)
        elif Controles.controles() == "izquierda":
            pos = movs.Mover_izq(pos)
        elif Controles.controles() == "arriba":
            pos = movs.Mover_arr(pos)
        elif Controles.controles() == "abajo":
            pos = movs.Mover_aba(mochila, objeto, pos)
        elif Controles.controles() == "seleccionar":
            if movs.QuitarObjeto(mochila, pos, ConjObjetos) == True:
                pantalla = 0
        elif Controles.controles() == "retroceder":
            pantalla = 0
