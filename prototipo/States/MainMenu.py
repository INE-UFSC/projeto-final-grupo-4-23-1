import pygame
from States.State import State
from prototipo.Button import Button

class MainMenu(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)

        self.__all_sprites = pygame.sprite.Group()

        self.create_buttons()

        self.run()

    def run(self):
        while (self.playing == True):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.nextState("Sair")

            pygame.display.update()

            #apagar depois
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.nextState("AsteroidGame")
            #apagar depois

            self.screen_content()

            pygame.display.update()

    def play(self):
        print("Play the game!")

    def quit(self):
        print("Quit the game")

    def screen_content(self):
        self.display.fill("black")

    def create_buttons(self):
        play_asteroids = Button(50, 150, "Play Asteroids", self.play)
        quit_menu = Button(50, 300, "Quit", self.quit)
        self.all_sprites.add(play_asteroids)
        self.all_sprites.add(quit_menu)

    @property
    def all_sprites(self):
        return self.__all_sprites
