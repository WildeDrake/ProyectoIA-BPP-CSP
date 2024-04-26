# -*- coding: utf-8 -*-         # Pa poder poner ñ lol

class Objeto:
    def __init__(self, peso, tamano, valor):
        self.peso = peso                    # Valor númerico.
        self.tamano = tamano                # Tamano es un 2-tupla (x,y)(en cuadraditos).
        self.valor = valor

class Mochila:
    def __init__(self, peso, tamano):
        self.peso = peso                    # valor númerico.
        self.tamano = tamano                # tamano es un 2-tupla (x,y)(en cuadraditos).
