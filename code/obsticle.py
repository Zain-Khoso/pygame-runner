# Imports.
from random import randint
import pygame
from code.settings import *


# Obsticle object definition.
class Obsticle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == obsticle_type_snail:
            self.frames = [
                pygame.image.load(obsticle_snail_frame_1_path).convert_alpha(),
                pygame.image.load(obsticle_snail_frame_2_path).convert_alpha(),
            ]

        if type == obsticle_type_fly:
            self.frames = [
                pygame.image.load(obsticle_fly_frame_1_path).convert_alpha(),
                pygame.image.load(obsticle_fly_frame_2_path).convert_alpha(),
            ]

        y_pos = 210 if type == obsticle_type_fly else 300

        self.frame = 0
        self.image = self.frames[self.frame]
        self.rect = self.image.get_rect(
            midbottom=(randint(obsticle_dis_start, obsticle_dis_end), y_pos)
        )

    def animate(self):
        self.frame += 0.1

        if self.frame >= len(self.frames):
            self.frame = 0

        self.image = self.frames[int(self.frame)]

    def update(self):
        self.rect.x -= obsticle_speed

        self.kill() if self.rect.x < -100 else None

        self.animate()
