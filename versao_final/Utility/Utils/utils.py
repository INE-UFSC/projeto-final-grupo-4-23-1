import os
import pygame
#retorna o caminho para a pasta assets
def get_assets_path(file_path):
    current_path = os.path.dirname(file_path).split('\\')
    return '\\'.join(current_path[0:current_path.index('States')]) + '\\assets'


class Fade:
    def __init__(self, display_width, display_height) -> None:
        self.__surface = pygame.Surface((display_width, display_height))
        self.__alpha = None
        self.__fade_start = True
        self.__fade_end = False

    
    def fill_black(self) -> None:
        self.surface.fill((0,0,0))
        
    @property
    def alpha(self):
        return self.__alpha
    
    @property
    def fade_start(self):
        return self.__fade_start

    @property
    def fade_end(self):
        return self.__fade_end
    
    def alpha_count(self):
        if self.fade_start:
            self.alpha -= 1
        else:
            self.alpha += 1
        if self.alpha == 0 or self.alpha == 255:
            return self.change_fade()
        else:
            return False
        
    
    def change_fade(self):
        if self.fade_start:
            self.fade_end = True
            self.fade_start = False
            return False
        else:
            self.fade_end = False
            self.fade_start = True
            return True
    
    @property
    def surface(self):
        return self.__surface

    @alpha.setter
    def alpha(self, alpha: int) -> None:
        self.__alpha = alpha
        
    @fade_start.setter
    def fade_start(self, status: bool):
        self.__fade_start = status
    
    @fade_start.setter
    def fade_end(self, status: bool):
        self.__fade_end = status