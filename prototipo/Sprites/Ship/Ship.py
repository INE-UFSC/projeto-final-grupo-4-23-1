import pygame
from math import cos, sin, radians
from os import path
from time import time

pasta = path.dirname(__file__)

class Ship(pygame.sprite.Sprite):
    def __init__(self, speed: float, vel_max: float) -> None:
        super().__init__()

        #tempo do ultimo tiro
        self.__last_shoot = 0

        #altura e largura da tela
        self.__display_width = pygame.display.Info().current_w
        self.__display_height = pygame.display.Info().current_h

        #posição inicial
        self.__x = int((self.display_width)/2)
        self.__y = int((self.display_height)/2)

        self.__vel_max = vel_max

        #direção, impulso e rotação inicial
        self.__direction = 90
        self.__thrust = speed
        self.__dx = 0
        self.__dy = 0

        #carrega imagem 
        self.__load_image = pygame.image.load(pasta+"//ship.png")
        self.__image = self.load_image

        #marca o hitbox
        self.__rect = self.image.get_rect(center = (self.x, self.y))
        self.__mask = pygame.mask.from_surface(self.image)

    def user_input(self) -> None:
        keys = pygame.key.get_pressed()

        #tecla W -> acelera
        if (keys[pygame.K_w]):
            self.accelerate()

        #tecla a -> rotaciona no sentido antihorario
        if (keys[pygame.K_a]):
            self.__direction += 3.75

        #tecla d -> rotaciona no sentido horario
        if (keys[pygame.K_d]):
            self.__direction -= 3.75


    #metodo que chama bulet, com o tempo minimo entre eles de 0.5sec
    def shoot(self) -> bool:
        if pygame.key.get_pressed()[pygame.K_SPACE]:

            if ((time() - self.last_shoot) > 0.5):
                self.__last_shoot = time()
                return True
            
            else:
                return False
        else:
            return False
                

    def hit(self) -> None:
        pass

    #acelera
    def accelerate(self) -> None:
        self.__dx += cos(radians(self.direction)) * self.thrust/8
        self.__dy += sin(radians(-self.direction)) * self.thrust/8

        if (abs(self.dx) > self.vel_max):
            self.__dx = -self.vel_max if (self.dx < 0) else self.vel_max
        if (abs(self.dy) >= self.vel_max):
            self.__dy = -self.vel_max if (self.dy < 0) else self.vel_max

    #atualiza o impulso e a rotação
    def update_position(self) -> None:
        #diminui a rotação e o impulso, confor o metodo update é chamado

        self.__dx /= 1.01
        self.__dy /= 1.01

        #altera x e y da nave, conforme a inpulso e a diração
        self.__x += self.dx
        self.__y += self.dy

    #atualiza imagem e hitbox, conforme a posição
    def update_image_position(self) -> None:
        self.__image = pygame.transform.rotate(self.load_image, self.direction-90)
        self.__rect = self.image.get_rect(center = (self.x, self.y))
        self.__mask = pygame.mask.from_surface(self.image)

    #teletransporta para o outro lado da tela
    def display_limit(self) -> None:
        if (self.x >= self.display_width):
            self.__x = 1
    
        if (self.x <= 0):
            self.__x = self.display_width-1

        if (self.y >= self.display_height):
            self.__y = 1

        if (self.y  <= 0):
            self.__y = self.display_height-1

    #metodo UPDATE, todo sprite deve ter
    # é chamado com o o self.all_sprites é atualizado(esta no asteroid game)
    def update(self) -> None:
        self.user_input()
        self.update_image_position()
        self.display_limit()
        self.update_position()

    @property
    def vel_max(self):
        return self.__vel_max

    @property
    def mask(self):
        return self.__mask

    @property
    def dx(self):
        return self.__dx

    @property
    def dy(self):
        return self.__dy

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


