import pygame
from States.State import State

class MainMenu(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)

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

    def screen_content(self):
        self.display.fill("black")
        self.text("MAIN MENU", 10, 10, 50)
