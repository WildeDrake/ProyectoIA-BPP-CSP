import pygame


def dibujar_mochila(screen, mochila):
    WIDTH, HEIGHT = screen.get_size()
    # Matriz de la mochila
    for i in range(mochila.tamano[0]):
        for j in range(mochila.tamano[1]):
            pygame.draw.rect(screen, (255, 255, 255), (j * (WIDTH//(mochila.tamano[0]*2)) + WIDTH//24, i * (HEIGHT//(mochila.tamano[1]*1.1)) + HEIGHT/20, WIDTH//(mochila.tamano[0]*2) + 1, HEIGHT//(mochila.tamano[1]*1.1) + 1), 1)


def dibujar_menu(screen):
    WIDTH, HEIGHT = screen.get_size()

    left = pygame.image.load("src/left.png")
    right = pygame.image.load("src/right.png")
    left = pygame.transform.scale(left, (WIDTH//18, HEIGHT//10))
    right = pygame.transform.scale(right, (WIDTH//18, HEIGHT//10))
    screen.blit(left,(WIDTH//1.8, HEIGHT//2))
    screen.blit(right, (WIDTH*0.93, HEIGHT//2))





def dibujar_objeto(screen, objeto):
    pass


