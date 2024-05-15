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


def dibujar_flechas(screen):
    left = pygame.image.load("src/left.png")
    right = pygame.image.load("src/right.png")
    left = pygame.transform.scale(left, (Global.WIDTH // 18, Global.HEIGHT // 10))
    right = pygame.transform.scale(right, (Global.WIDTH // 18, Global.HEIGHT // 10))
    screen.blit(left, (Global.WIDTH // 1.8, Global.HEIGHT // 2))
    screen.blit(right, (Global.WIDTH * 0.93, Global.HEIGHT // 2))


def dibujar_seleccion(screen, objeto):
    for i in range(objeto.tamano()[0]):
        for j in range(objeto.tamano()[1]):
            if objeto.matriz[i][j] != 0:
                pygame.draw.rect(screen, objeto.color,(j * (Global.tamCasillas - 1) + Global.WIDTH // 1.4, i * (Global.tamCasillas - 1) + Global.HEIGHT // 2, Global.tamCasillas, Global.tamCasillas))

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

