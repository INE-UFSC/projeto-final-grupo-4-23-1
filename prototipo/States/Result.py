import pygame
from States.State import State

class Result(State):
    def __init__(self, owner):
        super().__init__(owner)
        self.__alive_time = self.get_result().get_alive_time()
        self.__score = self.get_result().get_score()

    def screen_content(self):
        self.get_display().fill("black")

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        self.text("You Survived %.1f sec" % (self.alive_time), x_pos-150, y_pos-100, 50)
        self.text("Score: %d" % self.score, x_pos-65, y_pos-50, 50)
        self.text("Press SPACE to go back", x_pos-110, y_pos+50, 30)

    def handle_transition(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.get_owner().change_state("MainMenu")
        super().handle_transition()

    def handle_update(self):
        pygame.display.update()
        self.screen_content()
        pygame.display.update()

    @property
    def score(self):
        return self.__score

    @property
    def alive_time(self):
        return self.__alive_time

