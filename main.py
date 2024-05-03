import random

# import Juego
import Objetos
import pygame

WIDTH, HEIGHT = 1800, 1000


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('MochilaJogo')
    running = True
    objeto = Objetos.Objeto(1, 1, 1, 9)  # temp test
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:  # temp test
                if event.key == pygame.K_SPACE:  # temp test
                    del objeto  # temp test
                    objeto = Objetos.Objeto(1, 1, 1, 9)  # temp test

                if event.key == pygame.K_UP:
                    objeto.mover(0, -1)
                if event.key == pygame.K_DOWN:
                    objeto.mover(0, 1)
                if event.key == pygame.K_LEFT:
                    objeto.mover(-1, 0)
                if event.key == pygame.K_RIGHT:
                    objeto.mover(1, 0)

                if event.key == pygame.K_r:
                    objeto.rotar()

        pygame.draw.rect(screen, (0, 0, 0), screen.get_rect(), )  # temp test
        objeto.draw(screen)  # temp test

        # Juego.Juego(screen)
        pygame.time.Clock().tick(60)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
