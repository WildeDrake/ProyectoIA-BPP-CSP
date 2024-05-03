import random
import math
import pygame
import Global


class Objeto(pygame.sprite.Sprite):
    def __init__(self, id, peso, valor, volumen, tmno_max=(1000, 1000), color=None):
        super().__init__()
        self.id = id
        self.peso = peso  # Valor numérico.
        self.valor = valor
        if color is None:
            color = (random.randint(100, 255),
                     random.randint(100, 255),
                     random.randint(100, 255))
        self.color = color
        # Crear la forma con volumen cuadraditos.
        self.matriz = self.ConstruirMatriz(volumen, tmno_max)
        self.image = pygame.Surface((len(self.matriz[0]) * Global.tmno_cuad,
                                     len(self.matriz) * Global.tmno_cuad))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(topleft=(200, 200))
        self.update()

    def ConstruirMatriz(self, volumen, tmno_max):  # metodo feo y penca
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

        # crear matriz a partir de puntos
        min_x = min([c[0] for c in lista_cuadrados])
        max_x = max([c[0] for c in lista_cuadrados])
        min_y = min([c[1] for c in lista_cuadrados])
        max_y = max([c[1] for c in lista_cuadrados])
        matriz = [[0 for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
        for c in lista_cuadrados:
            matriz[c[1] - min_y][c[0] - min_x] = self.id

        return matriz

    def update(self):
        super().update()
        self.rect.size = (len(self.matriz[0]) * Global.tmno_cuad,
                            len(self.matriz) * Global.tmno_cuad)
        self.image.fill((0, 0, 0, 0))  # fondo transparente
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                if self.matriz[i][j] != 0:
                    pygame.draw.rect(self.image, self.color,
                                     (j * Global.tmno_cuad, i * Global.tmno_cuad,
                                      Global.tmno_cuad, Global.tmno_cuad))


def CrearObjetos(tmno_max, n_objetos):
    volums = [math.ceil(random.triangular(1, tmno_max[0] * tmno_max[1] / 16, 4)) for _ in range(n_objetos)]
    print(tmno_max[0] * tmno_max[1] / 4)
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
        obj.mover(sum, 0)
        sum += obj.get_size()[0] // Global.tmno_cuad + 1
        obj.draw(screen)
    pygame.display.flip()
    pygame.time.wait(10000)  #


if __name__ == "__main__":
    main()
