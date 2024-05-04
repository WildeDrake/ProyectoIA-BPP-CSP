import numpy as np
import pygame
import Objetos


# Para la selección de objetos.

def Objeto_der(ConjObjetos, objetoSeleccionado):
    if objetoSeleccionado == len(ConjObjetos):
        return ConjObjetos[0]
    return ConjObjetos[objetoSeleccionado + 1]


def Objeto_izq(ConjObjetos, objetoSeleccionado):
    if objetoSeleccionado == 0:
        return ConjObjetos[len(ConjObjetos) - 1]
    return ConjObjetos[objetoSeleccionado - 1]


def SacarObjeto(ConjObjetos, id):
    for objeto in ConjObjetos:
        if objeto.id == id:
            ConjObjetos.remove(objeto)


# Para la manipulación de objetos ¿lo podremos hacer en el menu y en la mochila?.
def RotarObjeto(objeto):
    matriz = np.rot90(objeto.matriz, -1)
    objeto.matriz = matriz
    # objeto.tamano = objeto.tamano[1], objeto.tamano[0]


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


def main():
    pygame.init()
    screen = pygame.display.set_mode((1800, 900))
    pygame.display.set_caption('test')
    objs = Objetos.CrearObjetos((20, 20), 1)
    objs.sprites()[0].rect.topleft = (100, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    RotarObjeto(objs[0])
                    objs[0].update()
                if event.key == pygame.K_ESCAPE:
                    return False
        screen.fill((0, 0, 0))
        objs.draw(screen)
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
