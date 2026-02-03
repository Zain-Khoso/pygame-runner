# Imports.
import sys, random, pygame
from code.player import Player
from code.obsticle import Obsticle
from code.settings import *


# Game object - Holds the root game logic.
class Game:
    def __init__(self):
        pygame.init()

        # Display setup.
        pygame.display.set_caption(screen_title)
        self.screen = pygame.display.set_mode((screen_width, screen_height))

        # Loading assets.
        self.sky = pygame.image.load(sky_path).convert()
        self.ground = pygame.image.load(ground_path).convert()
        avatar = pygame.image.load(avatar_path).convert_alpha()
        self.font = pygame.font.Font(font_path, font_size)
        self.music = pygame.mixer.Sound(music_path)
        self.music.set_volume(music_volume)

        # Surfaces and rectangles.
        self.title_surf = self.font.render(title_text, False, font_color_menu)
        self.title_rect = self.title_surf.get_rect(midtop=(400, 50))
        self.avatar_surf = pygame.transform.scale2x(avatar)
        self.avatar_rect = self.avatar_surf.get_rect(midbottom=(400, 300))

        # Sprite groups.
        self.player = pygame.sprite.GroupSingle()
        self.obsticles = pygame.sprite.Group()

        # Game stats.
        self.clock = pygame.time.Clock()
        self.game_active = False
        self.start_time = 0
        self.score = 0

        # Timers.
        self.obsticle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obsticle_timer, obsticle_interval)

    def play_music(self):
        if self.music.get_num_channels() == 0:
            self.music.play(loops=-1)

    def stop_music(self):
        self.music.stop()

    def load_player(self):
        self.player.add(Player())

    def load_obsticle(self):
        chioces = [
            obsticle_type_snail,
            obsticle_type_snail,
            obsticle_type_snail,
            obsticle_type_fly,
        ]

        self.obsticles.add(Obsticle(random.choice(chioces)))

    def display_score(self):
        current_time = pygame.time.get_ticks() - self.start_time
        score_surf = self.font.render(
            score_text % (int(current_time / 1000)), False, font_color_game
        )
        score_rect = score_surf.get_rect(topright=(790, 10))
        self.screen.blit(score_surf, score_rect)

        self.score = current_time

    def handle_collisions(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.obsticles, False):
            self.obsticles.empty()
            self.game_active = False

        else:
            self.game_active = True

    def show_menu(self):
        subtitle_surf = self.font.render(
            subtitle_1 if self.score == 0 else subtitle_2 % (int(self.score / 1000)),
            False,
            font_color_menu,
        )
        subtitle_rect = subtitle_surf.get_rect(midbottom=(400, 350))

        self.screen.fill((94, 129, 162))
        self.screen.blit(self.title_surf, self.title_rect)
        self.screen.blit(self.avatar_surf, self.avatar_rect)
        self.screen.blit(subtitle_surf, subtitle_rect)

        self.stop_music()

    def show_game(self):
        self.screen.blit(self.sky, (0, 0))
        self.screen.blit(self.ground, (0, 300))

        self.player.update()
        self.player.draw(self.screen)

        self.obsticles.update()
        self.obsticles.draw(self.screen)

        self.display_score()
        self.handle_collisions()

        self.play_music()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self.game_active and (event.type == self.obsticle_timer):
                self.load_obsticle()

            if (
                not self.game_active
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.game_active = True
                self.start_time = pygame.time.get_ticks()

    def run(self):
        self.load_player()

        while True:
            self.handle_events()

            self.show_game() if self.game_active else self.show_menu()

            pygame.display.update()
            self.clock.tick(fps)
