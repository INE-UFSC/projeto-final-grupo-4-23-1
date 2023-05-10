import pygame
from Button import Button
from States.State import State

class MainMenu(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.__all_sprites = pygame.sprite.Group()

        self.create_button()
        self.run()

    def create_button(self):
        play = Button(250, 150, 'Jogar', self.play)
        self.all_sprites.add(play)
        quit = Button(250, 300, 'Sair', self.quit)
        self.all_sprites.add(quit)

    def play(self):
        self.nextState("AsteroidGame")

    def quit(self):
        self.nextState("Sair")

    def run(self):
        while (self.playing == True):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.nextState("Sair")

            pygame.display.update()

            self.screen_content()

            self.all_sprites.update()
            self.all_sprites.draw(self.display)

            pygame.display.update()

    def screen_content(self):
        self.display.fill("black")

    @property
    def all_sprites(self):
        return self.__all_sprites
