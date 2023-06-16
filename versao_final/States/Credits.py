import pygame
import webbrowser
from Sprites.Button.Button import Button
from States.State import State


class Credits(State):
    def __init__(self, owner):
        super().__init__(owner)

        self.create_button()

    def create_button(self):
        x_pos = self.display_width // 2
        y_pos = self.display_height // 2

        back = Button(self, 20, 20, 180, 100, "<-- Back", True, self.back)
        self.all_sprites.add(back)

        buttonArthur = Button(self, self.x_pos + 50, self.y_pos - 125, 180, 60, "GITHUB", False, self.gitArthur)
        self.all_sprites.add(buttonArthur)

        buttonBreno = Button(self, self.x_pos + 50, self.y_pos, 180, 60, "GITHUB", False, self.gitBreno)
        self.all_sprites.add(buttonBreno)

        buttonLeonardo = Button(self, self.x_pos + 50, self.y_pos + 125, 180, 60, "GITHUB", False, self.gitLeonardo)
        self.all_sprites.add(buttonLeonardo)

        buttonPedro = Button(self, self.x_pos + 50, self.y_pos + 250, 180, 60, "GITHUB", False, self.gitPedro)
        self.all_sprites.add(buttonPedro)

    def back(self):
        self.get_owner().change_state("MainMenu")

    def screen_content(self):
        x_pos = self.display_width // 2
        y_pos = self.display_height // 2

        self.text("-=-=CREDITS=-=-", self.x_pos - 300, self.y_pos - 270, 40, 'white')

        self.text("Artur", self.x_pos - 350, self.y_pos - 125, 40, 'yellow')
        self.text("Breno", self.x_pos - 350, self.y_pos, 40, 'yellow')
        self.text("Leonardo", self.x_pos - 350, self.y_pos + 125, 40, 'yellow')
        self.text("Pedro", self.x_pos - 350, self.y_pos + 250, 40, 'yellow')

    def handle_update(self):
        pygame.display.update()
        self.background()
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()

    def gitArthur(self):
        url = "https://github.com/ArturRSoda"
        webbrowser.open_new(url)

    def gitBreno(self):
        url = "https://github.com/BrenoSPXx"
        webbrowser.open_new(url)

    def gitLeonardo(self):
        url = "https://github.com/leonardopfeng"
        webbrowser.open_new(url)

    def gitPedro(self):
        url = "https://github.com/Fontoura21"
        webbrowser.open_new(url)


    @property
    def x_pos(self):
        return self.display_width // 2

    @property
    def y_pos(self):
        return self.display_height // 2
