import Mochila
import Objetos
import movs
import Dibujar
import pygame
import Global

pantalla = 0        # 0 = pantalLa de seleccion de objetos.
                    # 1 = pantalla de colocacion de objetos.
                    # 2 = pantalla de quitar objetos.
mochila = Mochila.Mochila(100, Global.DimMochila)
ConjSprites = Objetos.CrearObjetos((6,6),10)
ConjObjetos = ConjSprites.sprites()
objetoseleccionado = 0
objeto = ConjObjetos[0]
pos = (0, 0)


def Juego(screen):
    global pantalla
    global mochila
    global ConjObjetos
    global objetoseleccionado
    global objeto
    global pos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        # Ciclo de juego - Seleccionar un objeto.
        if pantalla == 0:
            if event.type == pygame.K_RIGHT or event.type == pygame.K_d:
                objeto = movs.Objeto_der(ConjObjetos, objetoseleccionado)
            elif event.type == pygame.K_LEFT or event.type == pygame.K_a:
                objeto = movs.Objeto_izq(ConjObjetos, objetoseleccionado)
            elif event.type == pygame.K_r:
                movs.RotarObjeto(objeto)
            elif event.type == pygame.K_i:
                movs.InvertirObjeto(objeto)
            elif event.type == pygame.K_SPACE or event.type == pygame.K_KP_ENTER:
                movs.SacarObjeto(ConjObjetos, objeto.id)
                pantalla = 1
            elif event.type == pygame.K_ESCAPE or event.type == pygame.K_BACKSPACE:
                pantalla = 2

        # Ciclo de juego - Colocar un objeto.
        elif pantalla == 1:
            if event.type == pygame.KEYRIGHT or event.type == pygame.K_d:
                pos = movs.Mover_der(mochila, objeto, pos)
            elif event.type == pygame.KEYLEFT or event.type == pygame.K_a:
                pos = movs.Mover_izq(pos)
            elif event.type == pygame.K_UP or event.type == pygame.K_w:
                pos = movs.Mover_arr(pos)
            elif event.type == pygame.K_DOWN or event.type == pygame.K_s:
                pos = movs.Mover_aba(mochila, objeto, pos)
            elif event.type == pygame.K_r:
                movs.RotarObjeto(objeto)
            elif event.type == pygame.K_i:
                movs.InvertirObjeto(objeto)
            elif event.type == pygame.K_SPACE or event.type == pygame.K_KP_ENTER:
                if movs.ColocarObjeto(mochila, objeto, pos):
                    pantalla = 0
            elif event.type == pygame.K_ESCAPE or event.type == pygame.K_BACKSPACE:
                ConjObjetos.append(objeto)
                pantalla = 0

        # Ciclo de juego - Quitar un objeto.
        elif pantalla == 2:
            if event.type == pygame.KEYRIGHT or event.type == pygame.K_d:
                pos = movs.Mover_der(mochila, objeto, pos)
            elif event.type == pygame.KEYLEFT or event.type == pygame.K_a:
                pos = movs.Mover_izq(pos)
            elif event.type == pygame.K_UP or event.type == pygame.K_w:
                pos = movs.Mover_arr(pos)
            elif event.type == pygame.K_DOWN or event.type == pygame.K_s:
                pos = movs.Mover_aba(mochila, objeto, pos)
            elif event.type == pygame.K_SPACE or event.type == pygame.K_KP_ENTER:
                if movs.QuitarObjeto(mochila, pos, ConjObjetos) == True:
                    pantalla = 0
            elif event.type == pygame.K_ESCAPE or event.type == pygame.K_BACKSPACE:
                pantalla = 0
    Dibujar.dibujar_mochila(screen, mochila)
    Dibujar.dibujar_menu(screen)
    Dibujar.dibujar_objeto(screen, objeto)
    return True
