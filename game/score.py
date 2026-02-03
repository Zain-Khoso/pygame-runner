# Imports.
import pygame
from game.settings import *


# Score object.
class Score:
    def __init__(self):
        # Assets.
        self.font = pygame.font.Font(font_path, score_text_size)

        # Stats.
        self.score = 0

    def increase(self, by=1):
        self.score += by

    def reset(self):
        self.score = 0

    def get(self):
        return self.score

    def render(self, screen):
        surf = self.font.render(score_text % self.get(), False, score_text_color)
        rect = surf.get_rect(topright=(score_text_right, score_text_top))
        screen.blit(surf, rect)
