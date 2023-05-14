import pygame
from Button import Button
from States.State import State


class MainMenu(State):
    def __init__(self, owner):
        super().__init__(owner)
        self.__all_sprites = pygame.sprite.Group()

        self.create_button()

    def create_button(self):
        play = Button(250, 150, 'Jogar', self.play)
        self.all_sprites.add(play)
        quit = Button(250, 300, 'Sair', self.quit)
        self.all_sprites.add(quit)

    def play(self):
        self.get_owner().change_state("AsteroidGame")

    def quit(self):
        self.get_owner().close()

    def screen_content(self):
        self.get_display().fill("black")
        self.text("-=-=ASTEROIDS=-=-", 230, 30, 50)

    @property
    def all_sprites(self):
        return self.__all_sprites

    def handle_transition(self):
        super().handle_transition()
    
    def handle_update(self):
        pygame.display.update()
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()
