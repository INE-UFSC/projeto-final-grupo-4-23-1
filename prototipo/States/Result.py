import pygame
from States.State import State

class Result(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)

        self.__alive_time = state_machine.alive_time

        self.run()
       
    def run(self):
        while (self.playing):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.nextState("Sair")

            pygame.display.update()

            #talvez mudar depois
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_2]):
                self.nextState("MainMenu")
            #talvez mudar deopis1

            self.screen_content()

            pygame.display.update()

    def screen_content(self):
        self.display.fill("black")
        self.text("Voce sobreviveu %.1f sec" % (self.alive_time), 300, 300, 50)
        self.text("RESULT", 10, 10 ,30)
        self.text("Aperte 2 para sair", 50, 50, 40)

    @property
    def alive_time(self):
        return self.__alive_time