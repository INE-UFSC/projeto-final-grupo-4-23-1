import pygame
import fnmatch
import os

class AnimationEffect(pygame.sprite.Sprite):
    def __init__(self, game, position: tuple, scale: tuple, animation_speed: int, img_dir: str):
        super().__init__()

        self.__position = position
        self.__scale = scale

        self.__image_dir = img_dir

        self.__images_list = list()
        self.__index = 0
        self.__counter_gap = 0
        self.__animation_speed = animation_speed

        self.load_images()
        self.__image = self.__images_list[self.__index]        
        self.__rect = self.image.get_rect()
        self.rect.center = self.__position

        game.all_sprites.add(self)

    def load_images(self):
        n_images = len(fnmatch.filter(os.listdir(self.__image_dir), "*.png"))+1

        for n in range(1, n_images):
            img = pygame.image.load(self.__image_dir+f"//{n}.png")
            img = pygame.transform.scale(img, self.__scale)
            self.__images_list.append(img)

    def update(self):
        self.__counter_gap += 1
        if (self.__counter_gap >= self.__animation_speed):
            if (self.__index < (len(self.__images_list)-1)):
                self.__counter_gap = 0
                self.__index += 1
                self.__image = self.__images_list[self.__index]

            if (self.__index >= (len(self.__images_list)-1)):
                self.kill()

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

