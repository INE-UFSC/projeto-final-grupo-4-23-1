import pygame
from Sprites.MovingSprite import MovingSprite
from Sprites.Bullet.Bullet import Bullet
from math import cos, sin, radians
from os import path
from time import time

pasta = path.dirname(__file__)

class Ship(MovingSprite):
    def __init__(self, game,
                 speed: float,
                 vel_max: float,
                 cooldown: float,
                 life: int) -> None:

        #tempo do ultimo tiro
        self.__last_shoot = 0

        #posição inicial
        x = pygame.display.Info().current_w // 2
        y = pygame.display.Info().current_h // 2

        #direção, impulso e rotação inicial
        self.__cooldown = cooldown
        self.__life = life
        self.__vel_max = vel_max
        self.__speed = speed
        self.__dx = 0
        self.__dy = 0

        #carrega imagem 
        image = pygame.image.load(pasta+"//ship.png")
        image = pygame.transform.rotate(image, -90)
        super().__init__(game, self.speed, 90, image, (x, y))

    def user_input(self) -> None:
        keys = pygame.key.get_pressed()

        #tecla W -> acelera
        if (keys[pygame.K_w]):
            self.accelerate()

        #tecla a -> rotaciona no sentido antihorario
        if (keys[pygame.K_a]):
            d = self.direction + 3.75
            self.set_direction(d)

        #tecla d -> rotaciona no sentido horario
        if (keys[pygame.K_d]):
            d = self.direction - 3.75
            self.set_direction(d)

        if (keys[pygame.K_SPACE]):
            self.shoot()


    #metodo que chama bulet, com o tempo minimo entre eles de self.cooldown sec
    def shoot(self) -> None:
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if ((time() - self.last_shoot) > self.cooldown):
                bullet = Bullet(self, (self.x, self.y), self.direction, 10, 5, "yellow", 1)
                self.game.all_sprites.add(bullet)
                self.game.bullets_group.add(bullet)

                self.__last_shoot = time()

    def hit(self) -> None:
        self.__life -= 1

        x = self.display_width//2
        y = self.display_height//2
        self.set_pos(x, y)
        self.reset_speed()
                

    #acelera
    def accelerate(self) -> None:
        self.__dx += cos(radians(self.direction)) * self.speed/8
        self.__dy += sin(radians(-self.direction)) * self.speed/8

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
        x = self.x + self.dx
        y = self.y + self.dy
        self.set_pos(x, y)

    #metodo UPDATE, todo sprite deve ter
    # é chamado com o o self.all_sprites é atualizado(esta no asteroid game)
    def update(self) -> None:
        self.user_input()
        super().update()

    def reset_speed(self):
        self.__dx = 0
        self.__dy = 0

    @property
    def life(self):
        return self.__life

    @property
    def cooldown(self):
        return self.__cooldown

    @property
    def speed(self):
        return self.__speed

    @property
    def vel_max(self):
        return self.__vel_max

    @property
    def dx(self):
        return self.__dx

    @property
    def dy(self):
        return self.__dy

    @property
    def last_shoot(self):
        return self.__last_shoot


