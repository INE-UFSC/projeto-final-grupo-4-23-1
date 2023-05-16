import pygame
from math import cos, sin, radians
from os import path
from random import randint

pasta = path.dirname(__file__)

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, game, size: int = 2, position: tuple = None) -> None:
        super().__init__()
        #tamanho da tela
        self.__display_width = pygame.display.Info().current_w
        self.__display_height = pygame.display.Info().current_h

        #asteroidgame.py
        self.__game = game

        #tamanho / direção / impulso
        self.__size = size
        self.__direction = randint(0,360)
        self.__thrust = randint(3, 5)

        #pega o a imagem certa conforme o tamanho
        self.asteroid_size_image()
        self.__image = self.load_image

        #posição inicial
        self.start_position(position)

        #qtd de asteroids a dividir quando é destruido
        self.__asteroids_ramaining = 2

        #hitbox
        self.__rect = self.image.get_rect(center=(self.x, self.y))
        self.__mask = pygame.mask.from_surface(self.image)

    def asteroid_size_image(self) -> None:
        self.__load_image = pygame.image.load(pasta+f"//asteroid_{self.size}.png")
    
    def start_position(self, position: tuple) -> None:
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
    
    def update(self) -> None:

        self.update_coordenates()
        self.display_limit()
        self.update_position()
    
    def update_coordenates(self) -> None:
   
        self.__x += self.thrust * cos(radians(-self.direction))
        self.__y += self.thrust * sin(radians(-self.direction))


    def update_position(self) -> None:
        self.__image = pygame.transform.rotate(self.load_image, self.direction+90)
        self.__rect = self.image.get_rect(center = (self.x, self.y))  
        self.__mask = pygame.mask.from_surface(self.image)
    
    def display_limit(self) -> None:
        if (self.x >= self.display_width):
            self.__x = 1
    
        if (self.x <= 0):
            self.__x = self.display_width-1

        if (self.y >= self.display_height):
            self.__y = 1

        if (self.y  <= 0):
            self.__y = self.display_height-1
    
    def hit(self) -> None:
        if self.size > 0:
            for _ in range(self.asteroids_ramaining):
                asteroid = Asteroid(self.game, self.size - 1, (self.x, self.y))
                self.game.all_sprites.add(asteroid)
                self.game.all_asteroids.add(asteroid)

        self.kill()

    @property
    def mask(self):
        return self.__mask

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