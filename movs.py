import numpy as np
import pygame
import Objetos


# Para la manipulación de objetos en cualquier pantalla.
def RotarObjeto(objeto):
    matriz = np.rot90(objeto.matriz, -1)
    objeto.matriz = matriz


def InvertirObjeto(objeto):
    matriz = np.flip(objeto.matriz, 1)
    objeto.matriz = matriz


# Para la selección de objetos (pantalla == 0).

def Objeto_der(ConjObjetos, objetoSeleccionado):
    if objetoSeleccionado == len(ConjObjetos) - 1:
        return 0, ConjObjetos[0]
    return objetoSeleccionado + 1, ConjObjetos[objetoSeleccionado + 1]


def Objeto_izq(ConjObjetos, objetoSeleccionado):
    if objetoSeleccionado == 0:
        return len(ConjObjetos) - 1, ConjObjetos[len(ConjObjetos) - 1]
    return objetoSeleccionado - 1, ConjObjetos[objetoSeleccionado - 1]


def SacarObjeto(ConjObjetos, objetoSeleccionado):
    ConjObjetos.remove(ConjObjetos[objetoSeleccionado])


# Para manipulacion en contenedor (pantalla == 1 o pantalla == 2).

def Mover_izq(pos):
    if pos[1] > 0:
        return pos[0], pos[1] - 1
    return pos

def Mover_der1(contenedor, objeto, pos):
    if pos[1] + objeto.tamano()[1] < contenedor.tamano[1]:
        return pos[0], pos[1] + 1
    return pos
def Mover_der2(contenedor, pos):
    if pos[1] + 1 < contenedor.tamano[1]:
        return pos[0], pos[1] + 1
    return pos


def Mover_arr(pos):
    if pos[0] > 0:
        return pos[0] - 1, pos[1]
    return pos


def Mover_aba1(contenedor, objeto, pos):
    if pos[0] + objeto.tamano()[0] < contenedor.tamano[0]:
        return pos[0] + 1, pos[1]
    return pos
def Mover_aba2(contenedor, pos):
    if pos[0] + 1 < contenedor.tamano[0]:
        return pos[0] + 1, pos[1]
    return pos


# Para la colocación del objeto en el contenedor (pantalla == 1).

def ColocarObjeto(contenedor, objeto, pos):
    # Objeto colisiona con otro objeto.
    for i in range(objeto.tamano()[0]):
        for j in range(objeto.tamano()[1]):
            if objeto.matriz[i][j] != 0 and contenedor.matriz[pos[0] + i][pos[1] + j] != 0:
                return False
    # Colocar el objeto.
    for i in range(objeto.tamano()[0]):
        for j in range(objeto.tamano()[1]):
            if objeto.matriz[i][j] != 0:
                contenedor.matriz[pos[0] + i][pos[1] + j] = objeto.matriz[i][j]
    contenedor.objetos.append(objeto)
    contenedor.valor += objeto.valor
    return True


# Para quitar objeto del contenedor (pantalla == 2).

def QuitarObjeto(contenedor, pos, ConjObjetos):
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
            ConjObjetos.append(aux)
            break
    return True


def VolverAlMenu():
    pass

