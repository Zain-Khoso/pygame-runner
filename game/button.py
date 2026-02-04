# Imports.
import pygame
from game.settings import *


# Button object - Holds the logic for all menu buttons.
class Button(pygame.sprite.Sprite):
    def __init__(self, label: str, y_pos: int, action=None):
        super().__init__()

        self.font = pygame.font.Font(font_path, button_text_size)
        self.action = action

        # Label
        self.text_surf = self.font.render(label, False, button_text_color)

        # Background
        padding_x, padding_y = 64, 24
        self.width = self.text_surf.get_width() + padding_x
        self.height = self.text_surf.get_height() + padding_y

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(button_color)

        # Putting text on backgrund
        text_rect = self.text_surf.get_rect(
            center=(self.width // 2, (self.height // 2) + 2)
        )
        self.image.blit(self.text_surf, text_rect)

        self.rect = self.image.get_rect(midtop=(screen_width // 2, y_pos))

    def check_click(self, event):
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
            and self.action
        ):
            self.action()
