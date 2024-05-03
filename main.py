import random
import Juego
import Objetos
import pygame

WIDTH, HEIGHT = 1800, 1000


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('MochilaJogo')

    while Juego.Juego(screen):
        pygame.time.Clock().tick(60)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
