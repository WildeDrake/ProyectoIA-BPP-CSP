import pygame
import Global

tamCasillas = Global.WIDTH//(Global.DimMochila[0]*2) + 1, Global.HEIGHT//(Global.DimMochila[1]*1.1) + 1


def dibujar_mochila(screen, mochila):
    global tamCasillas
    # Matriz de la mochila
    for i in range(mochila.tamano[0]):
        for j in range(mochila.tamano[1]):
            pygame.draw.rect(screen, (255, 255, 255), (j * tamCasillas[0] + Global.WIDTH//24, i * tamCasillas[1] + Global.HEIGHT/20, tamCasillas[0], tamCasillas[1]), 1)


def dibujar_menu(screen):
    left = pygame.image.load("src/left.png")
    right = pygame.image.load("src/right.png")
    left = pygame.transform.scale(left, (Global.WIDTH//18, Global.HEIGHT//10))
    right = pygame.transform.scale(right, (Global.WIDTH//18, Global.HEIGHT//10))
    screen.blit(left,(Global.WIDTH//1.8, Global.HEIGHT//2))
    screen.blit(right, (Global.WIDTH*0.93, Global.HEIGHT//2))


def dibujar_objeto(screen, objeto):
    screen.blit(objeto.image, objeto.rect.topleft)
