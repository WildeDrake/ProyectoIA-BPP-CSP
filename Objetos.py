import random
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
    def __init__(self, id, peso, valor, volumen, color=None):
        super().__init__()
        self.id = id
        self.peso = peso  # Valor numérico.
        self.valor = valor
        if color is None:
            color = (random.randint(100, 255),
                     random.randint(100, 255),
                     random.randint(100, 255))
        matriz = self.ConstruirForma(volumen)  # Crear la forma con volumen cuadraditos.
        self.crear_bloques(matriz, color)  # Crear los bloques del objeto.

    def ConstruirForma(self, volumen):
        lista_cuadrados = []
        lista_posibles_cuadrados = [(0, 0)]
        for _ in range(volumen):
            nuevo_cuadrado = random.choice(lista_posibles_cuadrados)
            lista_cuadrados.append(nuevo_cuadrado)
            while nuevo_cuadrado in lista_posibles_cuadrados:
                lista_posibles_cuadrados.remove(nuevo_cuadrado)
            for c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                vecino = (nuevo_cuadrado[0] + c[0], nuevo_cuadrado[1] + c[1])
                if vecino not in lista_cuadrados:
                    lista_posibles_cuadrados.append(vecino)

        # Naturalizar la lista de cuadrados.
        min_x, min_y = min([c[0] for c in lista_cuadrados]), min([c[1] for c in lista_cuadrados])
        for i in range(len(lista_cuadrados)):
            lista_cuadrados[i] = (lista_cuadrados[i][0] - min_x, lista_cuadrados[i][1] - min_y)

        return lista_cuadrados

    def crear_bloques(self, cuadrados, color):
        for i in range(len(cuadrados)):
            Bloque(cuadrados[i][0], cuadrados[i][1], color, self)

    def mover(self, x, y):
        for bloque in self.sprites():
            bloque.rect.x += x * Global.tmno_cuad
            bloque.rect.y += y * Global.tmno_cuad

    def rotar(self):
        bloque0 = self.sprites()[0].rect.topleft
        for bloque in self.sprites():
            x, y = bloque.rect.topleft
            bloque.rect.topleft = bloque0[0] + bloque0[1] - y, bloque0[1] - bloque0[0] + x





# def CrearObjetos(mochila):
#    id, i = 1, 0
#    ConjObjetos = []
#    while i <= mochila.tamano[0] * mochila.tamano[1]:
#        razonTamano = random.randint(2, mochila.tamano[0] - 1), random.randint(2, mochila.tamano[1] - 1)
#        razonValor = random.randint(1, 100)
#        ConjObjetos.append(Objeto(id, None, razonTamano, razonValor))
#        i += ConjObjetos[id - 1].cuadraditos
#        id += 1
#    for objeto in ConjObjetos:
#        objeto.peso = (mochila.peso // len(ConjObjetos)) + random.randint(-mochila.peso // 5, mochila.peso // 5)
#    return ConjObjetos


def main():
    objeto = Objeto(1, 1, (5, 5), 9)
    for fila in objeto.matriz:
        print(fila)


if __name__ == "__main__":
    main()
