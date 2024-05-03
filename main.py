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
    objs = pygame.sprite.Group()
    objeto = Objetos.Objeto(1, 1, 1, 9)  # temp test
    objeto.add(objs)  # temp test
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:  # temp test
                if event.key == pygame.K_SPACE:  # temp test
                    objeto.kill()  # temp test
                    objeto = Objetos.Objeto(1, 1, 1, 9)  # temp test
                    objeto.add(objs)

        pygame.draw.rect(screen, (0, 0, 0), screen.get_rect())  # temp test
        objs.draw(screen)  # temp test

        # Juego.Juego(screen)
        pygame.time.Clock().tick(60)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
