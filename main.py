from sys import exit
import pygame

pygame.init()
pygame.display.set_caption("Runner")
screen = pygame.display.set_mode((800, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
