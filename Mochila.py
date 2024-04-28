import Objetos
import random


class Mochila:
    def __init__(self, peso, tamano):
        self.peso = peso                    # valor númerico.
        self.tamano = tamano                # tamano es un 2-tupla (x,y)(en cuadraditos).}}
        self.matriz = []                    # Crear una matriz de tamano[0] x tamano[1].
        for i in range(tamano[0]):          # Rellenar toda la matriz con 0.
            self.matriz.append([])
            for j in range(tamano[1]):
                self.matriz[i].append(0)
        self.ConjObjetos = []

    def CrearObjetos(self):
        self.ConjObjetos.clear()
        id , i = 1 , 0
        while i <= self.tamano[0] * self.tamano[1]:
            razonTamano = self.tamano[0] // random.randint(1, self.tamano[0]), self.tamano[1] // random.randint(1, self.tamano[1])
            razonPeso = self.peso // random.randint(1, self.peso-1)
            razonValor = random.randint(1, 100)
            self.ConjObjetos.append( Objetos.Objeto(id, razonPeso, razonTamano, razonValor) )
            i += self.ConjObjetos[id].cuadraditos
            id += 1
