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

    def increase_volume(self):
        self.__volume += 0.05

        if (self.__volume >= 1):
            self.__volume = 1
        
    def decrease_volume(self):
        self.__volume -= 0.05

        if (self.__volume <= 0):
            self.__volume = 0

    @property
    def volume(self):
        return self.__volume


