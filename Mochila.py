# -*- coding: utf-8 -*-         # Pa poder poner ñ lol

class Objeto:
    def _init_(self, peso, tamano):
        self.peso = peso                    # Valor númerico.
        self.tamano = tamano                # Tamano es un 2-tupla (x,y)(en cm).
        self.area = tamano.x * tamano.y     # Volumen en cm^2.

class Mochila:
    def _init_(self, peso, tamano):
        self.peso = peso                    # valor númerico.
        self.tamano = tamano                # tamano es un 2-tupla (x,y).
        self.area = tamano.x * tamano.y     # Volumen en cm^2.
