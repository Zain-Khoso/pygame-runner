# Imports.
import pygame
from game.settings import *


# Player object definition.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Loading assets.
        self.frames = [
            pygame.image.load(player_walk_1_path).convert_alpha(),
            pygame.image.load(player_walk_2_path).convert_alpha(),
        ]
        self.jump_frame = pygame.image.load(player_jump_path).convert_alpha()
        self.jump_sound = pygame.mixer.Sound(player_jump_sound_path)

        # States
        self.jump_sound.set_volume(player_jump_volume)
        self.gravity = 0
        self.frame = 0
        self.image = self.frames[self.frame]
        self.rect = self.image.get_rect(midbottom=(150, 300))

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.rect.bottom == 300:
            self.gravity = -player_jump_power
            self.jump_sound.play()

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
        self.handle_input()
        self.apply_gravity()
        self.animate()
