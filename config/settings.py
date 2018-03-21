#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 22, 2018, 2:43 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""
# Setting for the project

import os, pygame

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Game's background music
pygame.init()
pygame.mixer.init()  # Initialized the Mixer

# Background music of the global game
pygame.mixer.music.load(
    os.path.join(
        BASE_DIR,
        'material/sound/game_music.wav'
    )
)
pygame.mixer.music.set_volume(0.2)

# Sound of bullets
bullet_sound = pygame.mixer.Sound(
    os.path.join(
        BASE_DIR,
        'material/sound/bullet.wav'
    )
)
bullet_sound.set_volume(0.2)

# Sound of falling down of my planes
me_down_sound = pygame.mixer.Sound(
    os.path.join(
        BASE_DIR,
        'material/sound/game_over.wav'
    )
)
me_down_sound.set_volume(0.2)

# Sound of the falling of the enemies' planes
enemy1_down_sound = pygame.mixer.Sound(
    os.path.join(
        BASE_DIR,
        'material/sound/enemy1_down.wav'
    )
)
enemy1_down_sound.set_volume(0.2)

enemy2_down_sound = pygame.mixer.Sound(
    os.path.join(
        BASE_DIR,
        'material/sound/enemy2_down.wav'
    )
)
enemy2_down_sound.set_volume(0.2)

enemy3_down_sound = pygame.mixer.Sound(
    os.path.join(
        BASE_DIR,
        'material/sound/enemy3_down.wav'
    )
)
enemy3_down_sound.set_volume(0.2)

button_down_sound = pygame.mixer.Sound(
    os.path.join(
        BASE_DIR,
        'material/sound/button.wav'
    )
)
button_down_sound.set_volume(0.2)

level_up_sound = pygame.mixer.Sound(
    os.path.join(
        BASE_DIR,
        'material/sound/achievement.wav'
    )
)
level_up_sound.set_volume(0.2)

bomb_sound = pygame.mixer.Sound(
    os.path.join(
        BASE_DIR,
        'material/sound/use_bomb.wav'
    )
)
bomb_sound.set_volume(0.2)

get_bomb_sound = pygame.mixer.Sound(
    os.path.join(
        BASE_DIR,
        'material/sound/get_bomb.wav'
    )
)
get_bomb_sound.set_volume(0.2)

get_bullet_sound = pygame.mixer.Sound(
    os.path.join(
        BASE_DIR,
        'material/sound/get_double_laser.wav'
    )
)
get_bullet_sound.set_volume(0.2)

big_enemy_flying_sound = pygame.mixer.Sound(
    os.path.join(
        BASE_DIR,
        'material/sound/big_spaceship_flying.wav'
    )
)
big_enemy_flying_sound.set_volume(0.2)
