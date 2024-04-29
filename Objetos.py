import random


class Objeto:
    def __init__(self, id, peso, tamano, valor):
        self.id = id
        self.peso = peso                    # Valor númerico.
        self.tamano = tamano                # Tamano es un 2-tupla (x,y)(en cuadraditos).
        self.cuadraditos = 0                # Número de Casillas que ocupa en la matriz.
        self.valor = valor
        self.matriz = []
        self.ConstruirMatriz()

    def ConstruirMatriz(self):
        # Rellenar toda la matriz con 0.
        for i in range(self.tamano[0]):
            self.matriz.append([])
            for j in range(self.tamano[1]):
                self.matriz[i].append(0)
        # Rellenar el espacio que ocupa de la matriz.
        pos = self.tamano[0] // 2, self.tamano[1] // 2
        # Inicializar un conjunto para almacenar los bordes que ya se han tocado.
        contBordes = set()
        # El while para si estan rellenas las ambas esquinas contrarias.
        while len(contBordes) < 4:
            # Si la posición esta vacia, rellenarla.
            if self.matriz[pos[0]][pos[1]] == 0:
                self.matriz[pos[0]][pos[1]] = self.id
                self.cuadraditos += 1
            # Verificar si la posición actual está en un borde y, de ser así, añadir ese borde al conjunto.
            if pos[0] == 0:
                contBordes.add('arriba')
            elif pos[0] == self.tamano[0] - 1:
                contBordes.add('abajo')
            if pos[1] == 0:
                contBordes.add('izquierda')
            elif pos[1] == self.tamano[1] - 1:
                contBordes.add('derecha')
            aux = random.randint(0, 3)
            if aux == 0:  # arriba
                if pos[0] > 0:
                    pos = pos[0] - 1, pos[1]
            elif aux == 1:  # abajo
                if pos[0] < self.tamano[0] - 1:
                    pos = pos[0] + 1, pos[1]
            elif aux == 2:  # izquierda
                if pos[1] > 0:
                    pos = pos[0], pos[1] - 1
            elif aux == 3:  # derecha
                if pos[1] < self.tamano[1] - 1:
                    pos = pos[0], pos[1] + 1