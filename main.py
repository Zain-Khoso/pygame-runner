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

            screen.blit(
                snail_surf if obsticle_rect.bottom == 300 else fly_surf, obsticle_rect
            )

        obsticle_list = [obsticle for obsticle in obsticle_list if obsticle.x > -100]

    return obsticle_list


def collisions(player, obsticles):
    if obsticles:
        for obsticle in obsticles:
            if player.colliderect(obsticle):
                return False

    return True


def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]


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

snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_index = 0
snail_surf = snail_frames[snail_index]

fly_frame_1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_index = 0
fly_surf = fly_frames[fly_index]

obsticle_rect_list = []

player_walk_1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()

player_surf = player_walk[player_index]
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

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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
                if randint(0, 2):
                    obsticle_rect_list.append(
                        snail_surf.get_rect(bottomleft=(randint(900, 1100), 300))
                    )
                else:
                    obsticle_rect_list.append(
                        fly_surf.get_rect(bottomleft=(randint(900, 1100), 210))
                    )
            if event.type == snail_animation_timer:
                snail_index = 0 if snail_index == 1 else 1
                snail_surf = snail_frames[snail_index]

            if event.type == fly_animation_timer:
                fly_index = 0 if fly_index == 1 else 1
                fly_surf = fly_frames[fly_index]

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

        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom > 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)

        obsticle_rect_list = obsticle_movement(obsticle_rect_list)

        game_active = collisions(player_rect, obsticle_rect_list)
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
        obsticle_rect_list.clear()
        player_rect.midbottom = (150, 300)
        player_gravity = 0
        score = 0

        screen.fill((94, 129, 162))
        screen.blit(title_surf, title_rect)
        screen.blit(player_stand_surf, player_stand_rect)
        screen.blit(instructions_surf, instructions_rect)

    pygame.display.update()
    clock.tick(60)
