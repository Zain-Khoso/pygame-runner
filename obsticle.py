# Imports.
from random import randint
import pygame


# Obsticle object definition.
class Obsticle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "Snail":
            self.frames = [
                pygame.image.load("assets/snail/1.png").convert_alpha(),
                pygame.image.load("assets/snail/2.png").convert_alpha(),
            ]

        if type == "Fly":
            self.frames = [
                pygame.image.load("assets/fly/1.png").convert_alpha(),
                pygame.image.load("assets/fly/2.png").convert_alpha(),
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
