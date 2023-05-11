import pygame
from math import cos, sin, radians
from os import path
from random import randint

pasta = path.dirname(__file__)

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, game, size = 2, position = None):
        super().__init__()
        self.__display_width = pygame.display.Info().current_w
        self.__display_height = pygame.display.Info().current_h
        self.__game = game
        self.__size = size
        self.__direction = randint(0,360)
        self.__thrust = 5
        self.__load_image = pygame.image.load(pasta+"//asteroid.png")
        self.__image = self.load_image
        self.start_position(position)
        self.__asteroids_ramaining = 2
        self.__rect = self.image.get_rect(center=(self.x, self.y))

    
    def start_position(self, position):
        if position == None:
            random_side = randint(1,4)
            if random_side == 1:
                self.__x = 0
                self.__y = randint(0, self.display_height)
            elif random_side == 2:
                self.__x = randint(0, self.display_width)
                self.__y = 0
            elif random_side == 2:
                self.__x = self.display_width
                self.__y = randint(0, self.display_height)
            else:
                self.__x = randint(0, self.display_width)
                self.__y = self.display_height
            
        else:
            self.__x = position[0]
            self.__y = position[1]
    
    def update(self):

        self.update_coordenates()
        self.display_limit()
        self.update_position()
    
    def update_coordenates(self):
   
        self.__x += self.thrust * cos(radians(-self.direction))
        self.__y += self.thrust * sin(radians(-self.direction))


    def update_position(self):
        self.__image = pygame.transform.rotate(self.load_image, self.direction+90)
        self.__rect = self.image.get_rect(center = (self.x, self.y))  
    
    def display_limit(self):
        if (self.x >= self.display_width):
            self.__x = 1
    
        if (self.x <= 0):
            self.__x = self.display_width-1

        if (self.y >= self.display_height):
            self.__y = 1

        if (self.y  <= 0):
            self.__y = self.display_height-1
    
    def hit(self):
        print('acertou o asteroid')
        if self.size > 0:
            for i in range(self.asteroids_ramaining):
                asteroid = Asteroid(self.game, self.size - 1, (self.x, self.y))
                self.game.all_sprites.add(asteroid)
                self.game.all_asteroids.add(asteroid)

        self.kill()

    @property 
    def speed(self):
        return self.__speed
    
    @property
    def rotation(self):
        return self.__rotation

    @property
    def last_shoot(self):
        return self.__last_shoot

    @property
    def display_width(self):
        return self.__display_width    
    
    @property
    def display_height(self):
        return self.__display_height

    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image

    @property
    def load_image(self):
        return self.__load_image

    @property
    def rotation(self):
        return self.__rotation

    @property
    def thrust(self):
        return self.__thrust

    @property
    def direction(self):
        return self.__direction
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    @property
    def size(self):
        return self.__size

    @property
    def asteroids_ramaining(self):
        return self.__asteroids_ramaining
    
    @property 
    def game(self):
        return self.__game