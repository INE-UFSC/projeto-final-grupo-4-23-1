import pygame
from Sprites.Button.Button import Button
from States.State import State
from Profiles.Profile import Profile

class Store(State):
    def __init__(self, owner):
        super().__init__(owner)

        self.__current_profile: Profile = self.get_owner().game_data.profile
        self.create_button()

    def create_button(self):
        x_pos = self.display_width//2 
        y_pos = self.display_height//2

        back = Button(20, 20, 180, 100, "<-- Back", self.back)
        self.all_sprites.add(back)

    def back(self):
        self.save_profile(self.current_profile)
        self.get_owner().change_state("ProfileMenu")

    def screen_content(self) -> None:
        self.get_display().fill("black")

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        self.text("STORE", x_pos-50, 20, 50, "white")

    def handle_update(self) -> None:
        pygame.display.update()
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()

    @property
    def current_profile(self) -> Profile:
        return self.__current_profile