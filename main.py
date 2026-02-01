from sys import exit
from random import randint
import pygame


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = font.render(f"Score: {int(current_time / 1000)}", False, "Black")
    score_rect = score_surf.get_rect(topright=(790, 10))
    screen.blit(score_surf, score_rect)
    return current_time


def obsticle_movement(obsticle_list):
    if obsticle_list:
        for obsticle_rect in obsticle_list:
            obsticle_rect.x -= 5

            screen.blit(snail_surf, obsticle_rect)

        obsticle_list = [obsticle for obsticle in obsticle_list if obsticle.x > -100]
    return obsticle_list


pygame.init()
pygame.display.set_caption("Runner")
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0
score = 0

sky_surf = pygame.image.load("graphics/Sky.png").convert()
groung_surf = pygame.image.load("graphics/ground.png").convert()

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft=(800, 300))

obsticle_rect_list = []

player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(150, 300))
player_gravity = 0

title_surf = font.render("Pygame Runner", False, "Black")
title_rect = title_surf.get_rect(midtop=(400, 50))

player_stand_surf = pygame.image.load(
    "graphics/Player/player_stand.png"
).convert_alpha()
player_stand_surf = pygame.transform.scale2x(player_stand_surf)
player_stand_rect = player_stand_surf.get_rect(center=(400, 200))

obsticle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obsticle_timer, 1800)

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

            if event.type == obsticle_timer:
                obsticle_rect_list.append(
                    snail_surf.get_rect(bottomleft=(randint(900, 1100), 300))
                )
        else:
            if event.type == pygame.MOUSEBUTTONDOWN or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE
            ):
                game_active = True
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(groung_surf, (0, 300))

        score = display_score()

        screen.blit(snail_surf, snail_rect)

        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom > 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        obsticle_rect_list = obsticle_movement(obsticle_rect_list)

        if player_rect.colliderect(snail_rect):
            game_active = False
            snail_rect.left = 800
    else:
        instructions_surf = font.render(
            (
                "Press 'SPACE' to start."
                if score == 0
                else f"Your score: {int(score/1000)}"
            ),
            False,
            "Black",
        )
        instructions_rect = instructions_surf.get_rect(midbottom=(400, 350))

        screen.fill((94, 129, 162))
        screen.blit(title_surf, title_rect)
        screen.blit(player_stand_surf, player_stand_rect)
        screen.blit(instructions_surf, instructions_rect)

    pygame.display.update()
    clock.tick(60)
