import pygame
import math
from time import time

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, direction, speed: float, damage: int):
        super().__init__()
        self.__x = x
        self.__y = y
        self.__direction = -direction
        self.__speed = speed
        self.__damage = damage
        self.__lifetime = 1.0  # 5 pra desaparecer
        self.__criacao = time()

        self.cria_bullet()


    
    def cria_bullet(self):
        #cria imagem de um retangulo
        self.imagem_original = pygame.Surface([20, 3], pygame.SRCALPHA)
        #cria o retangulo com base na imagem
        pygame.draw.rect(self.imagem_original, ("yellow"), (0, 0 ,20 ,3))
        #rotaciona a imagem conforma a diracao da nave (dada no init)
        self.image = pygame.transform.rotate(self.imagem_original, -self.direction)
        #retangulo da bala
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)
    
    def update_image(self):
        
        self.image = pygame.transform.rotate(self.imagem_original, -self.direction)
        #retangulo da bala
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)
    


    def hit(self):
        self.kill()


    def update(self):
        # Obtém as dimensões da janela do jogo
        screen_width = pygame.display.Info().current_w
        screen_height = pygame.display.Info().current_h

        # Se a bala saiu da tela pela direita, teletransporta para o lado esquerdo
        if self.x > screen_width:
            self.__x = 0

        # Se a bala saiu da tela pela esquerda, teletransporta para o lado direito
        elif self.x < 0:
            self.__x = screen_width

        if self.y > screen_height:
            self.__y = 0

        elif self.y < 0:
            self.__y = screen_height

        # Calcula a nova posição da bala com base na direção e velocidade
        self.__x += self.speed * math.cos(math.radians(self.direction))
        self.__y += self.speed * math.sin(math.radians(self.direction))

        # Decrementa o tempo de vida da bala com base no tempo de atualização (assumindo 60 atualizações por segundo)
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

