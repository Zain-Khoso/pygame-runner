# Imports.
import threading, requests, pygame
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

    def upload_task(self, data):
        try:
            requests.post(
                "http://localhost:5000/api/add-score",
                json=data,
                timeout=10,
            )
        except Exception:
            pass

    def reset(self, username: str | None):
        if username and self.score != 0:
            data = {"username": username, "score": self.score}

            thread = threading.Thread(target=self.upload_task, args=(data,))
            thread.daemon = False
            thread.start()

        self.score = 0

    def get(self):
        return self.score

    def render(self, screen):
        surf = self.font.render(score_text % self.get(), False, score_text_color)
        rect = surf.get_rect(topright=(score_text_right, score_text_top))
        screen.blit(surf, rect)
