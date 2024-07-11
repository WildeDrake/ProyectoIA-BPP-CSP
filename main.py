import pygame
import argparse
import Global
import Juego
import Agente

def main(mode, heuristic, showAnimation, Problem):
    pygame.init()

    if mode == None:
        mode = 0
    if heuristic == None:
        heuristic = 0
    if showAnimation == None:
        showAnimation = 0
    if Problem == None:
        Problem = 0

    ########################### Modo Juego ###########################
    if mode == 0:
        screen = pygame.display.set_mode((Global.WIDTH, Global.HEIGHT))
        if Problem == 0:
            pygame.display.set_caption('Cutting Stock Problem Playable')
        else:
            pygame.display.set_caption('Bin Packing Problem Playable')
        while Juego.Juego(screen):
            pygame.time.Clock().tick(60)
            pygame.display.flip()

    ########################### Modo Heuristica ###########################
    if mode == 1:
        if showAnimation == 1:
            screen = pygame.display.set_mode((Global.WIDTH, Global.HEIGHT))
            if heuristic == 0:
                if Problem == 0:
                    pygame.display.set_caption('Cutting Stock Problem Agent - readingOrder')
                else:
                    pygame.display.set_caption('Bin Packing Problem Agent - readingOrder')
            if heuristic == 1:
                if Problem == 0:
                    pygame.display.set_caption('Cutting Stock Problem Agent - heuristica2')
                else:
                    pygame.display.set_caption('Bin Packing Problem Agent - heuristica2')
            pygame.display.set_caption('Bin Packing Problem Agent - readingOrder')
        else:
            screen = None
        while Agente.Agente(mode, heuristic, showAnimation, Problem, screen):
            pygame.time.Clock().tick(60)

    ########################### Modo SimulatedAnnealing ###########################

    for i in range(30):
        Global.randConj = i + 69
        Agente.Agente(mode, heuristic, showAnimation, Problem)

    pygame.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Procesa algunos argumentos.')
    parser.add_argument('--mode', type=int, help='0 para Jugar, 1 para Heuristicas, 2 para SimulatedAnnealing')
    parser.add_argument('--heuristic', type=int, help='0 para readingOrder, 1 para heuristica2')
    parser.add_argument('--showAnimation', type=int, help='0 para no mostrar animación, 1 para mostrar animación')
    parser.add_argument('--Problem', type=int, help='0 para Cutting Stock Problem, 1 para Bin Packing Problem')
    args = parser.parse_args()
    main(args.mode, args.heuristic, args.showAnimation, args.Problem)
