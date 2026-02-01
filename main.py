from sys import exit
import pygame


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = font.render(f"Score: {int(current_time / 1000)}", False, "Black")
    score_rect = score_surf.get_rect(topright=(790, 10))
    screen.blit(score_surf, score_rect)


pygame.init()
pygame.display.set_caption("Runner")
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = True
start_time = 0

sky_surf = pygame.image.load("graphics/Sky.png").convert()
groung_surf = pygame.image.load("graphics/ground.png").convert()

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft=(800, 300))

player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(50, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.MOUSEBUTTONDOWN or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE
            ):
                game_active = True
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(groung_surf, (0, 300))

        display_score()

        snail_rect.x -= 6
        if snail_rect.right <= 0:
            snail_rect.left = 800

        screen.blit(snail_surf, snail_rect)

        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom > 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        if player_rect.colliderect(snail_rect):
            game_active = False
            snail_rect.left = 800
    else:
        screen.fill("Red")

    pygame.display.update()
    clock.tick(60)
