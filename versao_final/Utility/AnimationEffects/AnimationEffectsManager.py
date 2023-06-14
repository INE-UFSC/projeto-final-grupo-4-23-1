import pygame
import fnmatch
import os
from Utility.AnimationEffects.AnimationEffect import AnimationEffect

pasta = os.path.dirname(__file__)
explosion_assets_dir = pasta+"//Frames//ExplosionFrames"
boss_explosion_assets_dir = pasta+"//Frames//BossExplosionFrames"
smoke_assets_dir = pasta+"//Frames//SmokeFrames"
laser_assets_dir = pasta+"//Frames//LaserFrames"

class AnimationEffectsManager:
    def __init__(self):
        self.__explosion_imgs_list =      self.load_list_imgs(explosion_assets_dir)
        self.__boss_explosion_imgs_list = self.load_list_imgs(boss_explosion_assets_dir)
        self.__smoke_imgs_list =          self.load_list_imgs(smoke_assets_dir)
        self.__laser_imgs_list =          self.load_list_imgs(laser_assets_dir)

    def add_explosion_effect(self, game, position: tuple, scale: tuple) -> AnimationEffect:
        return AnimationEffect(game, position, scale, 8, False, self.__explosion_imgs_list)

    def add_boss_explosion_effect(self, game, position: tuple, scale: tuple) -> AnimationEffect:
        return AnimationEffect(game, position, scale, 10, False, self.__boss_explosion_imgs_list)

    def add_smoke_effect(self, game, position: tuple, scale: tuple) -> AnimationEffect:
        return AnimationEffect(game, position, scale, 5, False, self.__smoke_imgs_list)

    def add_laser_effect(self, game, position: tuple, scale: tuple, direction: int) -> AnimationEffect:
        return AnimationEffect(game, position, scale, 8, True, self.__laser_imgs_list, direction)

    def load_list_imgs(self, assets_dir: str) -> list:
        imgs_list = list()
        n_images = len(fnmatch.filter(os.listdir(assets_dir), "*.png"))+1

        for n in range(1, n_images):
            img = pygame.image.load(assets_dir+f"//{n}.png")
            imgs_list.append(img)

        return imgs_list