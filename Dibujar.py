import pygame
import Global
import Objetos


def dibujar_contenedor(screen, contenedor):
    for i in range(contenedor.tamano[0]):
        for j in range(contenedor.tamano[1]):
            if contenedor.matriz[i][j] == 0:
                pygame.draw.rect(screen, (0, 0, 0),
                                 (j * (Global.tamCasillas - 1) + Global.WIDTH // 24,
                                  i * (Global.tamCasillas - 1) + Global.HEIGHT / 20,
                                  Global.tamCasillas, Global.tamCasillas))
            else:
                pygame.draw.rect(screen,
                                 Objetos.findInList(contenedor.objetos, contenedor.matriz[i][j]).color,
                                 (j * (Global.tamCasillas - 1) + Global.WIDTH // 24,
                                  i * (Global.tamCasillas - 1) + Global.HEIGHT / 20,
                                  Global.tamCasillas, Global.tamCasillas))
            pygame.draw.rect(screen, (255, 255, 255),
                             (j * (Global.tamCasillas - 1) + Global.WIDTH // 24,
                              i * (Global.tamCasillas - 1) + Global.HEIGHT / 20,
                              Global.tamCasillas, Global.tamCasillas), 1)





def dibujar_seleccion(screen, objeto, objetoSeleccionado, conjObjetos):
    # Flechas de selección.
    left = pygame.image.load("src/left.png")
    right = pygame.image.load("src/right.png")
    left = pygame.transform.scale(left, (Global.WIDTH // 18, Global.HEIGHT // 10))
    right = pygame.transform.scale(right, (Global.WIDTH // 18, Global.HEIGHT // 10))
    screen.blit(left, (Global.WIDTH // 1.8, Global.HEIGHT // 2))
    screen.blit(right, (Global.WIDTH * 0.93, Global.HEIGHT // 2))
    # Objeto seleccionado.
    for i in range(objeto.tamano()[0]):
        for j in range(objeto.tamano()[1]):
            if objeto.matriz[i][j] != 0:
                pygame.draw.rect(screen, objeto.color,(j * (Global.tamCasillas - 1) + Global.WIDTH // 1.4, i * (Global.tamCasillas - 1) + Global.HEIGHT // 2, Global.tamCasillas, Global.tamCasillas))
    # Valor del objeto.
    font = pygame.font.Font(None, 36)
    text = font.render("Peso: " + str(objeto.peso) + "         Valor: " + str(objeto.valor), True, (255, 255, 255))
    screen.blit(text, (Global.WIDTH // 1.45, Global.HEIGHT // 1.1))
    text = font.render(str(objetoSeleccionado+1) + " / " + str(len(conjObjetos)), True, (255, 255, 255))
    screen.blit(text, (Global.WIDTH // 1.34, Global.HEIGHT // 2.3))
    font = pygame.font.Font(None, 25)
    text = font.render(" r - rotar  |  i - invertir  |  espacio/enter - ""seleccionar objeto  |  escape/backspace - quitar objetos", True, (255, 255, 255))
    screen.blit(text, (Global.WIDTH // 1.8, Global.HEIGHT // 5))


def dibujar_objeto(screen, objeto, pos):
    for i in range(objeto.tamano()[0]):
        for j in range(objeto.tamano()[1]):
            if objeto.matriz[i][j] != 0:
                pygame.draw.rect(screen, objeto.color,
                                 ((pos[1] + j) * (Global.tamCasillas - 1) + Global.WIDTH // 24,
                                  (pos[0] + i) * (Global.tamCasillas - 1) + Global.HEIGHT / 20,
                                  Global.tamCasillas, Global.tamCasillas))
                pygame.draw.rect(screen, (255, 255, 255),
                                 ((pos[1] + j) * (Global.tamCasillas - 1) + Global.WIDTH // 24,
                                  (pos[0] + i) * (Global.tamCasillas - 1) + Global.HEIGHT / 20,
                                  Global.tamCasillas, Global.tamCasillas), 1)


def dibujar_delete(screen, pos):
    pygame.draw.rect(screen, (255, 255, 255),(pos[1] * (Global.tamCasillas - 1) + Global.WIDTH // 24, pos[0] * (Global.tamCasillas - 1) + Global.HEIGHT / 20, Global.tamCasillas, Global.tamCasillas))

