import pygame
from States.State import State
from Ship.Ship import Ship
from Asteroid.Asteroid import Asteroid
from CollisionManager.CollisionManager import CollisionManager
from time import time
class AsteroidGame(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)

        self.__last_asteroid_time = time()

        #tempo que começou o jogo
        self.__init_time = time()

        #grupo com todos os sprites
        self.__all_sprites = pygame.sprite.Group()
        #grupo so de asteroids
        self.__all_asteroids = pygame.sprite.Group()
        #grupo so da nave (feito para o sistema de colisao)
        self.__ship_group = pygame.sprite.Group()

        #adiciona a nave
        self.add_ship()

        #adiciona asteroid inicial
        asteroid = Asteroid(self)
        self.all_sprites.add(asteroid)
        self.all_asteroids.add(asteroid)

        #clock
        self.__ck = pygame.time.Clock()

        self.run()

    #adiciona a nave
    def add_ship(self):
        ship = Ship(5)
        self.all_sprites.add(ship)
        self.ship_group.add(ship)
    
    def add_asteroid(self):
        if (time() - self.last_asteroid_time) > 5:
            asteroid = Asteroid(self)

            self.all_sprites.add(asteroid)
            self.all_asteroids.add(asteroid)

            self.__last_asteroid_time = time()

    def run(self):
        while (self.playing == True):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.nextState("Sair")

            #fps
            self.ck.tick(60)
            
            pygame.display.update()

            #põe o conteudo da tela
            self.screen_content()
            
            #adiciona asteroid a cada 5s
            self.add_asteroid()

            #colisoes
            self.collisions()
            
            #atualiza todos os sprites(chama o metodo update de todos os sprites do grupo)
            self.update_all_sprites()

            pygame.display.update()

    def collisions(self):
        collisions = CollisionManager(self.ship_group, self.all_asteroids)

        #colisao ship <-> asteroid
        if (collisions.collision_asteroid_ship()):
            self.state_machine.set_alive_time(time() - self.init__time)
            self.nextState("Result")

    #conteudo da tela
    def screen_content(self):
        self.display.fill("black")
        self.text("Você sobreviveu: %.1f " % (time() - self.init__time), 10, 10, 30)

    #atualiza todos os sprites
    def update_all_sprites(self):
        self.all_sprites.update()
        self.all_sprites.draw(self.display)

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