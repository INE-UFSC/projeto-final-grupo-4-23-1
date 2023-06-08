from Utility.AnimationEffects.ExplosionEffect.ExplosionEffect import ExplosionEffect

class AnimationEffectsManager:
    def __init__(self):
        self.__effects = {"ExplosionEffect": ExplosionEffect}

    def add_explosion_effect(self, game, position: tuple, scale: tuple):
        self.__effects["ExplosionEffect"](game, position, scale)

    