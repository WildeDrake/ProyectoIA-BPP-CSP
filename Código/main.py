import pygame
import argparse
import Global
import Juego
import Agente

def main(mode, heuristic, showAnimation, Problem):
    pygame.init()
    ##Variables importantes aquí. Para ajustar tamaño del contenedor y resolución, ir a Global.py
    if mode == None:
        mode = 1    ## modo == 0 es para jugar, modo == 1 es para una iteración de SA, modo == 2 es para mostrar toda iteración de SA
    if heuristic == None:
        heuristic = 0 ## heuritic == 0 es para resolver con countingOrder, heuristic == 1 es para resolver con contactSurface
    if showAnimation == None:
        showAnimation = 1 ## showAnimation == 0 corre el agente sin animación, showAnimation == 1 da la animación
    if Problem == None:
        Problem = 0 ## Problem == 0 permite resolver el problema de Cutting Stock, Problem == 1 el de Bin Packing Problem

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
        Agente.Agente(mode, heuristic, showAnimation, Problem, screen)
        pygame.time.Clock().tick(60)

    ########################### Modo SimulatedAnnealing ###########################
    if mode == 2:
        if showAnimation == 1:
            screen = pygame.display.set_mode((Global.WIDTH, Global.HEIGHT))
            pygame.display.set_caption('Gato tiburón')
        else:
            screen = None
        Agente.Agente(mode, heuristic, showAnimation, Problem, screen)

    pygame.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Procesa algunos argumentos.')
    parser.add_argument('--mode', type=int, help='0 para Jugar, 1 para Heuristicas, 2 para SimulatedAnnealing')
    parser.add_argument('--heuristic', type=int, help='0 para readingOrder, 1 para heuristica2')
    parser.add_argument('--showAnimation', type=int, help='0 para no mostrar animación, 1 para mostrar animación')
    parser.add_argument('--Problem', type=int, help='0 para Cutting Stock Problem, 1 para Bin Packing Problem')
    args = parser.parse_args()
    main(args.mode, args.heuristic, args.showAnimation, args.Problem)
