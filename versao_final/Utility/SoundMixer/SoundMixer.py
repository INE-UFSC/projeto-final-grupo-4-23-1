import pygame
from os import path
import time

pasta = path.dirname(__file__)

class SoundMixer:
    def __init__(self):
        pygame.mixer.init()
        self.__volume = 0.20

        self.__bullet_sound = pygame.mixer.Sound(pasta+"//Sounds//bullet_sound.ogg")
        self.__button_click_sound = pygame.mixer.Sound(pasta+"//Sounds//button_click_sound.ogg")
        self.__charge_tank_boss_rush_sound = pygame.mixer.Sound(pasta+"//Sounds//charge_tank_boss_rush_sound.ogg")
        self.__ship_explosion_sound = pygame.mixer.Sound(pasta+"//Sounds//ship_explosion_sound.ogg")
        self.__hit_sound = pygame.mixer.Sound(pasta+"//Sounds//hit_sound.ogg")


    def play_bullet_sound(self):
        self.__bullet_sound.set_volume(self.volume)
        self.__bullet_sound.play()

    def play_button_click_sound(self):
        self.__button_click_sound.set_volume(self.volume)
        self.__button_click_sound.play()

    def play_charge_tank_boss_rush_sound(self):
        self.__charge_tank_boss_rush_sound.set_volume(self.volume)
        self.__charge_tank_boss_rush_sound.play()

    def play_ship_explosion_sound(self):
        self.__ship_explosion_sound.set_volume(self.volume)
        self.__ship_explosion_sound.play()

    def play_hit_sound(self):
        self.__hit_sound.set_volume(self.volume)
        self.__hit_sound.play()

    def increase_volume(self):
        r_vol = round(self.volume, 2)
        if (r_vol >= 0.95):
            inc = 0.01
        elif (r_vol >= 0.05):
            inc = 0.05
        elif (r_vol >= 0):
            inc = 0.01
        self.__volume = 1 if ((r_vol+inc) > 1) else self.volume+inc

        
    def decrease_volume(self):
        r_vol = round(self.volume, 2)
        if (r_vol <= 0.05):
            inc = 0.01
        elif (r_vol <= 0.95):
            inc = 0.05
        elif (r_vol<= 1):
            inc = 0.01
        self.__volume = 0 if ((r_vol-inc) < 0) else r_vol-inc

    @property
    def volume(self):
        return self.__volume


