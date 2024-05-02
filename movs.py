import numpy as np

# Para la selección de objetos.

def Objeto_der(ConjObjetos, id):
    if id == len(ConjObjetos):
        return ConjObjetos[0]
    return ConjObjetos[id+1]

def Objeto_izq(ConjObjetos, id):
    if id == 0:
        return ConjObjetos[len(ConjObjetos)-1]
    return ConjObjetos[id-1]

def SacarObjeto(ConjObjetos, id):
    for objeto in ConjObjetos:
        if objeto.id == id:
            ConjObjetos.remove(objeto)


# Para la manipulación de objetos ¿lo podremos hacer en el menu y en la mochila?.
def RotarObjeto(objeto):
    matriz = np.rot90(objeto.matriz, -1)
    objeto.matriz = matriz
    objeto.tamano = objeto.tamano[1], objeto.tamano[0]

def InvertirObjeto(objeto):
    matriz = np.flipiud(objeto.matriz)
    objeto.matriz = matriz

# Para la colocación del objeto en la mochila.
def Mover_izq(pos):
    if pos[1] > 0:
        return pos[0], pos[1] - 1
    return pos

def Mover_der(mochila, objeto, pos):
    if pos[1] + objeto.tamano[1] < mochila.tamano[1]:
        return pos[0], pos[1] + 1
    return pos

def Mover_arr(pos):
    if pos[0] > 0:
        return pos[0] - 1, pos[1]
    return pos

def Mover_aba(mochila, objeto, pos):
    if pos[0] + objeto.tamano[0] < mochila.tamano[0]:
        return pos[0] + 1, pos[1]
    return pos

def ColocarObjeto(mochila, objeto, pos):
    # Objeto colisiona con otro objeto.
    for i in range(objeto.tamano[0]):
        for j in range(objeto.tamano[1]):
            if mochila.matriz[pos[0] + i][pos[1] + j] != 0:
                return False
    # Colocar el objeto.
    for i in range(objeto.tamano[0]):
        for j in range(objeto.tamano[1]):
            mochila.matriz[pos[0] + i][pos[1] + j] = objeto.id
    mochila.append(objeto)
    return True

def QuitarObjeto(mochila, pos, ConjObjetos):
    # Encontrar el objeto.
    id = mochila.matriz[pos[0]][pos[1]]
    if id == 0:
        return False
    # Quitar matriz del objeto.
    for i in range(mochila.tamano[0]):
        for j in range(mochila.tamano[1]):
            if mochila.matriz[i][j] == id:
                mochila.matriz[i][j] = 0
    # Quitar objeto de la mochila y añadirlo al conjunto.
    for objeto in mochila.objetos:
        if objeto.id == id:
            ConjObjetos.append(mochila.objetos.remove(objeto))
            break
    return True

def VolverAlMenu():
    pass

