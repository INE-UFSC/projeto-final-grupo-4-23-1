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

        newProfile = Button(self, x_pos, y_pos - 200, 300, 100, 'New Profile', self.new_profile)
        self.all_sprites.add(newProfile)

        selectProfile = Button(self, x_pos, y_pos - 50, 300, 100, 'Select Profile', self.select_profile)
        self.all_sprites.add(selectProfile)

        scoreboard = Button(self, x_pos, y_pos + 100, 300, 100, 'Scoreboard', self.scoreboard)
        self.all_sprites.add(scoreboard)

        quit = Button(self, x_pos, y_pos + 250, 300, 100, 'Quit', self.quit)
        self.all_sprites.add(quit)

        inc_volume = Button(self, self.display_width-180, y_pos-35, 70, 70, "+V", self.increase_volume)
        self.all_sprites.add(inc_volume)

        dec_volume = Button(self, self.display_width-90, y_pos-35, 70, 70, "-V", self.decrease_volume)
        self.all_sprites.add(dec_volume)

    def decrease_volume(self):
        self.get_sound_mixer().decrease_volume()

    def increase_volume(self):
        self.get_sound_mixer().increase_volume()

    def select_profile(self):
        self.get_owner().change_state("SelectProfile")

    def new_profile(self):
        self.get_owner().change_state("CreateProfile")

    def quit(self):
        self.get_owner().close()

    def scoreboard(self):
        self.get_owner().change_state("ScoreBoard")

    def screen_content(self):
        self.get_display().fill("black")

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        self.text("-=-=ASTEROIDS-PLUS=-=-", x_pos-225, y_pos-400, 50, "white")

        self.text("Volume:", self.display_width-160, y_pos-60, 30, "white")
        volume = int(self.get_sound_mixer().volume * 100)
        self.text(str(volume), self.display_width-80, y_pos-60, 30, "yellow")

    @property
    def all_sprites(self):
        return self.__all_sprites

    def handle_update(self):
        pygame.display.update()
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()
