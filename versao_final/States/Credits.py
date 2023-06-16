import pygame
from Sprites.Button.Button import Button
from States.State import State


class Credits(State):
    def __init__(self, owner):
        super().__init__(owner)

        self.create_button()

    def create_button(self):
        x_pos = self.display_width // 2 - 150
        y_pos = self.display_height // 2

        back = Button(self, 20, 20, 180, 100, "<-- Back", True, self.back)
        self.all_sprites.add(back)

    def back(self):
        self.get_owner().change_state("MainMenu")

    def screen_content(self):
        x_pos = self.display_width // 2
        y_pos = self.display_height // 2

        self.text("-=-=CREDITS=-=-", self.x_pos - 300, self.y_pos - 270, 40, 'white')

        # name1 = self.get_all_profiles()[0].name if (len(self.get_all_profiles()) >= 1) else "<None>"
        # self.text("1. %s" % (name1), self.x_pos - 350, self.y_pos - 125, 40, 'yellow')
        #
        # score1 = self.get_all_profiles()[0].max_score if (len(self.get_all_profiles()) >= 1) else ""
        # self.text("%s" % (score1), self.x_pos + 50, self.y_pos - 125, 40, 'yellow')

        #onde eh o score colocar um botao
        #nome deixa igual a posição

        self.text("Arthur", self.x_pos - 350, self.y_pos - 125, 40, 'yellow')
        buttonArthur = Button(self, self.x_pos + 50, self.y_pos - 125, 180, 60, "GITHUB", False, self.back)
        self.all_sprites.add(buttonArthur)

        self.text("Breno", self.x_pos - 350, self.y_pos, 40, 'yellow')
        buttonBreno = Button(self, self.x_pos + 50, self.y_pos, 180, 60, "GITHUB", False, self.back)
        self.all_sprites.add(buttonBreno)

        self.text("Leonardo", self.x_pos - 350, self.y_pos + 125, 40, 'yellow')
        buttonLeonardo = Button(self, self.x_pos + 50, self.y_pos + 125, 180, 60, "GITHUB", False, self.back)
        self.all_sprites.add(buttonLeonardo)

        self.text("Pedro", self.x_pos - 350, self.y_pos + 250, 40, 'yellow')
        buttonPedro = Button(self, self.x_pos + 50, self.y_pos + 250, 180, 60, "GITHUB", False, self.back)
        self.all_sprites.add(buttonPedro)





    def handle_update(self):
        pygame.display.update()
        self.background()
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()

    @property
    def x_pos(self):
        return self.display_width // 2

    @property
    def y_pos(self):
        return self.display_height // 2