#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 22, 2018, 2:43 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        """

        :param position:
        """
        super(Bullet, self).__init__()
        self.image = pygame.image.load('material/image/bullet1.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 30
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        """
        Moving of a bullet, when hitting the edge of
        the screen, it dies
        :return:
        """
        if self.rect.top < 0:
            self.active = False
        else:
            self.rect.top -= self.speed

    def reset(self, position):
        """
        reset the function
        :return:
        """
        self.rect.left, self.rect.top = position
        self.active = True
