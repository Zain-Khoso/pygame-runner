from sys import exit
import pygame

pygame.init()
pygame.display.set_caption("Runner")
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
sky_surface = pygame.image.load("graphics/Sky.png")
groung_surface = pygame.image.load("graphics/ground.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(groung_surface, (0, 300))

    pygame.display.update()
    clock.tick(60)
