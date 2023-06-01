import pygame
from Sprites.Button.Button import Button
from States.State import State
from Profiles.Profile import Profile
from time import time

class Store(State):
    def __init__(self, owner):
        super().__init__(owner)

        self.__click_time = time()

        self.__vel_max_price = 15

        self.__current_profile: Profile = self.get_owner().game_data.profile

        self.create_button()

    def create_button(self):
        x_pos = self.display_width//2 
        y_pos = self.display_height//2

        back = Button(20, 20, 180, 100, "<-- Back", self.back)
        self.all_sprites.add(back)

        rmv_vel_max = Button(20, 180, 70, 70, "-", self.rmv_vel_max)
        add_vel_max = Button(325, 180, 70, 70, "+", self.add_vel_max)
        self.all_sprites.add(rmv_vel_max)
        self.all_sprites.add(add_vel_max)

    def rmv_vel_max(self):
        if ((time() - self.click_time) > 0.35):
            if (self.current_profile.ship_vel_max > 1):

                credit = self.current_profile.credit + self.vel_max_price
                self.current_profile.set_credit(credit)

                vel_max = self.current_profile.ship_vel_max - 1
                self.current_profile.set_ship_vel_max(vel_max)

            self.__click_time = time()

    def add_vel_max(self):
        if ((time() - self.click_time) > 0.35):

            if (self.current_profile.credit >= self.vel_max_price):
                if (self.current_profile.ship_vel_max < 5):

                    credit = self.current_profile.credit - self.vel_max_price
                    self.current_profile.set_credit(credit)

                    vel_max = self.current_profile.ship_vel_max + 1
                    self.current_profile.set_ship_vel_max(vel_max)

            self.__click_time = time()

    def update_rects(self) -> None:
        self.vel_max_rect()

    def vel_max_rect(self):
        #1 rect
        self.rect(100, 200, 50, 25, self.current_profile.ship_vel_max, 2)
        #2 rect
        self.rect(155, 200, 50, 25, self.current_profile.ship_vel_max, 3)
        #3 rect
        self.rect(210, 200, 50, 25, self.current_profile.ship_vel_max, 4)
        #4 rect
        self.rect(265, 200, 50, 25, self.current_profile.ship_vel_max, 5)

    def back(self):
        self.save_profile(self.current_profile)
        self.get_owner().change_state("ProfileMenu")

    def screen_content(self) -> None:
        self.get_display().fill("black")

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
        self.text("-%d"%self.vel_max_price, 40, 160, 30, "green")
        self.text("+%d"%self.vel_max_price, 345, 160, 30, "red")

    def rect(self, x: int, y: int, width: int, heigth: int, profile_value: int, green_value: int):
        color = "gray" if (profile_value < green_value) else "green"
        pygame.draw.rect(self.get_display(), color, (x, y, width, heigth))


    def handle_update(self) -> None:
        pygame.display.update()
        self.screen_content()
        pygame.display.update()

    @property
    def current_profile(self) -> Profile:
        return self.__current_profile

    @property
    def click_time(self):
        return self.__click_time
    
    @property
    def vel_max_price(self):
        return self.__vel_max_price