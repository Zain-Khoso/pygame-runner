from sys import exit
import pygame

pygame.init()
pygame.display.set_caption("Runner")
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
groung_surface = pygame.image.load("graphics/ground.png").convert()
text_surface = test_font.render("Hello World", False, "Black")

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft=(800, 300))

player_suface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_suface.get_rect(midbottom=(50, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(groung_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    screen.blit(snail_surface, snail_rect)
    screen.blit(player_suface, player_rect)

    pygame.display.update()
    clock.tick(60)
