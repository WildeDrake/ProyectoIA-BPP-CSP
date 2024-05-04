import Global
import Juego
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((Global.WIDTH, Global.HEIGHT))
    pygame.display.set_caption('ContenedorJogo')

    while Juego.Juego(screen):
        pygame.time.Clock().tick(60)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
