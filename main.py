from sys import exit
import pygame

pygame.init()
pygame.display.set_caption("Runner")
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surf = pygame.image.load("graphics/Sky.png").convert()
groung_surf = pygame.image.load("graphics/ground.png").convert()

text_surf = test_font.render("Score: 0", False, "Black")
text_rect = text_surf.get_rect(topright=(790, 10))

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft=(800, 300))

player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(50, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surf, (0, 0))
    screen.blit(groung_surf, (0, 300))

    screen.blit(text_surf, text_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    player_rect.colliderect(snail_rect)

    pygame.display.update()
    clock.tick(60)
