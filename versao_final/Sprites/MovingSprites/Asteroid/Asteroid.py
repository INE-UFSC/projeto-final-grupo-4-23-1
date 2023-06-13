import pygame
from Sprites.MovingSprites.MovingSprite import MovingSprite
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
        #velocidade do asteroid (aleatória)
        speed = randint(2, 4)
        #direção do asteroid (aleatória)
        direction = randint(0,360)
        #carrega a imagem do asteroid
        original_image = self.ld_image()

        super().__init__(game, speed, -direction, original_image, position)

    #se o asteroid for acertado, diminui de tamanho se o tamanho for maior que zero, caso contrário é destruído
    def hit(self) -> None:
        if self.size > 0:
            for _ in range(self.asteroids_ramaining):
                asteroid = Asteroid(self.game, self.size - 1, (self.x, self.y))
                self.game.all_sprites.add(asteroid)
                self.game.asteroid_group.add(asteroid)

        self.kill()
    
    def ld_image(self):
        n = randint(1,7)
        image = pygame.image.load(pasta+f"//images//asteroid_{n}.png")
        if self.size == 2:
            image = pygame.transform.scale(image, (90,90))
        
        elif self.size == 1:
            image = pygame.transform.scale(image, (60,60))
        
        else:
            image = pygame.transform.scale(image, (35,35))
        
        return image

    @property
    def size(self):
        return self.__size

    @property
    def asteroids_ramaining(self):
        return self.__asteroids_ramaining
    