import pygame
from os import path
import time

pasta = path.dirname(__file__)
SFX_dir = pasta+"//Sounds//SFX//"
Music_dir = pasta+"//Sounds//Music//"

class SoundMixer:
    def __init__(self):
        pygame.mixer.init()
        self.__sfx_volume = 0.20

        #sfx
        self.__bullet_sfx = pygame.mixer.Sound(SFX_dir+"bullet_sfx.ogg")
        self.__button_click_sfx = pygame.mixer.Sound(SFX_dir+"button_click_sfx.ogg")
        self.__charge_tank_boss_rush_sfx = pygame.mixer.Sound(SFX_dir+"charge_tank_boss_rush_sfx.ogg")
        self.__ship_explosion_sfx = pygame.mixer.Sound(SFX_dir+"explosion_sfx.ogg")
        self.__hit_sfx = pygame.mixer.Sound(SFX_dir+"hit_sfx.ogg")
        self.__boost_sfx = pygame.mixer.Sound(SFX_dir+"boost_sfx.ogg")


    def play_bullet_sfx(self):
        self.__bullet_sfx.set_volume(self.sfx_volume)
        self.__bullet_sfx.play()

    def play_button_click_sfx(self):
        self.__button_click_sfx.set_volume(self.sfx_volume)
        self.__button_click_sfx.play()

    def play_charge_tank_boss_rush_sfx(self):
        self.__charge_tank_boss_rush_sfx.set_volume(self.sfx_volume)
        self.__charge_tank_boss_rush_sfx.play()

    def play_explosion_sfx(self):
        self.__ship_explosion_sfx.set_volume(self.sfx_volume)
        self.__ship_explosion_sfx.play()

    def play_hit_sfx(self):
        self.__hit_sfx.set_volume(self.sfx_volume)
        self.__hit_sfx.play()

    def play_boost_sfx(self):
        self.__boost_sfx.set_volume(self.sfx_volume)
        self.__boost_sfx.play(-1)

    def increase_sfx_volume(self):
        r_vol = round(self.sfx_volume, 2)
        if (r_vol >= 0.95):
            inc = 0.01
        elif (r_vol >= 0.05):
            inc = 0.05
        elif (r_vol >= 0):
            inc = 0.01
        self.__sfx_volume = 1 if ((r_vol+inc) > 1) else self.sfx_volume+inc

        
    def decrease_sfx_volume(self):
        r_vol = round(self.sfx_volume, 2)
        if (r_vol <= 0.05):
            inc = 0.01
        elif (r_vol <= 0.95):
            inc = 0.05
        elif (r_vol<= 1):
            inc = 0.01
        self.__sfx_volume = 0 if ((r_vol-inc) < 0) else r_vol-inc

    @property
    def sfx_volume(self):
        return self.__sfx_volume

    @property
    def boost_sfx(self):
        return self.__boost_sfx

