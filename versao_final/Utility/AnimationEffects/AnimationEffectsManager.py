from Utility.AnimationEffects.ExplosionEffect.ExplosionEffect import ExplosionEffect
from Utility.AnimationEffects.BossExplosionEffect.BossExplosionEffect import BossExplosionEffect
from Utility.AnimationEffects.SmokeEffect.SmokeEffect import SmokeEffect

class AnimationEffectsManager:
    def __init__(self):
        self.__effects = {"ExplosionEffect": ExplosionEffect,
                          "BossExplosionEffect": BossExplosionEffect,
                          "SmokeEffect": SmokeEffect}

    def add_explosion_effect(self, game, position: tuple, scale: tuple):
        self.__effects["ExplosionEffect"](game, position, scale)

    def add_boss_explosion_effect(self, game, position: tuple, scale: tuple):
        self.__effects["BossExplosionEffect"](game, position, scale)

    def add_smoke_effect(self, game, position: tuple, scale: tuple):
        self.__effects["SmokeEffect"](game, position, scale)

   