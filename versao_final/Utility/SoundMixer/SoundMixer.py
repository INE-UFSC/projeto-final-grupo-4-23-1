import pygame
from os import path
import time

pasta = path.dirname(__file__)
SFX_dir = pasta+"//Sounds//SFX//"
Music_dir = pasta+"//Sounds//Music//"

class SoundMixer:
    def __init__(self):
        pygame.mixer.init()

        #sfx
        self.__sfx_volume = 0.05
        self.__mute_sfx = False
        self.__bullet_sfx = self.load_sfx("bullet_sfx.ogg")
        self.__button_click_sfx = self.load_sfx("button_click_sfx.ogg")
        self.__charge_tank_boss_rush_sfx = self.load_sfx("charge_tank_boss_rush_sfx.ogg")
        self.__explosion_sfx = self.load_sfx("explosion_sfx.ogg")
        self.__explosion_2_sfx = self.load_sfx("explosion_2_sfx.ogg")
        self.__hit_sfx = self.load_sfx("hit_sfx.ogg")
        self.__boost_sfx = self.load_sfx("boost_sfx.ogg")
        self.__lvl_up_sfx = self.load_sfx("lvl_up_sfx.ogg")
        self.__boss_defeated_sfx = self.load_sfx("boss_defeated_sfx.ogg")
        self.__boss_fight_sfx = self.load_sfx("boss_fight_sfx.ogg")
        self.__charge_up_sfx = self.load_sfx("charge_up_sfx.ogg")
        self.__cannon_blast_sfx = self.load_sfx("cannon_blast_sfx.ogg")
        self.__laser_shot_sfx = self.load_sfx("laser_shot_sfx.ogg")

        #music
        self.__music_volume = 0.05
        self.__mute_music = False
        self.__boss_level_music = self.load_music("boss_level_music.ogg")
        self.__normal_level_music = self.load_music("normal_level_music.ogg")
        self.__result_music = self.load_music("result_music.ogg")
        self.__theme_music = self.load_music("theme_music.ogg")

    def load_sfx(self, file_name: str):
        sfx = pygame.mixer.Sound(SFX_dir+file_name)
        return sfx

    def load_music(self, file_name: str):
        msc = pygame.mixer.Sound(Music_dir+file_name)
        return msc

    def play_boss_level_music(self):
        if (not self.__mute_music):
            pygame.mixer.fadeout(1000)
            self.__boss_level_music.set_volume(self.music_volume)
            self.__boss_level_music.play(-1)

    def play_normal_level_music(self):
        if (not self.__mute_music):
            pygame.mixer.fadeout(1000)
            self.__normal_level_music.set_volume(self.music_volume)
            self.__normal_level_music.play(-1)

    def play_result_music(self):
        if (not self.__mute_music):
            pygame.mixer.fadeout(1000)
            self.__result_music.set_volume(self.music_volume)
            self.__result_music.play(-1)

    def play_theme_music(self):
        if (not self.__mute_music):
            pygame.mixer.fadeout(1000)
            self.__theme_music.set_volume(self.music_volume)
            self.__theme_music.play(-1)

    def play_laser_shot_sfx(self):
        if (not self.mute_sfx):
            self.__laser_shot_sfx.set_volume(self.sfx_volume)
            self.__laser_shot_sfx.play()

    def play_cannon_blast_sfx(self):
        if (not self.__mute_sfx):
            self.__cannon_blast_sfx.set_volume(self.sfx_volume)
            self.__cannon_blast_sfx.play()

    def play_charge_up_sfx(self):
        if (not self.__mute_sfx):
            self.__charge_up_sfx.set_volume(self.sfx_volume)
            self.__charge_up_sfx.play()

    def play_boss_fight_sfx(self):
        if (not self.__mute_sfx):
            pygame.mixer.fadeout(1000)
            self.__boss_fight_sfx.set_volume(self.sfx_volume)
            self.__boss_fight_sfx.play()

    def play_boss_defeated_sfx(self):
        if (not self.__mute_sfx):
            self.__boss_defeated_sfx.set_volume(self.sfx_volume)
            self.__boss_defeated_sfx.play()

    def play_lvl_up_sfx(self):
        if (not self.__mute_sfx):
            self.__lvl_up_sfx.set_volume(self.sfx_volume)
            self.__lvl_up_sfx.play()

    def play_bullet_sfx(self):
        if (not self.__mute_sfx):
            self.__bullet_sfx.set_volume(self.sfx_volume)
            self.__bullet_sfx.play()

    def play_button_click_sfx(self):
        if (not self.__mute_sfx):
            self.__button_click_sfx.set_volume(self.sfx_volume)
            self.__button_click_sfx.play()

    def play_charge_tank_boss_rush_sfx(self):
        if (not self.__mute_sfx):
            self.__charge_tank_boss_rush_sfx.set_volume(self.sfx_volume)
            self.__charge_tank_boss_rush_sfx.play()

    def play_explosion_sfx(self):
        if (not self.__mute_sfx):
            self.__explosion_sfx.set_volume(self.sfx_volume)
            self.__explosion_sfx.play()

    def play_explosion_2_sfx(self):
        if (not self.__mute_sfx):
            self.__explosion_2_sfx.set_volume(self.sfx_volume)
            self.__explosion_2_sfx.play()

    def play_hit_sfx(self):
        if (not self.__mute_sfx):
            self.__hit_sfx.set_volume(self.sfx_volume)
            self.__hit_sfx.play()

    def play_boost_sfx(self):
        if (not self.__mute_sfx):
            self.__boost_sfx.set_volume(self.sfx_volume)
            self.__boost_sfx.play(-1)

    def increase_sfx_volume(self):
        if (not self.__mute_sfx):
            r_vol, inc = self.inc(self.sfx_volume)
            self.__sfx_volume = 1 if ((r_vol+inc) > 1) else r_vol+inc

    def decrease_sfx_volume(self):
        if (not self.__mute_sfx):
            r_vol, inc = self.dec(self.sfx_volume)
            self.__sfx_volume = 0 if ((r_vol-inc) < 0) else r_vol-inc

    def increase_music_volume(self):
        if (not self.__mute_sfx):
            r_vol, inc = self.inc(self.music_volume)
            self.__music_volume = 1 if ((r_vol+inc) > 1) else r_vol+inc

    def decrease_music_volume(self):
        if (not self.__mute_sfx):
            r_vol, inc = self.dec(self.music_volume)
            self.__music_volume = 0 if ((r_vol-inc) < 0) else r_vol-inc

    def mute_unmute_music(self):
        self.__mute_music = False if (self.__mute_music) else True

    def mute_unmute_sfx(self):
        self.__mute_sfx = False if (self.__mute_sfx) else True

    def inc(self, vol: float):
        r_vol = round(vol, 2)
        if (r_vol >= 0.95):
            inc = 0.01
        elif (r_vol >= 0.05):
            inc = 0.05
        elif (r_vol >= 0):
            inc = 0.01
        return (r_vol, inc)

    def dec(self, vol: float):
        r_vol = round(vol, 2)
        if (r_vol <= 0.05):
            inc = 0.01
        elif (r_vol <= 0.95):
            inc = 0.05
        elif (r_vol<= 1):
            inc = 0.01
        return (r_vol, inc)

    @property
    def cannon_blast_sfx(self):
        return self.__cannon_blast_sfx

    @property
    def sfx_volume(self):
        return self.__sfx_volume

    @property
    def boost_sfx(self):
        return self.__boost_sfx

    @property
    def mute_music(self):
        return self.__mute_music

    @property
    def mute_sfx(self):
        return self.__mute_sfx

    @property
    def music_volume(self):
        return self.__music_volume

    @property
    def boss_level_music(self):
        return self.__boss_level_music

    @property
    def normal_level_music(self):
        return self.__normal_level_music

    @property
    def result_music(self):
        return self.__result_music

    @property
    def theme_music(self):
        return self.__theme_music

