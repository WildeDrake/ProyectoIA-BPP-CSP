class Contenedor:
    def __init__(self, peso, tamano):
        self.tamano = tamano                # tamano es un 2-tupla (x,y)(en cuadraditos).}}
        self.matriz = []                    # Crear una matriz de tamano[0] x tamano[1].
        for i in range(tamano[0]):          # Rellenar toda la matriz con 0.
            self.matriz.append([])
            for j in range(tamano[1]):
                self.matriz[i].append(0)
        self.objetos = []                   # Lista de objetos en el contenedor.
        self.valor = 0                      # Valor total de los objetos en el contenedor.