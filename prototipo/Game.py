import pygame
from StateMachine import StateMachine

class Game:
    def __init__(self):
        pygame.init()

        self.display_width = 800
        self.display_height = 600
        self.BLACK, self.WHITE = (0,0,0), (255, 255, 255)
        self.font_name = pygame.font.get_default_font()
        self.display = pygame.Surface((self.display_width, self.display_height))
        self.window = pygame.display.set_mode((self.display_width, self.display_height))

        self.state_machine = StateMachine()

    @property
    def display_width(self):
        return self.display_width

    @property
    def display_height(self):
        return self.display_height

    def run(self):
        pygame.window.set_caption("ASTEROIDS")

        self.state_machine.state_manager()

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface,text_rect)

Game().run()

