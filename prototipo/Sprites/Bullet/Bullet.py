import pygame
from Sprites.MovingSprite import MovingSprite
from time import time

class Bullet(MovingSprite):
    def __init__(self, game,
                 position: tuple,
                 direction: int,
                 speed: float,
                 damage: int,
                 color: str,
                 lifetime: int) -> None:

        #dano e tempo de vida
        self.__damage = damage
        self.__lifetime = lifetime  # 5 pra desaparecer

        #tempo de criação
        self.__criacao = time()
        #cor do bulelt
        self.__color = color

        original_image = pygame.Surface([20,3], pygame.SRCALPHA)
        pygame.draw.rect(original_image, (self.color), (0, 0, 20, 3))
        #super do init
        super().__init__(game, speed, -direction, original_image, position)

    def update_image_position(self) -> None:
        super().update_image_position()
        self.set_image(pygame.transform.rotate(self.original_image, -self.direction))

    def hit(self) -> None:
        self.kill()

    def detect_lifetime(self) -> None:
        if (time() - self.criacao > self.lifetime):
            self.kill

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

