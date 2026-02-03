from sys import exit
from random import choice
import pygame

from player import Player
from obsticle import Obsticle

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = font.render(f"Score: {int(current_time / 1000)}", False, "Black")
    score_rect = score_surf.get_rect(topright=(790, 10))
    screen.blit(score_surf, score_rect)
    return current_time


def collisions():
    if pygame.sprite.spritecollide(player.sprite, obsticle_group, False):
        obsticle_group.empty()

        return False
    else:
        return True


pygame.init()
pygame.display.set_caption("Runner")
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound("audio/music.wav")
bg_music.play(loops=-1)

sky_surf = pygame.image.load("graphics/Sky.png").convert()
groung_surf = pygame.image.load("graphics/ground.png").convert()

player = pygame.sprite.GroupSingle()
player.add(Player())

obsticle_group = pygame.sprite.Group()

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

        if game_active and event.type == obsticle_timer:
            obsticle_group.add(Obsticle(choice(["Snail", "Snail", "Fly"])))

        if (
            not game_active
            and event.type == pygame.KEYDOWN
            and event.key == pygame.K_SPACE
        ):
            game_active = True
            start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(groung_surf, (0, 300))

        score = display_score()

        player.update()
        player.draw(screen)

        obsticle_group.update()
        obsticle_group.draw(screen)

        game_active = collisions()
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
