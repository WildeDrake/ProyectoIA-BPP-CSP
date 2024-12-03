import Contenedor
import Objetos
import movs
import Dibujar
import pygame
import Global

pantalla = 0        # 0 = pantalLa de seleccion de objetos.
                    # 1 = pantalla de colocacion de objetos.
                    # 2 = pantalla de quitar objetos.
contenedor = Contenedor.Contenedor(Global.dimContenedor)
ConjObjetos = Objetos.crearObjetosRellenoPerfecto(Global.dimContenedor)
objetoseleccionado = 0
objeto = ConjObjetos[0]
pos = (0, 0)


def Juego(screen):
    global pantalla
    if pantalla == 3:
        pygame.time.wait(3000)
        return False
    global contenedor
    global ConjObjetos
    global objetoseleccionado
    global objeto
    global pos
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:

            # Ciclo de juego - Seleccionar un objeto.
            if pantalla == 0:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    objetoseleccionado, objeto = movs.Objeto_der(ConjObjetos, objetoseleccionado)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    objetoseleccionado, objeto = movs.Objeto_izq(ConjObjetos, objetoseleccionado)
                elif event.key == pygame.K_r:
                    movs.RotarObjeto(objeto)
                elif event.key == pygame.K_i:
                    movs.InvertirObjeto(objeto)
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    movs.SacarObjeto(ConjObjetos, objetoseleccionado)
                    pantalla = 1
                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                    pantalla = 2

            # Ciclo de juego - Colocar un objeto.
            elif pantalla == 1:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    pos = movs.Mover_der1(contenedor, objeto, pos)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    pos = movs.Mover_izq(pos)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    pos = movs.Mover_arr(pos)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    pos = movs.Mover_aba1(contenedor, objeto, pos)
                elif event.key == pygame.K_r:
                    movs.RotarObjeto(objeto)
                elif event.key == pygame.K_i:
                    movs.InvertirObjeto(objeto)
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if movs.ColocarObjeto(contenedor, objeto, pos):
                        pantalla = 0
                        pos = (0, 0)
                        objetoseleccionado = 0
                        objeto = ConjObjetos[0]
                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                    ConjObjetos.append(objeto)
                    objetoseleccionado = len(ConjObjetos) - 1
                    pantalla = 0
                    pos = (0, 0)

            # Ciclo de juego - Quitar un objeto.
            elif pantalla == 2:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    pos = movs.Mover_der2(contenedor, pos)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    pos = movs.Mover_izq(pos)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    pos = movs.Mover_arr(pos)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    pos = movs.Mover_aba2(contenedor, pos)
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if movs.QuitarObjeto(contenedor, pos, ConjObjetos) == True:
                        pantalla = 0
                        objetoseleccionado = len(ConjObjetos) - 1
                        objeto = ConjObjetos[objetoseleccionado]
                        pos = (0, 0)
                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                    pantalla = 0
                    pos = (0, 0)
                    # Pantalla de victoria.
            if contenedor.valor == Global.area or event.key == pygame.K_o:
                pantalla = 3

    screen.fill((0, 0, 0))
    Dibujar.dibujar_background(screen)
    if pantalla == 0:
        Dibujar.dibujar_contenedor(screen, contenedor)
        Dibujar.dibujar_seleccion(screen, objeto, objetoseleccionado, ConjObjetos, contenedor)
    if pantalla == 1:
        Dibujar.dibujar_contenedor(screen, contenedor)
        Dibujar.dibujar_objeto(screen, objeto, pos)
    if pantalla == 2:
        Dibujar.dibujar_contenedor(screen, contenedor)
        Dibujar.dibujar_delete(screen, pos)
    if pantalla == 3:
        Dibujar.dibujar_win(screen, contenedor)

    return True
