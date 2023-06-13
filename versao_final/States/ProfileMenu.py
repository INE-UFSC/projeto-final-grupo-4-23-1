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

        play_normal = Button(self, x_pos-315, y_pos-200, 300, 100, 'Normal Mode', True, self.play_normal)
        self.all_sprites.add(play_normal)

        play_only_boss = Button(self, x_pos+15, y_pos-200, 300, 100, 'Only Boss Mode', True, self.play_only_boss)
        self.all_sprites.add(play_only_boss)

        store = Button(self, x_pos-150, y_pos-50, 300, 100, 'Store', True, self.store)
        self.all_sprites.add(store)

        exit = Button(self, x_pos-150, y_pos+100, 300, 100, 'Exit Profile', True, self.exit_profile)
        self.all_sprites.add(exit)

    def exit_profile(self) -> None:
        self.get_owner().change_state("MainMenu")

    def store(self) -> None:
        self.get_owner().change_state("Store")

    def play_only_boss(self) -> None:
        self.get_game_data().set_only_boss_mode(True)
        self.get_owner().change_state("BossTransition")

    def play_normal(self) -> None:
        self.get_game_data().set_only_boss_mode(False)
        self.get_owner().change_state("NormalLevel")

    def screen_content(self) -> None:

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        self.text("Max Score:", 20, 20, 40, "white")
        self.text(str(self.current_profile.max_score), 180, 20, 40, "yellow")

        self.text(self.current_profile.name, x_pos-50, 20, 50, "yellow")

        self.text("Credit:", self.display_width-220, 20, 40, "white")
        self.text("%.1f"%self.current_profile.credit, self.display_width-120, 20, 40, "yellow")

    def handle_update(self) -> None:
        pygame.display.update()
        self.background()
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()

    @property
    def current_profile(self) -> Profile:
        return self.__current_profile