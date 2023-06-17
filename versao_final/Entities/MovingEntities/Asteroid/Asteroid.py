import pygame
from Entities.MovingEntities.MovingEntity import MovingEntity
from random import randint


class Asteroid(MovingEntity):
    def __init__(self, game, lst_imgs: list, size: int = 2, position: tuple = None) -> None:
        self.__size = size
        self.__asteroids_ramaining = 2
        self.__images_list = lst_imgs
        speed = randint(2, 4)
        direction = randint(0,360)
        original_image = self.ld_image()

        super().__init__(game, speed, -direction, original_image, position)

    #se o asteroid for acertado, diminui de tamanho se o tamanho for maior que zero, caso contrário é destruído
    def hit(self) -> None:
        if self.size > 0:
            for _ in range(self.asteroids_ramaining):
                asteroid = Asteroid(self.game, self.__images_list,self.size - 1, (self.x, self.y))
                self.game.all_sprites.add(asteroid)
                self.game.asteroid_group.add(asteroid)

        self.kill()
    
    def ld_image(self):
        n = randint(0,6)
        image = self.__images_list[n]
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
    