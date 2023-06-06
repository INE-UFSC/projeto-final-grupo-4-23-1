import pygame
from Sprites.Button.Button import Button
from Profiles.Profile import Profile
from States.State import State

class ProfileMenu(State):
    def __init__(self, owner):
        super().__init__(owner)

        self.__current_profile: Profile = self.get_owner().game_data.profile
        self.create_button()

    def create_button(self):
        x_pos = self.display_width//2
        y_pos = self.display_height//2

        play = Button(x_pos-150, y_pos-200, 300, 100, 'Play', self.play)
        self.all_sprites.add(play)

        store = Button(x_pos-150, y_pos-50, 300, 100, 'Store', self.store)
        self.all_sprites.add(store)

        exit = Button(x_pos-150, y_pos+100, 300, 100, 'Exit Profile', self.exit_profile)
        self.all_sprites.add(exit)

    def exit_profile(self) -> None:
        self.get_owner().change_state("MainMenu")

    def store(self) -> None:
        self.get_owner().change_state("Store")

    def play(self) -> None:
        self.get_owner().change_state("BossLevel")

    def screen_content(self) -> None:
        self.get_display().fill("black")

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        self.text("Max Score:", 20, 20, 40, "white")
        self.text(str(self.current_profile.max_score), 180, 20, 40, "yellow")

        self.text(self.current_profile.name, x_pos-50, 20, 50, "yellow")

        self.text("Credit:", self.display_width-220, 20, 40, "white")
        self.text(str(self.current_profile.credit), self.display_width-120, 20, 40, "yellow")

    def handle_update(self) -> None:
        pygame.display.update()
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()

    @property
    def current_profile(self) -> Profile:
        return self.__current_profile