import numpy as np
import pygame
import Objetos


# Para la selección de objetos.

def Objeto_der(ConjObjetos, objetoSeleccionado):
    if objetoSeleccionado == len(ConjObjetos):
        return ConjObjetos[0]
    return objetoSeleccionado + 1, ConjObjetos[objetoSeleccionado + 1]


def Objeto_izq(ConjObjetos, objetoSeleccionado):
    if objetoSeleccionado == 0:
        return ConjObjetos[len(ConjObjetos) - 1]
    return objetoSeleccionado - 1, ConjObjetos[objetoSeleccionado - 1]


def SacarObjeto(ConjObjetos, objetoSeleccionado):
    ConjObjetos.remove(objetoSeleccionado)


# Para la manipulación de objetos ¿lo podremos hacer en el menu y en el contenedor?.
def RotarObjeto(objeto):
    matriz = np.rot90(objeto.matriz, -1)
    objeto.matriz = matriz


def InvertirObjeto(objeto):
    matriz = np.flipiud(objeto.matriz)
    objeto.matriz = matriz


# Para la colocación del objeto en la contenedor.
def Mover_izq(pos):
    if pos[1] > 0:
        return pos[0], pos[1] - 1
    return pos


def Mover_der(contenedor, objeto, pos):
    if pos[1] + objeto.tamano()[1] < contenedor.tamano[1]:
        return pos[0], pos[1] + 1
    return pos


def Mover_arr(pos):
    if pos[0] > 0:
        return pos[0] - 1, pos[1]
    return pos


def Mover_aba(contenedor, objeto, pos):
    if pos[0] + objeto.tamano()[0] < contenedor.tamano[0]:
        return pos[0] + 1, pos[1]
    return pos


def ColocarObjeto(contenedor, objeto, pos):
    # Objeto colisiona con otro objeto.
    for i in range(objeto.tamano()[0]):
        for j in range(objeto.tamano()[1]):
            if contenedor.matriz[pos[0] + i][pos[1] + j] != 0:
                return False
    # Colocar el objeto.
    for i in range(objeto.tamano()[0]):
        for j in range(objeto.tamano()[1]):
            contenedor.matriz[pos[0] + i][pos[1] + j] = objeto.matriz[i][j]
    contenedor.objetos.append(objeto)
    return True


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
            ConjObjetos.append(contenedor.objetos.remove(objeto))
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
