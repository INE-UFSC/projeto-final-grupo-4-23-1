import pygame
from Sprites.MovingSprite import MovingSprite
from math import cos, sin, radians
from os import path
from random import randint

pasta = path.dirname(__file__)

class Asteroid(MovingSprite):
    def __init__(self, game, size: int = 2, position: tuple = None) -> None:
        #tamanho
        self.__size = size
        #quantidade de asteroids a dividir quando é destruido
        self.__asteroids_ramaining = 2

        speed = randint(2, 4)
        direction = randint(0,360)
        original_image = pygame.image.load(pasta+f"//asteroid_{self.size}.png")

        super().__init__(game, speed, -direction, original_image, position)

    def hit(self) -> None:
        if self.size > 0:
            for _ in range(self.asteroids_ramaining):
                asteroid = Asteroid(self.game, self.size - 1, (self.x, self.y))
                self.game.all_sprites.add(asteroid)
                self.game.all_asteroids.add(asteroid)

        self.kill()

    @property
    def size(self):
        return self.__size

    @property
    def asteroids_ramaining(self):
        return self.__asteroids_ramaining
    