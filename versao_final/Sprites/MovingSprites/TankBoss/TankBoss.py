import pygame
from Sprites.MovingSprites.MovingSprite import MovingSprite
from random import randint
from time import time
from os import path
from math import atan2, cos, sin, radians, pi

pasta = path.dirname(__file__)

class TankBoss(MovingSprite):
    def __init__(self, game, life: int, position: tuple = None) -> None:
        self.__life = life

        self.__change_direction_time = time()
        self.__rush_time = time()
        self.__stop_time = time()
        self.__stop = False
        self.__activate_rush = False


        speed = 5
        direction = randint(0, 360)
        original_image = pygame.image.load(pasta+"//TankBoss.png")
        super().__init__(game, speed, -direction, original_image, position)

    def hit(self) -> None:
        if (self.activate_rush == False):
            self.__life -= 1
            if (self.life <= 0):
                self.kill()

    def update_image_position(self) -> None:
        super().update_image_position()
        self.set_image(self.original_image)

    def change_direction(self) -> None:
        if (self.activate_rush == False):
            if ((time() - self.change_direction_time) > 3):

                direction = randint(0, 360)
                self.set_speed(5)
                image = pygame.image.load(pasta+"//TankBoss.png")
                self.set_original_image(image)
                self.set_direction(direction)

                self.__change_direction_time = time()

    def rush(self) -> None:
        if (self.activate_rush == False):
            if ((time() - self.rush_time) > 8):
                self.__activate_rush = True
                image = pygame.image.load(pasta+"//TankBoss_rush.png")
                self.set_original_image(image)
                self.__stop_time = time()
        else:
            if ((time() - self.stop_time) < 2):
                self.__stop = True
            else:
                self.__stop = False
                ship_x = self.game.ship.x
                ship_y = self.game.ship.y
                angle = atan2(ship_y-self.y, ship_x-self.x) 
                direction = int(180*angle/pi)

                self.__change_direction_time = time()-1.5
                self.set_speed(15)
                self.set_direction(direction)

                self.__rush_time = time()
                self.__activate_rush = False
    

    def update_position(self) -> None:
        if (self.stop == False):
            x = self.x + self.speed * cos(radians(self.direction))
            y = self.y + self.speed * sin(radians(self.direction))
            self.set_pos(x, y)

    def update(self) -> None:
        self.change_direction()
        self.rush()
        super().update()

    @property
    def change_direction_time(self):
        return self.__change_direction_time

    @property
    def life(self):
        return self.__life
        
    @property
    def rush_time(self):
        return self.__rush_time

    @property
    def activate_rush(self):
        return self.__activate_rush

    @property
    def stop_time(self):
        return self.__stop_time

    @property
    def stop(self):
        return self.__stop