import pygame
from Sprites.Button.Button import Button
from States.State import State
from tkinter import messagebox
from Sprites.InputBox.InputBox import InputBox

class CreateProfile(State):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.__name = ''
        self.__name_max_length = 5
        self.__input_box = None
        self.create_button()
        self.create_input_box()


    def screen_content(self) -> None:
        self.get_display().fill("black")

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        
        self.text("ENTER A NEW NAME", x_pos-200, y_pos-250, 50, "white")
    

         
    def create_input_box(self):
        x_pos = self.display_width // 2
        y_pos = self.display_height // 2

        self.__input_box = InputBox(x_pos - 165, y_pos - 50, 300, 100)
        self.all_sprites.add(self.__input_box)

    
    def create_button(self) -> None:
        x_pos = self.display_width//2
        y_pos = self.display_height//2

        back = Button(20, 20, 180, 100, "<-- Back", self.back)
        self.all_sprites.add(back)


        select = Button(x_pos-310, y_pos+150, 300, 100, "Create", self.call_create_profile)
        self.all_sprites.add(select)

        back = Button(x_pos+10, y_pos+150, 300, 100, "Back", self.back)
        self.all_sprites.add(back)


    def call_create_profile(self) -> None:
        self.name = self.input_box.text
        if len(self.name) != 0:
            if len(self.name) <= self.name_max_length:
                if " " not in self.name:
                    if not self.verify_profile_existence(self.name):
                        self.create_profile(self.name, 1, 1, 1, 1, 1, 1, 1)
                        self.enter_selected_profile()
                    else:
                        messagebox.showerror(title = 'ERROR', message = f"{self.name} already exists")
                else:
                    messagebox.showerror(title = 'ERROR', message = "The name should not have spaces")
            else:
                messagebox.showerror(title = 'ERROR', message = f"{self.name} should have less than {self.name_max_length} characters")
        else:
            messagebox.showerror(title = 'ERROR', message = "The name should have a bigger length")
    


    def enter_selected_profile(self) -> None:
        if (len(self.all_profiles) != 0):
            self.get_owner().game_data.set_profile(self.profile_selected)
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
    def input_box(self):
        return self.__input_box
    
    @property
    def name_max_length(self):
        return self.__name_max_length
    
    @property
    def name(self):
        return self.__name    
    
    @property
    def profile_selected(self):
        return self.all_profiles[-1]   
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @input_box.setter
    def input_box(self, input_box):
        self.__input_box = input_box