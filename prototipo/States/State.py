import pygame
from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, state_machine):
        #maquina de estados
        self.state_machine = state_machine
        self.__playing = True

        #pega a tela
        self.display = pygame.display.get_surface()

    @property
    def playing(self):
        return self.__playing

    #metodo para chamar o proximo estado
    def nextState(self, nextState):
        self.state_machine.change_state(nextState)
        self.__playing = False

    #metodo geral para colocar texto
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