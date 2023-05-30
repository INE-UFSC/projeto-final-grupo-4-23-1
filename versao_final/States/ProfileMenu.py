import pygame
from States.State import State

class ProfileMenu(State):
    def __init__(self, owner):
        super().__init__(owner)

        self.__current_profile = self.get_owner().game_data.profile

    def create_button(self):
        pass

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
        pygame.display.update()

    @property
    def current_profile(self):
        return self.__current_profile