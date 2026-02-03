# Imports.
import pygame


# Player object definition.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.gravity = 0
        self.frame = 0

        frame_1 = pygame.image.load("assets/player/walk_1.png").convert_alpha()
        frame_2 = pygame.image.load("assets/player/walk_2.png").convert_alpha()
        self.jump_frame = pygame.image.load("assets/player/jump.png").convert_alpha()
        self.jump_sound = pygame.mixer.Sound("assets/player/jump.mp3")
        self.jump_sound.set_volume(0.5)

        self.frames = [frame_1, frame_2]
        self.image = self.frames[self.frame]
        self.rect = self.image.get_rect(midbottom=(80, 300))

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.rect.bottom == 300:
            self.gravity = -20
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
        self.player_input()
        self.apply_gravity()
        self.animate()
