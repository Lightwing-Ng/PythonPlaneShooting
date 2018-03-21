#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 22, 2018, 2:43 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import sys
from pygame.locals import *

from config.settings import *
from src.plane import OurPlane  
from src.enemy import SmallEnemy
from src.bullet import Bullet

# Initialize screen size
bg_size = 480, 852
# set the dialogue box of background screen
screen = pygame.display.set_mode(bg_size)
# set the title
pygame.display.set_caption('Plane Shooting')
# load the background image
background = pygame.image.load(
    os.path.join(
        BASE_DIR,
        'material/image/background.png'
    )
)

# set the blood slot's color of RGB mode
color_black = (0, 0, 0)
color_green = (0, 255, 0)
color_red = (255, 0, 0)
color_white = (255, 255, 255)

# Obtain a plane
our_plane = OurPlane(bg_size)


def add_small_enemies(group1, group2, num):
    """
    Add enemies' planes of small size
    :param group1: formal parameters, sprite
    :param group2: formal parameters, sprite
    :param num:
    :return:
    """
    for i in range(num):
        small_enemy = SmallEnemy(bg_size)
        group1.add(small_enemy)
        group2.add(small_enemy)


def main():
    """
    Main entry of this game
    :return:
    """
    # -1, infinite loop
    pygame.mixer.music.play(-1)
    running = True
    switch_image = False
    delay = 60

    enemies = pygame.sprite.Group()
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 6)

    # define bullets
    bullet_index = 0
    e1_destroy_index = 0
    me_destroy_index = 0

    # define the number of bullets instances
    bullet1 = []
    bullet_num = 6
    for i in range(bullet_num):
        bullet1.append(
            Bullet(
                our_plane.rect.midtop
            )
        )

    while running:
        # draw a backgournd picture
        screen.blit(background, (0, 0))

        clock = pygame.time.Clock()
        clock.tick(60)

        if not delay % 3:
            switch_image = not switch_image

        # When the enemies are alive
        for each in small_enemies:
            if each.active:
                each.move()
                screen.blit(each.image, each.rect)

                pygame.draw.line(
                    screen,
                    color_black, (
                        each.rect.left,
                        each.rect.top - 5,
                    ), (
                        each.rect.right,
                        each.rect.top - 5
                    ), 2
                )
                energy_remain = each.energy / SmallEnemy.energy
                # Color ot Blood Slot
                if energy_remain > 0.2:
                    energy_color = color_green
                else:
                    energy_color = color_red
                pygame.draw.line(
                    screen,
                    energy_color, (
                        each.rect.left,
                        each.rect.top - 5
                    ), (
                        each.rect.left + each.rect.width * energy_remain,
                        each.rect.top - 5
                    ), 2
                )
            else:  # not active
                if e1_destroy_index == 0:
                    enemy1_down_sound.play()
                    screen.blit(
                        each.destroy_images[e1_destroy_index],
                        each.rect
                    )
                e1_destroy_index = (e1_destroy_index + 1) % 4

                if e1_destroy_index == 0:
                    each.reset()

        # When we are alive, display as normal
        if our_plane.active:
            if switch_image:
                screen.blit(
                    our_plane.image_one,
                    our_plane.rect
                )
            else:
                screen.blit(
                    our_plane.image_two,
                    our_plane.rect
                )

            # When alive, ready for shooting
            if not (delay % 10):
                bullet_sound.play()
                bullets = bullet1
                bullets[bullet_index].reset(our_plane.rect.midtop)
                bullet_index = (bullet_index + 1) % bullet_num

            for b in bullets:
                if b.active:  # when a bullet is activated
                    b.move()  # flying
                    screen.blit(b.image, b.rect)
                    enemies_hit = pygame.sprite.spritecollide(
                        b,
                        enemies,
                        False,
                        pygame.sprite.collide_mask
                    )

                    if enemies_hit:  # if the bullet hits a plane
                        # the bullet's mission is completed
                        b.active = False
                        for e in enemies_hit:
                            # at the same time, the plane is over
                            e.active = False

        # when our plane is destroy, a explosion happens
        else:
            if not (delay % 3):
                screen.blit(
                    our_plane.destroy_images[me_destroy_index],
                    our_plane.rect
                )
                me_destroy_index = (me_destroy_index + 1) % 4
            if me_destroy_index == 0:
                me_down_sound.play()
                our_plane.reset()

        # When our plane collides with the enermy in the air,
        # it's over
        enemies_down = pygame.sprite.spritecollide(
            our_plane,
            enemies,
            False,
            pygame.sprite.collide_mask
        )

        for event in pygame.event.get():
            if event.type == 12:
                pygame.quit()
                sys.exit()

        if delay == 0:
            delay = 60
        delay -= 1

        # trigger from keyboard
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            our_plane.move_up()
        elif key_pressed[K_s] or key_pressed[K_DOWN]:
            our_plane.move_down()
        elif key_pressed[K_a] or key_pressed[K_LEFT]:
            our_plane.move_left()
        elif key_pressed[K_d] or key_pressed[K_RIGHT]:
            our_plane.move_right()

        # draw the new image and display it
        pygame.display.flip()
