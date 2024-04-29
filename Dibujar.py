import pygame


def dibujar_mochila(screen, mochila):
    WIDTH, HEIGHT = screen.get_size()
    # Matriz de la mochila
    for i in range(mochila.tamano[0]):
        for j in range(mochila.tamano[1]):
            pygame.draw.rect(screen, (255, 255, 255), (j * WIDTH//18 + WIDTH//24, i * HEIGHT//11 + HEIGHT/20, WIDTH//18, HEIGHT//11), 1)
    # Objetos de la mochila



