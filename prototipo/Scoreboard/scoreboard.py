import pygame
from Sprites.Button.Button import Button
from States.State import State

class Scoreboard(State):
    def __init__(self,scores):
        super().__init__(scores)
        self.__all_sprites = pygame.sprite.Group()

        self.create_button()
    
    def create_button(self):

        x_pos = self.display_width//2 - 150
        y_pos = self.display_height//2


        back = Button(x_pos, y_pos+25, 'Back', self.back)
        self.all_sprites.add(back)

    def back(self):
        self.get_owner().change_state("AsteroidGame")

    def screen_content(self):
        self.get_display().fill("black")

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        self.text("-=-=ASTEROIDS-PLUS=-=-", x_pos-225, y_pos-250, 50)

    @property
    def all_sprites(self):
        return self.__all_sprites

    def handle_update(self):
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()

        