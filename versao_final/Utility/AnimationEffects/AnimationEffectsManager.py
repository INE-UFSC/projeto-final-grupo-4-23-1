from Utility.AnimationEffects.ExplosionEffect.ExplosionEffect import ExplosionEffect
from Utility.AnimationEffects.BossExplosionEffect.BossExplosionEffect import BossExplosionEffect

class AnimationEffectsManager:
    def __init__(self):
        self.__effects = {"ExplosionEffect": ExplosionEffect,
                          "BossExplosionEffect": BossExplosionEffect}

    def add_explosion_effect(self, game, position: tuple, scale: tuple):
        self.__effects["ExplosionEffect"](game, position, scale)

    def add_boss_explosion_effect(self, game, position: tuple, scale: tuple):
        self.__effects["BossExplosionEffect"](game, position, scale)

   