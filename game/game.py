# Imports.
import sys, random, pygame
from game.player import Player
from game.obsticle import Obsticle
from game.settings import *
from game.score import Score
from game.button import Button


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
        self.font = pygame.font.Font(font_path, menu_text_size)
        self.music = pygame.mixer.Sound(music_path)
        self.music.set_volume(music_volume)

        # Menu elements.
        self.title_surf = self.font.render(title_text, False, menu_text_color)
        self.avatar_surf = pygame.transform.scale_by(avatar, 0.8)

        # Local objects.
        self.player = pygame.sprite.GroupSingle()
        self.obsticles = pygame.sprite.Group()
        self.score = Score()

        # Menu buttons
        self.start_button = Button("Start", 100, self.start_game)
        self.restart_button = Button("Restart", 160, self.start_game)
        self.login_button = Button("Login", 220)
        self.signup_button = Button("Sign Up", 280)
        self.exit_button = Button("Exit", 340, self.exit_game)

        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.start_button)
        self.buttons.add(self.restart_button)
        self.buttons.add(self.login_button)
        self.buttons.add(self.signup_button)
        self.buttons.add(self.exit_button)

        # Game stats.
        self.clock = pygame.time.Clock()
        self.game_active = False

        # Timers.
        self.obsticle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obsticle_timer, obsticle_interval)

    def play_music(self):
        if self.music.get_num_channels() == 0:
            self.music.play(loops=-1)

    def stop_music(self):
        if self.music.get_num_channels() > 0:
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

        self.obsticles.add(Obsticle(random.choice(chioces), self.score))

    def handle_collisions(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.obsticles, False):
            self.obsticles.empty()
            self.game_active = False

        else:
            self.game_active = True

    def show_menu(self):
        # Title
        title_width = self.title_surf.get_width() + 20 + self.avatar_surf.get_width()
        title_height = max(self.title_surf.get_height(), self.avatar_surf.get_height())

        master_rect = pygame.Rect(0, 0, title_width, title_height)
        master_rect.center = (screen_width // 2, 50)

        title_rect = self.title_surf.get_rect(midleft=master_rect.midleft)
        avatar_rect = self.avatar_surf.get_rect(midright=master_rect.midright)

        # Drawing menu
        self.screen.fill(menu_color)
        self.screen.blit(self.title_surf, title_rect)
        self.screen.blit(self.avatar_surf, avatar_rect)
        self.buttons.draw(self.screen)
        self.score.render(self.screen)

        self.stop_music()

    def show_game(self):
        self.screen.blit(self.sky, (0, 0))
        self.screen.blit(self.ground, (0, 300))

        self.player.update()
        self.player.draw(self.screen)

        self.obsticles.update()
        self.obsticles.draw(self.screen)

        self.score.render(self.screen)
        self.handle_collisions()

        self.play_music()

    def start_game(self):
        self.score.reset()
        self.game_active = True

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game()

            if self.game_active:
                if event.type == self.obsticle_timer:
                    self.load_obsticle()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.game_active = False
            else:
                for button in self.buttons.sprites():
                    button.check_click(event)

    def run(self):
        self.load_player()

        while True:
            self.handle_events()

            self.show_game() if self.game_active else self.show_menu()

            pygame.display.update()
            self.clock.tick(fps)
