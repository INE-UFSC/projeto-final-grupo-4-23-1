import pygame
from Entities.Button.Button import Button
from States.State import State


class MainMenu(State):
    def __init__(self, owner):
        super().__init__(owner)
        self.__all_sprites = pygame.sprite.Group()

        self.create_button()

    def create_button(self):

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        #menu buttons
        newProfile = Button(self, x_pos-310, y_pos - 170, 300, 100, 'New Profile', True, self.new_profile)
        self.all_sprites.add(newProfile)

        selectProfile = Button(self, x_pos+10, y_pos-170, 300, 100, 'Select Profile', True, self.select_profile)
        self.all_sprites.add(selectProfile)

        scoreboard = Button(self, x_pos-310, y_pos-20, 300, 100, 'Scoreboard', True, self.scoreboard)
        self.all_sprites.add(scoreboard)

        credits = Button(self, x_pos+10, y_pos-20, 300, 100, 'Credits', True, self.credits)
        self.all_sprites.add(credits)

        quit = Button(self, x_pos-150, y_pos+130, 300, 100, 'Quit', True, self.quit)
        self.all_sprites.add(quit)

        #volume buttons
        mute_sfx = Button(self, self.display_width-270, y_pos-80, 70, 70, "M", True, self.mute_unmute_sfx)
        self.all_sprites.add(mute_sfx)

        inc_sfx_volume = Button(self, self.display_width-180, y_pos-80, 70, 70, "+V", True, self.increase_sfx_volume)
        self.all_sprites.add(inc_sfx_volume)

        dec_sfx_volume = Button(self, self.display_width-90, y_pos-80, 70, 70, "-V", True, self.decrease_sfx_volume)
        self.all_sprites.add(dec_sfx_volume)

        mute_music = Button(self, self.display_width-270, y_pos+35, 70, 70, "M", True, self.mute_unmute_music)
        self.all_sprites.add(mute_music)

        inc_music_volume = Button(self, self.display_width-180, y_pos+35, 70, 70, "+V", True, self.increase_music_volume)
        self.all_sprites.add(inc_music_volume)

        dec_music_volume = Button(self, self.display_width-90, y_pos+35, 70, 70, "-V", True, self.decrease_music_volume)
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

    def select_profile(self):
        self.get_owner().change_state("SelectProfile")

    def new_profile(self):
        self.get_owner().change_state("CreateProfile")

    def quit(self):
        self.get_owner().close()

    def scoreboard(self):
        self.get_owner().change_state("ScoreBoard")

    def credits(self):
        self.get_owner().change_state("Credits")

    def screen_content(self):

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        self.text("-=-=ASTEROIDS-PLUS=-=-", x_pos-400, 100, 45, "white")

        self.text("SFX Volume:", self.display_width-260, y_pos-105, 18, "white")
        volume = "X" if (self.get_sound_mixer().mute_sfx) else int(self.get_sound_mixer().sfx_volume * 100)
        self.text(str(volume), self.display_width-75, y_pos-105, 18, "yellow")

        self.text("MUSIC Volume:", self.display_width-265, y_pos+10, 18, "white")
        volume = "X" if (self.get_sound_mixer().mute_music) else int(self.get_sound_mixer().music_volume * 100)
        self.text(str(volume), self.display_width-65, y_pos+10, 18, "yellow")

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
