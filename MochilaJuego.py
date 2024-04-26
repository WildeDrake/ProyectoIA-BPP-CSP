from Objetos import Mochila
import pygame


pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Mochila Juego')
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    mochila = Mochila(100, (20, 20))
    pygame.draw.rect(screen, (0, 255, 255), (200, 150, mochila.tamano[0]*10, mochila.tamano[1]*10))
    pygame.display.flip()

pygame.quit()