from Utility.AnimationEffects.AnimationEffect import AnimationEffect
from os import path

pasta = path.dirname(__file__)

class LaserEffect(AnimationEffect):
    def __init__(self, game, position: tuple, scale: tuple, list_imgs: list, direction: int):
        super().__init__(game=game,
                         position=position,
                         scale=scale,
                         animation_speed=8,
                         looping=True,
                         list_imgs=list_imgs,
                         direction=direction)
    
    def hit(self):
        pass

