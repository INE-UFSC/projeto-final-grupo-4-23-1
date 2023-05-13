import pygame
from States.MainMenu import MainMenu
from States.Result import Result
from States.AsteroidGame import AsteroidGame

class StateMachine:
    def __init__(self):
        self.__state = "MainMenu"
        self.__working = True
        self.__alive_time = 0
        self.__score = 0

    @property
    def state(self):
        return self.__state

    @property
    def working(self):
        return self.__working

    @property
    def alive_time(self):
        return self.__alive_time

    @property
    def score(self):
        return self.__score

    def set_alive_time(self, v):
        self.__alive_time = v

    def set_score(self, v):
        self.__score = v

    def change_state(self, nextState):
        self.__state = nextState

    def state_manager(self):
        while (self.working):
            if (self.state == "MainMenu"):
                MainMenu(self)
            if (self.state == "AsteroidGame"):
                AsteroidGame(self)
            if (self.state == "Result"):
                Result(self)
            if (self.state == "Sair"):
                pygame.quit()
                break
