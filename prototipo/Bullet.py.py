import pygame
import math

class Bullet:
    def __init__(self, x: int, y: int, direction, speed: float, damage: int):
        super().__init__()
        self.__x = x
        self.__y = y
        self.__direction = direction
        self.__speed = speed
        self.__damage = damage
        self.__alive = True
        self.__lifetime = 5.0  # 5 pra desaparecer


    
    def cria_bullet(self):
        #cria imagem de um retangulo
        self.imagem_original = pygame.Surface([20, 3], pygame.SRCALPHA)
        #cria o retangulo com base na imagem
        pygame.draw.rect(self.imagem_original, ("yellow"), (0, 0 ,20 ,3))
        #rotaciona a imagem conforma a diracao da nave (dada no init)
        self.image = pygame.transform.rotate(self.imagem_original, -self.direcao)
        #retangulo da bala
        self.rect = self.image.get_rect(center = (self.x, self.y))


    
    def detecta_colisao(self):
        #lista de booleanos quando é detectado colisao entre a bala e o grupo de asteroids
        hitlist = pygame.sprite.spritecollide(self, self.jogo.todos_asteroids, True)
        if hitlist:
            for sprite in hitlist:
                sprite.hit()

            self.kill()



    def update(self):
        # Obtém as dimensões da janela do jogo
        screen_width, screen_height = pygame.display.get_surface().get_size()

        # Se a bala saiu da tela pela direita, teletransporta para o lado esquerdo
        if self.x > screen_width:
            self.x = 0

        # Se a bala saiu da tela pela esquerda, teletransporta para o lado direito
        elif self.x < 0:
            self.x = screen_width
        # Calcula a nova posição da bala com base na direção e velocidade
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)
        # Decrementa o tempo de vida da bala com base no tempo de atualização (assumindo 60 atualizações por segundo)
        self.lifetime -= 1.0 / 60.0  # 60 FPS
        # Verifica se a vida útil da bala acabou
        if self.lifetime <= 0:
            self.alive = False # define o status da bala como 'morta' quando a vida útil acaba
    
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
    def alive(self):
        return self.__alive
    
    @property
    def lifetime(self):
        return self.__lifetime

    @x.setter
    def x (self, x):
        self.__x = x
    
    @y.setter
    def y (self, y):
        self.__y = y
    
    @direction.setter
    def direction (self, direction):
        self.__direction = direction

    @speed.setter
    def speed(self,speed):
        self.__speed = speed
    
    @damage.setter
    def damage(self, damage):
        self.__damage = damage
    
    @alive.setter
    def alive(self, alive):
        self.__alive = alive
    
    @lifetime.setter
    def lifetime(self,lifetime):
        self.__lifetime = lifetime