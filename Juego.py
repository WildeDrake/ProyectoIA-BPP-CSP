import Contenedor
import Objetos
import movs
import Dibujar
import pygame
import Global

pantalla = 0        # 0 = pantalLa de seleccion de objetos.
                    # 1 = pantalla de colocacion de objetos.
                    # 2 = pantalla de quitar objetos.
contenedor = Contenedor.Contenedor(100, Global.dimContenedor)
ConjObjetos = Objetos.CrearObjetos(Global.dimContenedor, 16,  10)
objetoseleccionado = 0
objeto = ConjObjetos[0]
pos = (0, 0)


def Juego(screen):
    global pantalla
    global contenedor
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
                objetoseleccionado, objeto = movs.Objeto_der(ConjObjetos, objetoseleccionado)
            elif event.type == pygame.K_LEFT or event.type == pygame.K_a:
                objetoseleccionado, objeto = movs.Objeto_izq(ConjObjetos, objetoseleccionado)
            elif event.type == pygame.K_r:
                movs.RotarObjeto(objeto)
            elif event.type == pygame.K_i:
                movs.InvertirObjeto(objeto)
            elif event.type == pygame.K_SPACE or event.type == pygame.K_KP_ENTER:
                movs.SacarObjeto(ConjObjetos, objetoseleccionado)
                pantalla = 1
            elif event.type == pygame.K_ESCAPE or event.type == pygame.K_BACKSPACE:
                pantalla = 2

        # Ciclo de juego - Colocar un objeto.
        elif pantalla == 1:
            if event.type == pygame.KEYRIGHT or event.type == pygame.K_d:
                pos = movs.Mover_der(contenedor, objeto, pos)
            elif event.type == pygame.KEYLEFT or event.type == pygame.K_a:
                pos = movs.Mover_izq(pos)
            elif event.type == pygame.K_UP or event.type == pygame.K_w:
                pos = movs.Mover_arr(pos)
            elif event.type == pygame.K_DOWN or event.type == pygame.K_s:
                pos = movs.Mover_aba(contenedor, objeto, pos)
            elif event.type == pygame.K_r:
                movs.RotarObjeto(objeto)
            elif event.type == pygame.K_i:
                movs.InvertirObjeto(objeto)
            elif event.type == pygame.K_SPACE or event.type == pygame.K_KP_ENTER:
                if movs.ColocarObjeto(contenedor, objeto, pos):
                    pantalla = 0
            elif event.type == pygame.K_ESCAPE or event.type == pygame.K_BACKSPACE:
                ConjObjetos.append(objeto)
                objetoseleccionado = len(ConjObjetos) - 1
                pantalla = 0

        # Ciclo de juego - Quitar un objeto.
        elif pantalla == 2:
            if event.type == pygame.KEYRIGHT or event.type == pygame.K_d:
                pos = movs.Mover_der(contenedor, objeto, pos)
            elif event.type == pygame.KEYLEFT or event.type == pygame.K_a:
                pos = movs.Mover_izq(pos)
            elif event.type == pygame.K_UP or event.type == pygame.K_w:
                pos = movs.Mover_arr(pos)
            elif event.type == pygame.K_DOWN or event.type == pygame.K_s:
                pos = movs.Mover_aba(contenedor, objeto, pos)
            elif event.type == pygame.K_SPACE or event.type == pygame.K_KP_ENTER:
                if movs.QuitarObjeto(contenedor, pos, ConjObjetos) == True:
                    pantalla = 0
                    objetoseleccionado = len(ConjObjetos) - 1
                    objeto = ConjObjetos[objetoseleccionado]
            elif event.type == pygame.K_ESCAPE or event.type == pygame.K_BACKSPACE:
                pantalla = 0
    Dibujar.dibujar_contenedor(screen, contenedor)
    Dibujar.dibujar_flechas(screen)
    Dibujar.dibujar_objeto(screen, objeto, pos)
    return True

def main():
    pygame.init()
    screen = pygame.display.set_mode((Global.WIDTH, Global.HEIGHT))
    pygame.display.set_caption("Proyecto de objetos")
    clock = pygame.time.Clock()
    running = True

    movs.ColocarObjeto(contenedor, ConjObjetos[0], (0, 0))

    while running:
        screen.fill((0, 0, 0))
        running = Juego(screen)
        pygame.display.flip()
        clock.tick(60)
        print("\rPantalla: " + str(pantalla), end="")
    pygame.quit()

if __name__ == "__main__":
    main()
