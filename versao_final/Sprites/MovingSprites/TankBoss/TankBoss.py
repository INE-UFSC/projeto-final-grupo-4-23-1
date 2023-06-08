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
        self.__invunerable_time = time()
        self.__invunerable = False
        self.__stop = False
        self.__activate_rush = False


        speed = 5
        direction = randint(0, 360)
        original_image = pygame.image.load(pasta+"//TankBoss.png")
        super().__init__(game, speed, -direction, original_image, position)

    def hit(self) -> None:
        if ((self.activate_rush == False) and (self.invunerable == False)):

            self.__life -= self.game.ship.damage

            self.__invunerable = True
            self.__invunerable_time = time()

            image = pygame.image.load(pasta+"//TankBoss_rush.png")
            self.set_original_image(image)

            if (self.life <= 0):
                self.kill()

    def set_life(self, life: int):
        self.__life = life

    def update_image_position(self) -> None:
        image = self.original_image
        self.set_image(image)
        self.set_rect(self.image.get_rect(center = (self.x, self.y)))
        self.set_mask(pygame.mask.from_surface(self.image))

    def change_direction(self) -> None:
        if (self.activate_rush == False):
            if ((time() - self.change_direction_time) > 3):

                direction = randint(0, 360)
                self.set_speed(5)
                image = pygame.image.load(pasta+"//TankBoss.png")
                self.set_original_image(image)
                self.set_direction(direction)

                self.__change_direction_time = time()

    def check_invunerable(self) -> None:
        if (self.invunerable == True):
            if ((time() - self.invunerable_time) > 1.5):
                self.__invunerable = False

    def rush(self) -> None:
        if (self.activate_rush == False):
            if ((time() - self.rush_time) > 8):
                self.__activate_rush = True
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
                self.__invunerable = True
                self.__invunerable_time = time()

    def red(self):
        if (self.invunerable == True) or (self.activate_rush == True):
            image = pygame.image.load(pasta+"//TankBoss_rush.png")
        else:
            image = pygame.image.load(pasta+"//TankBoss.png") 

        self.set_original_image(image)

    def update_position(self) -> None:
        if (self.stop == False):
            super().update_position()

    def update(self) -> None:
        self.change_direction()
        self.red()
        self.rush()
        self.check_invunerable()
        super().update()

    @property
    def invunerable(self):
        return self.__invunerable

    @property
    def invunerable_time(self):
        return self.__invunerable_time

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