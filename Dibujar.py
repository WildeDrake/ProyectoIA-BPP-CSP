import pygame


def dibujar_mochila(screen, mochila):
    WIDTH, HEIGHT = screen.get_size()
    # Matriz de la mochila
    for i in range(mochila.tamano[0]):
        for j in range(mochila.tamano[1]):
            pygame.draw.rect(screen, (255, 255, 255), (j * (WIDTH//(mochila.tamano[0]*2)) + WIDTH//24, i * (HEIGHT//(mochila.tamano[1]*1.1)) + HEIGHT/20, WIDTH//(mochila.tamano[0]*2) + 1, HEIGHT//(mochila.tamano[1]*1.1) + 1), 1)




