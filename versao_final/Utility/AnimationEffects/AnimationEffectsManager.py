import pygame
import fnmatch
import os
from Utility.AnimationEffects.ExplosionEffect.ExplosionEffect import ExplosionEffect
from Utility.AnimationEffects.BossExplosionEffect.BossExplosionEffect import BossExplosionEffect
from Utility.AnimationEffects.SmokeEffect.SmokeEffect import SmokeEffect

pasta = os.path.dirname(__file__)
explosion_assets_dir = pasta+"//ExplosionEffect//Assets"
boss_explosion_assets_dir = pasta+"//BossExplosionEffect//Assets"
smoke_assets_dir = pasta+"//SmokeEffect//Assets"

class AnimationEffectsManager:
    def __init__(self):
        self.__effects = {"ExplosionEffect": ExplosionEffect,
                          "BossExplosionEffect": BossExplosionEffect,
                          "SmokeEffect": SmokeEffect}
        #load images
        self.__explosion_imgs_list = self.load_list_imgs(explosion_assets_dir)
        self.__boss_explosion_imgs_list = self.load_list_imgs(boss_explosion_assets_dir)
        self.__smoke_imgs_list = self.load_list_imgs(smoke_assets_dir)

    def add_explosion_effect(self, game, position: tuple, scale: tuple):
        self.__effects["ExplosionEffect"](game, position, scale, self.__explosion_imgs_list)

    def add_boss_explosion_effect(self, game, position: tuple, scale: tuple):
        self.__effects["BossExplosionEffect"](game, position, scale, self.__boss_explosion_imgs_list)

    def add_smoke_effect(self, game, position: tuple, scale: tuple):
        self.__effects["SmokeEffect"](game, position, scale, self.__smoke_imgs_list)


    def load_list_imgs(self, assets_dir: str) -> list:
        imgs_list = list()
        n_images = len(fnmatch.filter(os.listdir(assets_dir), "*.png"))+1

        for n in range(1, n_images):
            img = pygame.image.load(assets_dir+f"//{n}.png")
            imgs_list.append(img)

        return imgs_list