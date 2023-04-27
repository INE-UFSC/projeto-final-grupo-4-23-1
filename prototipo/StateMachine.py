import pygame
from States.MainMenu import MainMenu
from States.AsteroidGame import AsteroidGame

class StateMachine:
    def __init__(self):
        self.__state = "MainMenu"
        self.__working = True

    @property
    def state(self):
        return self.__state

    @property
    def working(self):
        return self.__working

    def change_state(self, nextState):
        self.__state = nextState

    def state_manager(self):
        while (self.working):
            if (self.state == "MainMenu"):
                MainMenu(self)
            if (self.state == "AsteroidGame"):
                AsteroidGame(self)

            if (self.state == "Sair"):
                pygame.quit()
