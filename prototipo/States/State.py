import pygame
from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, state_machine):
        self.state_machine = state_machine
        self.__playing = True

        self.display = pygame.display.get_surface()

        self.run()

    @property
    def playing(self):
        return self.__playing

    def nextState(self, nextState):
        self.state_machine.change_state(nextState)
        self.__playing = False

    def text(self, text, x, y, size):
        self.font = pygame.font.SysFont(None, size)
        textSurface = self.font.render(text, True, ("white"))
        self.display.blit(textSurface, (x, y))

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def screen_content(self):
        pass