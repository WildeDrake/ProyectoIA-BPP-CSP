import random
import math
import pygame

import Global
import Mochila


class Bloque(pygame.sprite.Sprite):
    def __init__(self, x, y, color, group):
        super().__init__(group)
        self.image = pygame.Surface((Global.tmno_cuad, Global.tmno_cuad))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x * Global.tmno_cuad, y * Global.tmno_cuad))


class Objeto(pygame.sprite.Group):
    def __init__(self, id, peso, valor, volumen, tmno_max=(1000, 1000), color=None):
        super().__init__()
        self.id = id
        self.peso = peso  # Valor numérico.
        self.valor = valor
        if color is None:
            color = (random.randint(100, 255),
                     random.randint(100, 255),
                     random.randint(100, 255))
        matriz = self.ConstruirForma(volumen, tmno_max)  # Crear la forma con volumen cuadraditos.
        self.crear_bloques(matriz, color)  # Crear los bloques del objeto.

    def ConstruirForma(self, volumen, tmno_max):
        tmno_max = (tmno_max[0] // 2, tmno_max[1] // 2)  # dividir por 2, más facil de manejar
        lista_cuadrados = []  # Lista de cuadrados que forman el objeto.
        lista_posibles_cuadrados = [(0, 0)]  # Lista de cuadrados que pueden ser añadidos.
        for _ in range(volumen):
            # Elegir un cuadrado aleatorio.
            nuevo_cuadrado = random.choice(lista_posibles_cuadrados)
            lista_cuadrados.append(nuevo_cuadrado)
            while nuevo_cuadrado in lista_posibles_cuadrados:
                lista_posibles_cuadrados.remove(nuevo_cuadrado)
            # Añadir los cuadrados adyacentes al nuevo cuadrado.
            for c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                vecino = (nuevo_cuadrado[0] + c[0], nuevo_cuadrado[1] + c[1])
                if (vecino not in lista_cuadrados
                        and -tmno_max[0] <= vecino[0] <= tmno_max[0]
                        and -tmno_max[1] <= vecino[1] <= tmno_max[1]):
                    lista_posibles_cuadrados.append(vecino)

        # Naturalizar la lista de cuadrados.
        min_x, min_y = min([c[0] for c in lista_cuadrados]), min([c[1] for c in lista_cuadrados])
        for i in range(len(lista_cuadrados)):
            lista_cuadrados[i] = (lista_cuadrados[i][0] - min_x, lista_cuadrados[i][1] - min_y)

        return lista_cuadrados

    def crear_bloques(self, cuadrados, color):
        for i in range(len(cuadrados)):
            Bloque(cuadrados[i][0], cuadrados[i][1], color, self)

    # tamaño del objeto
    def __get_width(self):
        return (max([bloque.rect.x for bloque in self.sprites()])
                - min([bloque.rect.x for bloque in self.sprites()]))

    def __get_height(self):
        return (max([bloque.rect.y for bloque in self.sprites()])
                - min([bloque.rect.y for bloque in self.sprites()]))

    def get_size(self):
        return self.__get_width(), self.__get_height()

    # posicion global del objeto
    def __get_x(self):
        return min([bloque.rect.x for bloque in self.sprites()])

    def __get_y(self):
        return min([bloque.rect.y for bloque in self.sprites()])

    def get_pos(self):
        return self.__get_x(), self.__get_y()

    def mover(self, x, y):
        for bloque in self.sprites():
            bloque.rect.x += x * Global.tmno_cuad
            bloque.rect.y += y * Global.tmno_cuad

    def rotar(self):
        bloque0 = self.sprites()[0].rect.topleft
        for bloque in self.sprites():
            x, y = bloque.rect.topleft
            bloque.rect.topleft = bloque0[0] + bloque0[1] - y, bloque0[1] - bloque0[0] + x


def CrearObjetos(tmno_max, n_objetos):
    volums = [math.ceil(random.triangular(1,tmno_max[0]*tmno_max[1]/16,4)) for _ in range(n_objetos)]
    print(tmno_max[0]*tmno_max[1]/4)
    print(volums)

    objetos = []
    for i in range(n_objetos):
        objetos.append(Objeto(i, 1, 1, volums[i], tmno_max))

    return objetos


#################### TEST ####################
def main():
    WIDTH, HEIGHT = 400, 400
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('generator test')
    objs = CrearObjetos((20, 20), 100)

    sum = 0
    for obj in objs:
        obj.mover(sum,0)
        sum += obj.get_size()[0] //Global.tmno_cuad + 1
        obj.draw(screen)
    pygame.display.flip()
    pygame.time.wait(10000) #


if __name__ == "__main__":
    main()
