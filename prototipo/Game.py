import pygame
from StateMachine import StateMachine

class Game:
    def __init__(self):
        pygame.init()

        self.__display_width = 800
        self.__display_height = 600

        self.state_machine = StateMachine()

    @property
    def display_width(self):
        return self.__display_width

    @property
    def display_height(self):
        return self.__display_height

    def run(self):
        self.display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("ASTEROIDS")

        self.state_machine.state_manager()

Game().run()

