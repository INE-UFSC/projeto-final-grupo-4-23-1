import pygame
from Sprites.Button.Button import Button
from States.State import State
from tkinter import messagebox
from time import time

class SelectProfile(State):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.create_button()

        self.__profile_selected_index = 0
        self.__button_time = time()

    def screen_content(self) -> None:
        self.get_display().fill("black")

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        
        self.text("SELECT YOUR PROFILE", x_pos-200, y_pos-250, 50)
        self.show_profile_selected_name()

    def show_profile_selected_name(self):
        x_pos = self.display_width//2
        y_pos = self.display_height//2

        if (len(self.all_profiles) == 0):
            self.text("None", x_pos-40, y_pos-50, 40)
        else:
            self.text(self.profile_selected.name , x_pos-40, y_pos-50, 40)

    def create_button(self):
        x_pos = self.display_width//2
        y_pos = self.display_height//2

        back = Button(10, 10, "<-- Back", self.back)
        self.all_sprites.add(back)

        advance = Button(x_pos+100, y_pos-80, ">>>", self.advance_selected_profile)
        self.all_sprites.add(advance)

        back = Button(x_pos-400, y_pos-80, "<<<", self.back_selected_profile)
        self.all_sprites.add(back)

        select = Button(x_pos-310, y_pos+150, "Enter Profile", self.enter_selected_profile)
        self.all_sprites.add(select)

        remove =Button(x_pos+10, y_pos+150, "Remove Profile", self.remove_selected_profile)
        self.all_sprites.add(remove)

    def remove_selected_profile(self):
        if (len(self.all_profiles) != 0):
            if (messagebox.askyesno("Remove Profile", "Do you really want to delete %s profile?" % self.profile_selected.name)):
                self.remove_profile(self.profile_selected.name)
                self.advance_selected_profile()


    def enter_selected_profile(self):
        if (len(self.all_profiles) != 0):
            self.get_owner().game_data.set_profile(self.profile_selected)
            print(self.get_owner().game_data.profile.name)

    def advance_selected_profile(self):
        if ((time() - self.button_time) > 0.1):
            if (len(self.all_profiles) == 0):
                self.__profile_selected_index = 0
            elif (self.profile_selected_index >= len(self.all_profiles)-1):
                self.__profile_selected_index = 0
            else:
                self.__profile_selected_index += 1

            self.__button_time = time()

    def back_selected_profile(self):
        if ((time() - self.button_time) > 0.1):
            if (len(self.all_profiles) == 0):
                self.__profile_selected_index = 0
            elif (self.profile_selected_index == 0):
                self.__profile_selected_index = len(self.all_profiles)-1
            else:
                self.__profile_selected_index -= 1

            self.__button_time = time()

    def back(self) -> None:
        self.get_owner().change_state("MainMenu")


    def handle_update(self) -> None:
        pygame.display.update()
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()

    @property
    def all_profiles(self):
        return self.get_all_profiles()

    @property
    def profile_selected_index(self):
        return self.__profile_selected_index

    @property
    def profile_selected(self):
        return self.all_profiles[self.profile_selected_index]

    @property
    def button_time(self):
        return self.__button_time