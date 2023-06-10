import pygame
import fnmatch
import os

class AnimationEffect(pygame.sprite.Sprite):
    def __init__(self, game, position: tuple, scale: tuple, animation_speed: int, list_imgs: list):
        super().__init__()

        self.__position = position
        self.__scale = scale

        self.__images_list = list_imgs
        self.__index = 0
        self.__counter_gap = 0
        self.__animation_speed = animation_speed

        img = self.__images_list[self.__index]
        self.__image = pygame.transform.scale(img, self.__scale)
        self.__rect = self.image.get_rect()
        self.rect.center = self.__position

        game.all_sprites.add(self)

    def update(self):
        self.__counter_gap += 1
        if (self.__counter_gap >= self.__animation_speed):
            if (self.__index < (len(self.__images_list)-1)):
                self.__counter_gap = 0
                self.__index += 1
                img = self.__images_list[self.__index]
                self.__image = pygame.transform.scale(img, self.__scale)

            if (self.__index >= (len(self.__images_list)-1)):
                self.kill()

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect


