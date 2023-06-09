import pygame
from Sprites.Button.Button import Button
from States.State import State
from Profiles.Profile import Profile
from time import time

class Store(State):
    def __init__(self, owner):
        super().__init__(owner)

        self.__vel_max_price = 15
        self.__damage_price = 20
        self.__life_price = 50

        self.__current_profile: Profile = self.get_owner().game_data.profile

        self.create_button()

    def create_button(self):
        x_pos = self.display_width//2 
        y_pos = self.display_height//2

        back = Button(self, 20, 20, 180, 100, "<-- Back", self.back)
        self.all_sprites.add(back)

        #linha 1 coluna 1
        rmv_vel_max = Button(self, 20, 180, 70, 70, "-", True, self.rmv_vel_max)
        add_vel_max = Button(self, 325, 180, 70, 70, "+", True, self.add_vel_max)
        self.all_sprites.add(rmv_vel_max)
        self.all_sprites.add(add_vel_max)

        #linha 1 coluna 2
        rmv_damage = Button(self, 500, 180, 70, 70, "-", True, self.rmv_damage)
        add_damage = Button(self, 805, 180, 70, 70, "+", True, self.add_damage)
        self.all_sprites.add(rmv_damage)
        self.all_sprites.add(add_damage)

        #linha 2 coluna 1
        rmv_life = Button(self, 20, 360, 70, 70, "-", True, self.rmv_life)
        add_life = Button(self, 325, 360, 70, 70, "+", True, self.add_life)
        self.all_sprites.add(rmv_life)
        self.all_sprites.add(add_life)



    def rmv_vel_max(self):
        if (self.current_profile.ship_vel_max > 1):

            credit = self.current_profile.credit + self.vel_max_price
            self.current_profile.set_credit(credit)

            vel_max = self.current_profile.ship_vel_max - 1
            self.current_profile.set_ship_vel_max(vel_max)

    def add_vel_max(self):
        if (self.current_profile.credit >= self.vel_max_price):
            if (self.current_profile.ship_vel_max < 5):

                credit = self.current_profile.credit - self.vel_max_price
                self.current_profile.set_credit(credit)

                vel_max = self.current_profile.ship_vel_max + 1
                self.current_profile.set_ship_vel_max(vel_max)

    def rmv_damage(self):
        if (self.current_profile.ship_damage > 1):

            credit = self.current_profile.credit + self.damage_price
            self.current_profile.set_credit(credit)

            damage = self.current_profile.ship_damage - 1
            self.current_profile.set_ship_damage(damage)

    def add_damage(self):
        if (self.current_profile.credit >= self.damage_price):
            if (self.current_profile.ship_damage < 5):

                credit = self.current_profile.credit - self.damage_price
                self.current_profile.set_credit(credit)

                damage = self.current_profile.ship_damage + 1
                self.current_profile.set_ship_damage(damage)

    def rmv_life(self):
        if (self.current_profile.ship_life > 1):

            credit = self.current_profile.credit + self.life_price
            self.current_profile.set_credit(credit)

            life = self.current_profile.ship_life - 1
            self.current_profile.set_ship_life(life)

    def add_life(self):
        if (self.current_profile.credit >= self.life_price):
            if (self.current_profile.ship_life < 5):

                credit = self.current_profile.credit - self.life_price
                self.current_profile.set_credit(credit)

                life = self.current_profile.ship_life + 1
                self.current_profile.set_ship_life(life)



    def update_rects(self) -> None:
        self.vel_max_rect()
        self.damage_rect()
        self.life_rect()

    def vel_max_rect(self):
        #1 rect
        self.rect(100, 200, 50, 25, self.current_profile.ship_vel_max, 2)
        #2 rect
        self.rect(155, 200, 50, 25, self.current_profile.ship_vel_max, 3)
        #3 rect
        self.rect(210, 200, 50, 25, self.current_profile.ship_vel_max, 4)
        #4 rect
        self.rect(265, 200, 50, 25, self.current_profile.ship_vel_max, 5)

    def damage_rect(self):
        #1 rect
        self.rect(580, 200, 50, 25, self.current_profile.ship_damage, 2)
        #2 rect
        self.rect(635, 200, 50, 25, self.current_profile.ship_damage, 3)
        #3 rect
        self.rect(690, 200, 50, 25, self.current_profile.ship_damage, 4)
        #4 rect
        self.rect(745, 200, 50, 25, self.current_profile.ship_damage, 5)

    def life_rect(self):
        #1 rect
        self.rect(100, 380, 50, 25, self.current_profile.ship_life, 2)
        #2 rect
        self.rect(155, 380, 50, 25, self.current_profile.ship_life, 3)
        #3 rect
        self.rect(210, 380, 50, 25, self.current_profile.ship_life, 4)
        #4 rect
        self.rect(265, 380, 50, 25, self.current_profile.ship_life, 5)

    def back(self):
        self.save_profile(self.current_profile)
        self.get_owner().change_state("ProfileMenu")

    def screen_content(self) -> None:

        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        self.update_rects()

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        self.text("STORE", x_pos-50, 20, 50, "white")

        self.text("Credit:", self.display_width-220, 20, 40, "white")
        self.text(str(self.current_profile.credit), self.display_width-120, 20, 40, "yellow")

        #velmax
        self.text("Vel. Max:", 160, 160, 30, "white")
        self.text("+%d"%self.vel_max_price, 40, 160, 30, "green")
        self.text("-%d"%self.vel_max_price, 345, 160, 30, "red")

        #damage
        self.text("Damage:", 640, 160, 30, "white")
        self.text("+%d"%self.damage_price, 520, 160, 30, "green")
        self.text("-%d"%self.damage_price, 825, 160, 30, "red")

        #life
        self.text("Life:", 160, 320, 30, "white")
        self.text("+%d" % self.life_price, 40, 320, 30, "green")
        self.text("-%d" % self.life_price, 345, 320, 30, "red")

    def rect(self, x: int, y: int, width: int, heigth: int, profile_value: int, green_value: int):
        color = "gray" if (profile_value < green_value) else "green"
        pygame.draw.rect(self.get_display(), color, (x, y, width, heigth))


    def handle_update(self) -> None:
        pygame.display.update()
        self.background()
        self.screen_content()
        pygame.display.update()

    @property
    def current_profile(self) -> Profile:
        return self.__current_profile

    @property
    def vel_max_price(self):
        return self.__vel_max_price

    @property
    def damage_price(self):
        return self.__damage_price

    @property
    def life_price(self):
        return self.__life_price

