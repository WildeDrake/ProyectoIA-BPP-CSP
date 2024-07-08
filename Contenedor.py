import Objetos


class Contenedor:
    def __init__(self, tamano):
        self.tamano = tamano  # tamano es un 2-tupla (x,y)(en cuadraditos).}}
        self.matriz = []  # Crear una matriz de tamano[0] x tamano[1].
        for i in range(tamano[0]):  # Rellenar toda la matriz con 0.
            self.matriz.append([])
            for j in range(tamano[1]):
                self.matriz[i].append(0)
        self.objetos = []  # Lista de objetos en el contenedor.
        self.valor = 0  # Valor total de los objetos en el contenedor.
        self.listCont = None  # Lista de cuadrados que estan en contacto con el borde o un objeto.

    def empezarListaContactos(self):
        if self.listCont is None:
            self.listCont = [(0, i) for i in range(self.tamano[1])] \
                            + [(self.tamano[0] - 1, i) for i in range(self.tamano[1])] \
                            + [(i, 0) for i in range(self.tamano[0])] \
                            + [(i, self.tamano[1] - 1) for i in range(self.tamano[0])]

        # solo en caso de que ya existan objetos en el contenedor, se escanea la matris completa
        if len(self.objetos) > 0 or self.valor > 0:
            for i in range(self.tamano[0]):
                for j in range(self.tamano[1]):
                    if self.matriz[i][j] != 0:
                        for ay, ax in [(j + 1, i), (j - 1, i), (j, i + 1), (j, i - 1)]:
                            if (ay, ax) not in self.listCont and 0 <= ay < self.tamano[1] \
                                    and 0 <= ax < self.tamano[0] and self.matriz[ax][ay] == 0:
                                self.listCont.append((ay, ax))

    def colocarObjeto(self, obj: Objetos.Objeto, pos: tuple):
        self.valor += obj.valor
        if obj.listColis is None:
            obj.crearListaColision()
        if self.listCont is None:
            self.empezarListaContactos()
        for x, y in obj.listColis:
            self.matriz[x + pos[0]][y + pos[1]] = obj.id
            if (x + pos[0], y + pos[1]) in self.listCont:
                self.listCont.remove((x + pos[0], y + pos[1]))
            for ay, ax in [(y + pos[1] + 1, x + pos[0]), (y + pos[1] - 1, x + pos[0]),
                           (y + pos[1], x + pos[0] + 1), (y + pos[1], x + pos[0] - 1)]:
                if (ay, ax) not in self.listCont and 0 <= ay < self.tamano[1] \
                        and 0 <= ax < self.tamano[0] and self.matriz[ax][ay] == 0:
                    self.listCont.append((ay, ax))

    def contarContactosConLista(self, obj: Objetos.Objeto, pos: tuple):
        if obj.listColis is None:
            obj.crearListaColision()
        if self.listCont is None:
            self.empezarListaContactos()
        count = 0
        for x, y in obj.listColis:
            if (x + pos[0], y + pos[1]) in self.listCont:
                count += 1

        return count