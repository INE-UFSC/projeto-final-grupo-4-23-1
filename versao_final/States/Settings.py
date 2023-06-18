import pygame
from Entities.Button.Button import Button
from States.State import State


class Settings(State):
    def __init__(self, owner):
        super().__init__(owner)
        self.__all_sprites = pygame.sprite.Group()

        self.create_button()

    def create_button(self):

        x_pos = self.display_width // 2
        y_pos = self.display_height // 2

        back = Button(self, 20, 20, 180, 100, "<-- Back", True, self.back)
        self.all_sprites.add(back)

        # volume buttons
        mute_sfx = Button(self, x_pos - 95, y_pos - 80, 70, 70, "M", True, self.mute_unmute_sfx)
        self.all_sprites.add(mute_sfx)

        inc_sfx_volume = Button(self, x_pos - 5, y_pos - 80, 70, 70, "+V", True,
                                self.increase_sfx_volume)
        self.all_sprites.add(inc_sfx_volume)

        dec_sfx_volume = Button(self, x_pos + 85, y_pos - 80, 70, 70, "-V", True, self.decrease_sfx_volume)
        self.all_sprites.add(dec_sfx_volume)

        mute_music = Button(self, x_pos - 95, y_pos + 35, 70, 70, "M", True, self.mute_unmute_music)
        self.all_sprites.add(mute_music)

        inc_music_volume = Button(self, x_pos - 5, y_pos + 35, 70, 70, "+V", True,
                                  self.increase_music_volume)
        self.all_sprites.add(inc_music_volume)

        dec_music_volume = Button(self, x_pos + 85, y_pos + 35, 70, 70, "-V", True,
                                  self.decrease_music_volume)
        self.all_sprites.add(dec_music_volume)

    def mute_unmute_sfx(self):
        self.get_sound_mixer().mute_unmute_sfx()

    def mute_unmute_music(self):
        self.get_sound_mixer().mute_unmute_music()
        if (self.get_sound_mixer().mute_music):
            pygame.mixer.stop()
        else:
            self.get_sound_mixer().play_theme_music()

    def increase_music_volume(self):
        pygame.mixer.stop()
        self.get_sound_mixer().increase_music_volume()
        self.get_sound_mixer().play_theme_music()

    def decrease_music_volume(self):
        pygame.mixer.stop()
        self.get_sound_mixer().decrease_music_volume()
        self.get_sound_mixer().play_theme_music()

    def decrease_sfx_volume(self):
        self.get_sound_mixer().decrease_sfx_volume()

    def increase_sfx_volume(self):
        self.get_sound_mixer().increase_sfx_volume()

    def screen_content(self):

        x_pos = self.display_width // 2
        y_pos = self.display_height // 2

        self.text("-=-=SETTINGS=-=-", x_pos - 250, 100, 45, "white")

        self.text("SFX Volume:", x_pos - 85, y_pos - 105, 18, "white")
        volume = "X" if (self.get_sound_mixer().mute_sfx) else int(self.get_sound_mixer().sfx_volume * 100)
        self.text(str(volume), x_pos + 100, y_pos - 105, 18, "yellow")

        self.text("MUSIC Volume:", x_pos - 90, y_pos + 10, 18, "white")
        volume = "X" if (self.get_sound_mixer().mute_music) else int(self.get_sound_mixer().music_volume * 100)
        self.text(str(volume), x_pos + 105, y_pos + 10, 18, "yellow")


    def back(self) -> None:
        self.get_owner().change_state("MainMenu")

    @property
    def all_sprites(self):
        return self.__all_sprites

    def handle_update(self):
        pygame.display.update()
        self.background()
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()
