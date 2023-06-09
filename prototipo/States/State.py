import pygame
from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, owner):
        #Game é o parâmetro owner. Assim é possível fazer a transição de estados com o change_state
        self.__owner = owner

        #altura e largura da tela
        self.__display_width = pygame.display.Info().current_w
        self.__display_height = pygame.display.Info().current_h

    def get_display(self):
        return pygame.display.get_surface()
    
    def get_owner(self):
        return self.__owner
    
    def get_result(self):
        return self.__owner.result_data
    

    #metodo geral para colocar texto
    def text(self, text, x, y, size):
        self.font = pygame.font.SysFont(None, size)
        textSurface = self.font.render(text, True, ("white"))
        self.get_display().blit(textSurface, (x, y))
    
    #conteúdo da tela
    @abstractmethod
    def screen_content(self):
        pass
    #atualiza a tela
    @abstractmethod
    def handle_update(self):
        pass
    #lida com a transição de estados
    def handle_transition(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.get_owner().close()

    @property
    def display_width(self):
        return self.__display_width
    
    @property
    def display_height(self):
        return self.__display_height