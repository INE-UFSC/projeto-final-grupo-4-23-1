import pygame
from Sprites.Button.Button import Button
from States.State import State
from tkinter import messagebox
from Sprites.InputBox.InputBox import InputBox

class CreateProfile(State):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.create_button()
        self.create_input_box()
        self.__name = ''

    def screen_content(self) -> None:
        self.get_display().fill("black")

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        
        self.text("ENTER A NEW NAME", x_pos-200, y_pos-250, 50, "white")
    
      
         
    def create_input_box(self):
        x_pos = self.display_width//2
        y_pos = self.display_height//2
    
        input_box = InputBox(x_pos-165, y_pos-50, 500, 100)
        self.all_sprites.add(input_box)
    
    def create_button(self) -> None:
        x_pos = self.display_width//2
        y_pos = self.display_height//2

        back = Button(20, 20, 180, 100, "<-- Back", self.back)
        self.all_sprites.add(back)


        select = Button(x_pos-310, y_pos+150, 300, 100, "Create", self.create_profile)
        self.all_sprites.add(select)

        back = Button(x_pos+10, y_pos+150, 300, 100, "Back", self.back)
        self.all_sprites.add(back)


    def create_profile(self) -> None:
        if len(self.name) != 0:
            self.create_profile(self.name, 1, 1, 1, 1, 1, 1, 1)
            self.enter_selected_profile()
        else:
            pass
        



    def enter_selected_profile(self) -> None:
        if (len(self.all_profiles) != 0):
            self.get_owner().game_data.set_profile(self.get_profile(self.name))
            self.get_owner().change_state("ProfileMenu")

    def back(self) -> None:
        self.get_owner().change_state("MainMenu")


    def handle_update(self) -> None:
        pygame.display.update()
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()
        

    @property
    def all_profiles(self) -> list:
        return self.get_all_profiles()

    
    @property
    def name(self):
        return self.__name       