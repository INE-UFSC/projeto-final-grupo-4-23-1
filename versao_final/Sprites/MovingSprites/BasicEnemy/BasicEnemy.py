import pygame
from Sprites.MovingSprite import MovingSprite
from Sprites.Bullet.Bullet import Bullet
from random import randint
from time import time
from os import path

pasta = path.dirname(__file__)

class BasicEnemy(MovingSprite):
    def __init__(self, game, life: int, position: tuple = None) -> None:
        self.__life = life

        self.__change_direction_time = time()
        self.__last_shoot_time = time()

        speed = randint(2, 4)
        direction = randint(0, 360)
        original_image = pygame.image.load(pasta+"//BasicEnemy.png")
        super().__init__(game, speed, -direction, original_image, position)

    def hit(self) -> None:
        self.__life -= 1
        if (self.life <= 0):
            self.kill()

    def shoot(self) -> None:
        if ((time() - self.last_shoot_time) > 2):
            direction = randint(0, 360)

            bullet = Bullet(self.game, (self.x, self.y), direction, 10, 1, "red", 1)
            self.game.all_sprites.add(bullet)
            self.game.enemy_bullets_group.add(bullet)

            self.__last_shoot_time = time()
    
    def update_image_position(self) -> None:
        super().update_image_position()
        self.set_image(self.original_image)

    def change_direction(self) -> None:
        if ((time() - self.change_direction_time) > 5):

            direction = randint(0, 360)
            self.set_direction(direction)

            self.__change_direction_time = time()

    def update(self) -> None:
        self.change_direction()
        self.shoot()
        super().update()

    @property
    def last_shoot_time(self):
        return self.__last_shoot_time

    @property
    def change_direction_time(self):
        return self.__change_direction_time

    @property
    def life(self):
        return self.__life