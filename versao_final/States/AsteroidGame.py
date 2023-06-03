import pygame
from States.State import State
from Sprites.Ship.Ship import Ship
from Sprites.Asteroid.Asteroid import Asteroid
from Sprites.BasicEnemy.BasicEnemy import BasicEnemy
from CollisionManager.CollisionManager import CollisionManager
from time import time


class AsteroidGame(State):
    def __init__(self, owner):
        super().__init__(owner)

        #collision manager
        self.__collision_manager = CollisionManager(self)

        #tempo do ultimo asteroid e inimigo
        self.__last_asteroid_time = time()
        self.__last_basic_enemy_time = time()

        #pontuação -> 1 por asteroid aki no protopipo
        self.__score = 0
        #tempo que começou o jogo
        self.__init_time = time()

        #grupo com todos os sprites
        self.__all_sprites = pygame.sprite.Group()
        #grupo so de asteroids
        self.__all_asteroids = pygame.sprite.Group()
        #grupo so da nave (feito para o sistema de colisao)
        self.__ship_group = pygame.sprite.Group()
        #grupo bullet
        self.__ship_bullets_group = pygame.sprite.Group()
        #grupo enemy
        self.__enemy_group = pygame.sprite.Group()
        self.__enemy_bullets_group = pygame.sprite.Group()

        #adiciona a nave
        self.add_ship()

        #adiciona asteroid inicial
        asteroid = Asteroid(self)
        self.all_sprites.add(asteroid)
        self.all_asteroids.add(asteroid)

        #clock
        self.__ck = pygame.time.Clock()

    #adiciona a nave
    def add_ship(self):
        self.ship = Ship(game=self, speed=2, vel_max=10, cooldown=0.5, life=3)
        self.all_sprites.add(self.ship)
        self.ship_group.add(self.ship)
    
    def add_asteroid(self):
        if (time() - self.last_asteroid_time) > 5:
            asteroid = Asteroid(self)

            self.all_sprites.add(asteroid)
            self.all_asteroids.add(asteroid)

            self.__last_asteroid_time = time()

    def add_basic_enemy(self):
        if (time() - self.last_basic_enemy_time) > 8:
            enemy = BasicEnemy(game=self, life=1)

            self.all_sprites.add(enemy)
            self.enemy_group.add(enemy)

            self.__last_basic_enemy_time = time()

            
    #conteudo da tela
    def screen_content(self):
        self.get_display().fill("black")
        self.text("You Survived: %.1f " % (time() - self.init__time), 10, 10, 30)
        self.text("Score: %d" % self.score, 10, 37, 30)
        self.text("Life: %d" % self.ship.life, 10, 64, 30)

        #adiciona asteroid a cada 5s
        self.add_asteroid()
        #adiciona inimigo basico a cada 8s
        self.add_basic_enemy()

    #atualiza a tela
    def handle_update(self):
        self.ck.tick(60)
        pygame.display.update()

        #põe o conteudo da tela
        self.screen_content()
        #colisoes
        self.collision_manager.collisions()
        #atualiza todos os sprites(chama o metodo update de todos os sprites do grupo)
        self.update_all_sprites()

        pygame.display.update()

    #lida com a transição de estados
    def handle_transition(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.get_owner().change_state("Result")
        super().handle_transition()
    
    #atualiza todos os sprites
    def update_all_sprites(self):
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())

    def set_score(self, v: int) -> None:
        self.__score = v

    @property
    def collision_manager(self):
        return self.__collision_manager

    @property
    def enemy_bullets_group(self):
        return self.__enemy_bullets_group

    @property
    def enemy_group(self):
        return self.__enemy_group

    @property
    def last_basic_enemy_time(self):
        return self.__last_basic_enemy_time

    @property
    def score(self):
        return self.__score

    @property
    def all_asteroids(self):
        return self.__all_asteroids

    @property
    def ship_group(self):
        return self.__ship_group

    @property
    def init__time(self):
        return self.__init_time

    @property
    def ck(self):
        return self.__ck

    @property
    def all_sprites(self):
        return self.__all_sprites
    
    @property
    def last_asteroid_time(self):
        return self.__last_asteroid_time
    
    @property
    def ship_bullets_group(self):
        return self.__ship_bullets_group
