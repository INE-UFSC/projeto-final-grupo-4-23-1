import pygame
from Sprites.Button.Button import Button
from States.State import State

class SelectProfile(State):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.create_button()
        print(self.all_profiles)

        self.__profile_selected = self.all_profiles[0]

    def screen_content(self) -> None:
        self.get_display().fill("black")

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        
        self.text("SELECT YOUR PROFILE", x_pos-200, y_pos-250, 50)
        self.text(self.profile_selected.name, x_pos, y_pos, 30)

    def create_button(self):
        x_pos = self.display_width//2
        y_pos = self.display_height//2

        back = Button(10, 10, "Back", self.back)
        self.all_sprites.add(back)

    def back(self) -> None:
        self.get_owner().change_state("MainMenu")


    def handle_update(self) -> None:
        pygame.display.update()
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()

    @property
    def all_profiles(self):
        return self.get_all_profiles()

    @property
    def profile_selected(self):
        return self.__profile_selected