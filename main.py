from sys import exit
from random import randint, choice
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.gravity = 0
        self.frame = 0

        frame_1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
        frame_2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
        self.jump_frame = pygame.image.load("graphics/Player/jump.png").convert_alpha()

        self.frames = [frame_1, frame_2]
        self.image = self.frames[self.frame]
        self.rect = self.image.get_rect(midbottom=(200, 300))

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.rect.bottom == 300:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity

        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animate(self):
        if self.rect.bottom < 300:
            self.image = self.jump_frame
        else:
            self.frame += 0.1

            if self.frame >= len(self.frames):
                self.frame = 0

            self.image = self.frames[int(self.frame)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animate()


class Obsticle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "Snail":
            self.frames = [
                pygame.image.load("graphics/snail/snail1.png").convert_alpha(),
                pygame.image.load("graphics/snail/snail2.png").convert_alpha(),
            ]

        if type == "Fly":
            self.frames = [
                pygame.image.load("graphics/Fly/Fly1.png").convert_alpha(),
                pygame.image.load("graphics/Fly/Fly2.png").convert_alpha(),
            ]

        y_pos = 210 if type == "Fly" else 300

        self.frame = 0
        self.image = self.frames[self.frame]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animate(self):
        self.frame += 0.1

        if self.frame >= len(self.frames):
            self.frame = 0

        self.image = self.frames[int(self.frame)]

    def destroy(self):
        if self.rect.x < -100:
            self.kill()

    def update(self):
        self.rect.x -= 5

        self.animate()
        self.destroy()


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = font.render(f"Score: {int(current_time / 1000)}", False, "Black")
    score_rect = score_surf.get_rect(topright=(790, 10))
    screen.blit(score_surf, score_rect)
    return current_time


def collisions(player, obsticles):
    if obsticles:
        for obsticle in obsticles:
            if player.colliderect(obsticle):
                return False

    return True


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

        score = 0

        screen.fill((94, 129, 162))
        screen.blit(title_surf, title_rect)
        screen.blit(player_stand_surf, player_stand_rect)
        screen.blit(instructions_surf, instructions_rect)

    pygame.display.update()
    clock.tick(60)
