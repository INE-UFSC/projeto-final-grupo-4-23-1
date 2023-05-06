import pygame
from States.State import State
from Ship.Ship import Ship
from Asteroid.Asteroid import Asteroid
from time import time
class AsteroidGame(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.__last_asteroid_time = time()
        #grupo com todos os sprites
        self.__all_sprites = pygame.sprite.Group()
        #adiciona a nave
        self.add_ship()
        #adiciona asteroid inicial
        self.all_sprites.add(Asteroid(self))

        #clock
        self.__ck = pygame.time.Clock()

        self.run()

    #adiciona a nave
    def add_ship(self):
        ship = Ship(10)
        self.all_sprites.add(ship)
    
    def add_asteroid(self):
        current_time = time()
        if (current_time - self.last_asteroid_time) > 5:
            asteroid = Asteroid(self)
            self.all_sprites.add(asteroid)
            self.__last_asteroid_time = time()

    def run(self):
        while (self.playing == True):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.nextState("Sair")

            #fps
            self.ck.tick(60)
            
            #apagar depois
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                self.nextState("MainMenu")
            #apagar depois

            pygame.display.update()

            #põe o conteudo da tela
            self.screen_content()
            
            #adiciona asteroid a cada 5s
            self.add_asteroid()
            
            #atualiza todos os sprites(chama o metodo update de todos os sprites do grupo)
            self.update_all_sprites()

            pygame.display.update()

    #conteudo da tela
    def screen_content(self):
        self.display.fill("black")
        self.text("ASTEROID GAME", 100, 100, 30)
        self.text("tecla 1 para mudar de estado", 10, 10, 50)

    #atualiza todos os sprites
    def update_all_sprites(self):
        self.all_sprites.update()
        self.all_sprites.draw(self.display)

    @property
    def ck(self):
        return self.__ck

    @property
    def all_sprites(self):
        return self.__all_sprites
    
    @property
    def last_asteroid_time(self):
        return self.__last_asteroid_time