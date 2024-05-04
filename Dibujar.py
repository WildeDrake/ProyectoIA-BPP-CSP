import pygame
import Global


def dibujar_contenedor(screen, contenedor):
    for i in range(contenedor.tamano[0]):
        for j in range(contenedor.tamano[1]):
            pygame.draw.rect(screen, (255, 255, 255), (j * (Global.tamCasillas-1) + Global.WIDTH//24 , i * (Global.tamCasillas-1) + Global.HEIGHT/20, Global.tamCasillas, Global.tamCasillas), 1)


def dibujar_flechas(screen):
    left = pygame.image.load("src/left.png")
    right = pygame.image.load("src/right.png")
    left = pygame.transform.scale(left, (Global.WIDTH//18, Global.HEIGHT//10))
    right = pygame.transform.scale(right, (Global.WIDTH//18, Global.HEIGHT//10))
    screen.blit(left,(Global.WIDTH//1.8, Global.HEIGHT//2))
    screen.blit(right, (Global.WIDTH*0.93, Global.HEIGHT//2))


def dibujar_objeto(screen, objeto):
    pass
