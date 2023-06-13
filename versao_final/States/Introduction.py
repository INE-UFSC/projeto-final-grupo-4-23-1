import pygame
from States.State import State
import os


class Introduction(State):
    def __init__(self, owner):
        super().__init__(owner)
        self.__intro_credits = pygame.font.Font(f'{self.get_assets_path(__file__)}/fonts/game_font.ttf', 70)
        self.__fade = pygame.Surface((self.display_width, self.display_height))
        self.__fade.fill((0, 0, 0))
        
        self.__company_intro_text = 'ABLP Company'
        self.__association_intro_text = 'IN ASSOCIATION WITH UFSC'
        self.__present_intro_text = 'PRESENT'
        self.__game_name_intro_text = 'ASTEROID-PLUS'
        
        self.screen_content()
    
    def company_intro(self):
        self.intro_credits_surf = self.intro_credits.render(
            self.company_intro_text, True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surf.get_rect(
            center=(self.display_width / 2, 360)
        )
        self.render_intro_start()
        self.render_intro_end()
    
    def association_intro(self):
        self.intro_credits_surf = self.intro_credits.render(
            self.association_intro_text, True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surf.get_rect(
            center=(self.display_width / 2, 280)
        )
        self.render_intro_start()
        self.render_intro_end()
        
    
    def present_intro(self):
        self.intro_credits_surf = self.intro_credits.render(
            self.present_intro_text, True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surf.get_rect(
            center=(self.display_width / 2, 360)
        )
        self.render_intro_start()
        self.render_intro_end()
    
    def game_name_intro(self):
        self.intro_credits_surf = self.intro_credits.render(
            self.game_name_intro_text, True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surf.get_rect(
            center=(self.display_width / 2, 280)
        )
        self.render_intro_start()
        self.render_intro_end()
        
    
    def render_intro_start(self):
        
        for alpha in range(255, 0, -1):
            pygame.event.get()
            self.fade.set_alpha(alpha)
            self.get_display().blit(self.intro_credits_surf, self.intro_credits_rect)
            self.get_display().blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
    
    def render_intro_end(self):    
        
        for alpha in range(0, 255):
            pygame.event.get()
            self.fade.set_alpha(alpha)
            self.get_display().blit(self.intro_credits_surf, self.intro_credits_rect)
            self.get_display().blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
    
    def screen_content(self):
        self.company_intro()
        self.association_intro()
        self.present_intro()
        self.game_name_intro()
       
        
    def get_assets_path(self, file_path):
        current_path = os.path.dirname(file_path).split('\\')
        return '\\'.join(current_path[0:current_path.index('States')]) + '\\assets'
    
    def handle_update(self):
        self.get_owner().change_state('MainMenu')
    
    def create_button(self):
        pass
      
    @property
    def intro_credits(self):
        return self.__intro_credits  
    
    @property
    def fade(self):
        return self.__fade
    
    @property
    def company_intro_text(self):
        return self.__company_intro_text
    
    @property
    def association_intro_text(self):
        return self.__association_intro_text
    
    @property
    def present_intro_text(self):
        return self.__present_intro_text
    
    @property
    def game_name_intro_text(self):
        return self.__game_name_intro_text
 