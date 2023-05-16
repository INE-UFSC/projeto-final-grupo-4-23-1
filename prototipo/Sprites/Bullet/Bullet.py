import pygame
import math
from time import time

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, direction: int, speed: float, damage: int) -> None:
        super().__init__()
        self.__x = x
        self.__y = y
        self.__direction = -direction
        self.__speed = speed
        self.__damage = damage
        self.__lifetime = 1.0  # 5 pra desaparecer
        self.__criacao = time()

        self.__screen_width = pygame.display.Info().current_w
        self.__screen_height = pygame.display.Info().current_h


        self.cria_bullet()


    
    def cria_bullet(self) -> None:
        #cria imagem de um retangulo
        self.imagem_original = pygame.Surface([20, 3], pygame.SRCALPHA)
        #cria o retangulo com base na imagem
        pygame.draw.rect(self.imagem_original, ("yellow"), (0, 0 ,20 ,3))
        #rotaciona a imagem conforma a diracao da nave (dada no init)
        self.image = pygame.transform.rotate(self.imagem_original, -self.direction)
        #retangulo da bala
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)
    
    def update_image(self) -> None:
        
        self.image = pygame.transform.rotate(self.imagem_original, -self.direction)
        #retangulo da bala
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)
    
    def hit(self) -> None:
        self.kill()

    def update(self) -> None:
        # Obtém as dimensões da janela do jogo
        # Se a bala saiu da tela pela direita, teletransporta para o lado esquerdo
        if self.x > self.screen_width:
            self.__x = 0

        # Se a bala saiu da tela pela esquerda, teletransporta para o lado direito
        elif self.x < 0:
            self.__x = self.screen_width

        if self.y > self.screen_height:
            self.__y = 0

        elif self.y < 0:
            self.__y = self.screen_height

        # Calcula a nova posição da bala com base na direção e velocidade
        self.__x += self.speed * math.cos(math.radians(self.direction))
        self.__y += self.speed * math.sin(math.radians(self.direction))

        if time() - self.__criacao > self.lifetime:
            self.kill()
        
        self.update_image()

    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def direction(self):
        return self.__direction
    
    @property
    def speed(self):
        return self.__speed
    
    @property
    def damage(self):
        return self.__damage

    
    @property
    def lifetime(self):
        return self.__lifetime
    
    @property
    def criacao(self):
        return self.__criacao

    @property
    def screen_width(self):
        return self.__screen_width

    @property
    def screen_height(self):
        return self.__screen_height

