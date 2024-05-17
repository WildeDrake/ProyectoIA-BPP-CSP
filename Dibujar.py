import pygame
import Global
import Objetos

pygame.font.init()
font1 = pygame.font.Font(None, Global.WIDTH // 50)
font2 = pygame.font.Font(None, Global.WIDTH // 70)

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
    global font1
    text = font1.render("Valor en Contenedor: " + str(contenedor.valor), True, (255, 255, 255))
    screen.blit(text, (Global.WIDTH // 1.45, Global.HEIGHT // 1.05))

def dibujar_seleccion(screen, objeto, objetoSeleccionado, conjObjetos, contenedor):
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
    global flont1, font2
    text = font1.render(str(objetoSeleccionado+1) + " / " + str(len(conjObjetos)), True, (255, 255, 255))
    screen.blit(text, (Global.WIDTH // 1.34, Global.HEIGHT // 2.3))
    text = font1.render("Valor: " + str(objeto.valor), True, (255, 255, 255))
    screen.blit(text, (Global.WIDTH // 1.35, Global.HEIGHT // 1.1))
    text = font2.render(" r - rotar  |  i - invertir  |  espacio/enter - seleccionar objeto  |  escape/backspace - quitar objetos", True, (255, 255, 255))
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
    global font2
    text = font2.render(" r - rotar  |  i - invertir  |  espacio/enter -Colocar objeto  |  escape/backspace - Retroceder",True, (255, 255, 255))
    screen.blit(text, (Global.WIDTH // 1.8, Global.HEIGHT // 5))
    text = font2.render(" Flechas/WASD - Mover objeto",True, (255, 255, 255))
    screen.blit(text, (Global.WIDTH // 1.8, Global.HEIGHT // 5.7))


def dibujar_delete(screen, pos):
    pygame.draw.rect(screen, (255, 255, 255),(pos[1] * (Global.tamCasillas - 1) + Global.WIDTH // 24, pos[0] * (Global.tamCasillas - 1) + Global.HEIGHT / 20, Global.tamCasillas, Global.tamCasillas))

def dibujar_win(screen, contenedor):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, Global.WIDTH // 10)
    text = font.render("Fin del Juego", True, (255, 255, 255))
    screen.blit(text, (Global.WIDTH // 3, Global.HEIGHT // 2.3))
    text = font1.render("Valor del contenedor: " + str(contenedor.valor), True, (255, 255, 255))
    screen.blit(text, (Global.WIDTH // 2.1, Global.HEIGHT // 1.6))