import pygame
from Sprites.Button.Button import Button
from States.State import State


class MainMenu(State):
    def __init__(self, owner):
        super().__init__(owner)
        self.__all_sprites = pygame.sprite.Group()

        self.create_button()

    def create_button(self):

        x_pos = self.display_width//2 - 150
        y_pos = self.display_height//2


        play = Button(x_pos, y_pos-125, 'Play', self.play)
        self.all_sprites.add(play)

        select_profile = Button(x_pos, y_pos+25, "Select Profile", self.select_profile)
        self.all_sprites.add(select_profile)

        quit = Button(x_pos, y_pos+175, 'Quit', self.quit)
        self.all_sprites.add(quit)

    def select_profile(self):
        self.get_owner().change_state("SelectProfile")

    def play(self):
        self.get_owner().change_state("AsteroidGame")

    def quit(self):
        self.get_owner().close()

    def screen_content(self):
        self.get_display().fill("black")

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        self.text("-=-=ASTEROIDS-PLUS=-=-", x_pos-225, y_pos-250, 50)

    @property
    def all_sprites(self):
        return self.__all_sprites

    def handle_update(self):
        pygame.display.update()
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()
