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

def SeleccionarObjeto():
    pos = (0, 0)


# Para la manipulación de objetos ¿lo podremos hacer en el menu y en la mochila?.
def RotarObjeto(objeto):
    matriz = np.rot90(objeto.matriz, -1)
    objeto.matriz = matriz
    objeto.tamano = objeto.tamano[1], objeto.tamano[0]

def InvertirObjeto(objeto):
    matriz = np.flipiud(objeto.matriz)
    objeto.matriz = matriz

# Para la colocación del objeto en la mochila.
def Mover_izq(mochila, objeto, pos):
    if pos[1] > 0:
        return pos[0], pos[1] - 1
    return pos

def Mover_der(mochila, objeto, pos):
    if pos[1] + objeto.tamano[1] < mochila.tamano[1]:
        return pos[0], pos[1] + 1
    return pos

def Mover_arr(mochila, objeto, pos):
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
    return True

def QuitarObjeto(mochila, pos):
    # Encontrar el objeto.
    id = mochila.matriz[pos[0]][pos[1]]
    # Encontrar el objeto.
    for i in range(mochila.tamano[0]):
        for j in range(mochila.tamano[1]):
            if mochila.matriz[i][j] == id:
                mochila.matriz[i][j] = 0

def VolverAlMenu():
    pass

