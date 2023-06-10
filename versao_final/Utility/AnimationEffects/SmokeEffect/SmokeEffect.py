from Utility.AnimationEffects.AnimationEffect import AnimationEffect
from os import path

pasta = path.dirname(__file__)

class SmokeEffect(AnimationEffect):
    def __init__(self, game, position: tuple, scale: tuple, list_imgs: list):
        super().__init__(game=game,
                         position=position,
                         scale=scale,
                         animation_speed=5,
                         list_imgs=list_imgs)
