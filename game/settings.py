# Imports.
import sys
import os


# Function to get an absolute path to resources
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # type: ignore
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Screen
screen_title = "Pygame - Runner"
screen_width = 800
screen_height = 400

# Assets
sky_path = resource_path("assets/sky.png")
ground_path = resource_path("assets/ground.png")
avatar_path = resource_path("assets/player/stand.png")
font_path = resource_path("assets/font.ttf")
music_path = resource_path("assets/music.wav")
obsticle_snail_frame_1_path = resource_path("assets/snail/1.png")
obsticle_snail_frame_2_path = resource_path("assets/snail/2.png")
obsticle_fly_frame_1_path = resource_path("assets/fly/1.png")
obsticle_fly_frame_2_path = resource_path("assets/fly/2.png")
player_walk_1_path = resource_path("assets/player/walk_1.png")
player_walk_2_path = resource_path("assets/player/walk_2.png")
player_jump_path = resource_path("assets/player/jump.png")
player_jump_sound_path = resource_path("assets/player/jump.mp3")
username_file_path = resource_path("username.txt")

# Menu
menu_color = (94, 129, 162)
menu_text_size = 80
menu_text_color = (111, 196, 169)
button_color = (64, 64, 64)
button_text_size = 36
button_text_color = (111, 196, 169)
title_text = "Runner"
music_volume = 0.1
fps = 60

# Obsticle
obsticle_interval = 1500
obsticle_type_snail = "Snail"
obsticle_type_fly = "Fly"
obsticle_dis_start = 900
obsticle_dis_end = 1100
obsticle_speed = 5

# Player
player_jump_volume = 0.2
player_jump_power = 20

# Score
score_text = "Score: %s"
score_text_color = (64, 64, 64)
score_text_size = 30
score_text_top = 20
score_text_right = 780
