from sys import exit
import pygame

pygame.init()
pygame.display.set_caption("Runner")
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png")
groung_surface = pygame.image.load("graphics/ground.png")
text_surface = test_font.render("Hello World", False, "Black")

snail_surface = pygame.image.load("graphics/snail/snail1.png")
snail_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(groung_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_x_pos -= 4
    screen.blit(snail_surface, (snail_x_pos, 250))

    pygame.display.update()
    clock.tick(60)
