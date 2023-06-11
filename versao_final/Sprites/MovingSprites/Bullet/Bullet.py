import pygame
from Sprites.MovingSprites.MovingSprite import MovingSprite
from time import time

class Bullet(MovingSprite):
    def __init__(self, game,
                 position: tuple,
                 direction: int,
                 speed: float,
                 damage: int,
                 color: str,
                 lifetime: int,
                 img = None) -> None:

        #dano e tempo de vida
        self.__damage = damage
        self.__lifetime = lifetime  # 5 pra desaparecer

        #tempo de criação
        self.__criacao = time()
        #cor do bulelt
        self.__color = color

        default_img = pygame.Surface([20, 3], pygame.SRCALPHA)
        original_image = default_img if (img == None) else img
        #super do init
        super().__init__(game, speed, -direction, original_image, position)


    def update_image_position(self) -> None:
        image = pygame.transform.rotate(self.original_image, -self.direction)
        self.set_image(image)
        self.set_rect(self.image.get_rect(center = (self.x, self.y)))
        self.set_mask(pygame.mask.from_surface(self.image))

    def hit(self) -> None:
        self.kill()

    def detect_lifetime(self) -> None:
        if (time() - self.criacao > self.lifetime):
            self.kill()

    def update(self) -> None:
        self.detect_lifetime()
        super().update()


    @property
    def color(self):
        return self.__color
    
    @property
    def damage(self):
        return self.__damage

    @property
    def lifetime(self):
        return self.__lifetime
    
    @property
    def criacao(self):
        return self.__criacao

