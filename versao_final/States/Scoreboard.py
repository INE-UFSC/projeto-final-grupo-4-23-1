import pygame
from Sprites.Button.Button import Button
from States.State import State


class Scoreboard(State):
    def __init__(self,owner):
        super().__init__(owner)

        self.create_button()
               

    def create_button(self):

        x_pos = self.display_width//2 - 150
        y_pos = self.display_height//2


        back = Button(20, 20, 180, 100, "<-- Back", self.back)
        self.all_sprites.add(back)


    def back(self):
        self.get_owner().change_state("MainMenu")

    def screen_content(self):
        self.get_display().fill("black")

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        self.text("HIGHSCORE BOARD", x_pos-225, y_pos-250, 50, 'white')
        self.text("1 %s" % (self.get_all_profiles()[0].name), x_pos-100, y_pos-125, 50, 'yellow')
        self.text("2 %s" % (self.get_all_profiles()[1].name), x_pos-100, y_pos-75, 50, 'yellow')
        self.text("3 %s" % (self.get_all_profiles()[2].name), x_pos-100, y_pos-25, 50, 'yellow')
        self.text("4 %s" % (self.get_all_profiles()[3].name), x_pos-100, y_pos+25, 50, 'yellow')
        self.text("5 %s" % (self.get_all_profiles()[4].name), x_pos-100, y_pos+75, 50, 'yellow')

    

    def handle_update(self):
        pygame.display.update()
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()