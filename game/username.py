# Imports.
import os, pygame
from game.settings import *


# Username object - holds all the logic of changing username.
class Username:
    def __init__(self):
        # Loading assets
        self.font = pygame.font.Font(font_path, button_text_size)

        # States.
        self.value = self.read()

    def read(self):
        if not os.path.exists(username_file_path):
            return ""

        try:
            with open(username_file_path, "r") as file:
                return file.read().strip()
        except Exception as e:
            print(f"Error reading file: {e}")
            return ""

    def get(self):
        return self.value

    def write(self):
        try:
            with open("username.txt", "w", encoding="utf-8") as file:
                file.write(str(self.value).strip())
        except IOError as e:
            print(f"FileSystem Error: {e}")
        except Exception as e:
            print(f"Unexpected error saving file: {e}")

    def handle_input(self, event):
        if event.key == pygame.K_BACKSPACE:
            self.value = self.value[:-1]
        elif event.key == pygame.K_RETURN:
            if len(self.value) <= 0 or len(self.value) > 14:
                return

            self.write()
        else:
            if len(self.value) < 15:
                self.value += event.unicode

    def render(self, screen):
        # Text
        value_surf = self.font.render(self.value, False, button_color)

        # Bg box
        width = max(value_surf.get_width() + 16, 100)
        height = value_surf.get_height() + 8
        value_rect = pygame.Rect(0, 0, width, height)
        value_rect.midbottom = (screen_width // 2, 350)

        pygame.draw.rect(screen, button_color, value_rect, 2)
        screen.blit(value_surf, value_rect)
