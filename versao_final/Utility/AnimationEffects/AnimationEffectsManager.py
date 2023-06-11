import pygame
import fnmatch
import os
from Utility.AnimationEffects.ExplosionEffect.ExplosionEffect import ExplosionEffect
from Utility.AnimationEffects.BossExplosionEffect.BossExplosionEffect import BossExplosionEffect
from Utility.AnimationEffects.SmokeEffect.SmokeEffect import SmokeEffect
from Utility.AnimationEffects.LaserEffect.LaserEffect import LaserEffect

pasta = os.path.dirname(__file__)
explosion_assets_dir = pasta+"//ExplosionEffect//Assets"
boss_explosion_assets_dir = pasta+"//BossExplosionEffect//Assets"
smoke_assets_dir = pasta+"//SmokeEffect//Assets"
laser_assets_dir = pasta+"//LaserEffect//Assets"

class AnimationEffectsManager:
    def __init__(self):
        self.__effects = {"ExplosionEffect": ExplosionEffect,
                          "BossExplosionEffect": BossExplosionEffect,
                          "SmokeEffect": SmokeEffect,
                          "LaserEffect": LaserEffect}
        #load images
        self.__explosion_imgs_list = self.load_list_imgs(explosion_assets_dir)
        self.__boss_explosion_imgs_list = self.load_list_imgs(boss_explosion_assets_dir)
        self.__smoke_imgs_list = self.load_list_imgs(smoke_assets_dir)
        self.__laser_imgs_list = self.load_list_imgs(laser_assets_dir)

    def add_explosion_effect(self, game, position: tuple, scale: tuple) -> ExplosionEffect:
        return self.__effects["ExplosionEffect"](game, position, scale, self.__explosion_imgs_list)

    def add_boss_explosion_effect(self, game, position: tuple, scale: tuple) -> BossExplosionEffect:
        return self.__effects["BossExplosionEffect"](game, position, scale, self.__boss_explosion_imgs_list)

    def add_smoke_effect(self, game, position: tuple, scale: tuple) -> SmokeEffect:
        return self.__effects["SmokeEffect"](game, position, scale, self.__smoke_imgs_list)

    def add_laser_effect(self, game, position: tuple, scale: tuple, direction: int) -> LaserEffect:
        return self.__effects["LaserEffect"](game, position, scale, self.__laser_imgs_list, direction)


    def load_list_imgs(self, assets_dir: str) -> list:
        imgs_list = list()
        n_images = len(fnmatch.filter(os.listdir(assets_dir), "*.png"))+1

        for n in range(1, n_images):
            img = pygame.image.load(assets_dir+f"//{n}.png")
            imgs_list.append(img)

        return imgs_list