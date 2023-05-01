import pygame
from States.State import State
from Ship.Ship import Ship

class AsteroidGame(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)

        #grupo com todos os sprites
        self.__all_sprites = pygame.sprite.Group()
        #adiciona a nave
        self.add_ship()

        self.run()

    #adiciona a nave
    def add_ship(self):
        ship = Ship(2)
        self.all_sprites.add(ship)

    def run(self):
        while (self.playing == True):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.nextState("Sair")

            #apagar depois
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                self.nextState("MainMenu")
            #apagar depois

            pygame.display.update()

            #põe o conteudo da tela
            self.screen_content()

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
    def all_sprites(self):
        return self.__all_sprites