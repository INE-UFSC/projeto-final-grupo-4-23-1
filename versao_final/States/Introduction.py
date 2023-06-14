import pygame
from States.State import State
import os
from Utility.Utils.utils import get_assets_path
from Sprites.Button.Button import Button
class Introduction(State):
    def __init__(self, owner):
        super().__init__(owner)
        self.__intro_credits = pygame.font.Font(f'{get_assets_path(__file__)}/fonts/game_font.ttf', 70)
        self.__fade = pygame.Surface((self.display_width, self.display_height))
        self.__fade.fill((0, 0, 0))
        
        self.__company_intro_text = 'ABLP Company'
        self.__association_intro_text = 'IN ASSOCIATION WITH UFSC'
        self.__present_intro_text = 'PRESENT'
        self.__game_name_intro_text = 'ASTEROID-PLUS'
        
        self.__skip = False

        skip = Button(self, 10, 10, 100, 70, "SKIP", True, self.skip)
        self.all_sprites.add(skip)

        self.screen_content()

    def skip(self):
        self.__skip = True
    
    #mostra a introdução da compania na tela
    def company_intro(self):
        self.intro_credits_surf = self.intro_credits.render(
            self.company_intro_text, True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surf.get_rect(
            center=(self.display_width / 2, 360)
        )
        self.render_intro_start()
        self.render_intro_end()
    
    #mostra a introdução da associação na tela
    def association_intro(self):
        self.intro_credits_surf = self.intro_credits.render(
            self.association_intro_text, True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surf.get_rect(
            center=(self.display_width / 2, 280)
        )
        self.render_intro_start()
        self.render_intro_end()
        
    #mostra a introdução 'present' na tela, antecedendo o nome do jogo
    def present_intro(self):
        self.intro_credits_surf = self.intro_credits.render(
            self.present_intro_text, True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surf.get_rect(
            center=(self.display_width / 2, 360)
        )
        self.render_intro_start()
        self.render_intro_end()
    
    #mostra o nome do jogo na tela
    def game_name_intro(self):
        self.intro_credits_surf = self.intro_credits.render(
            self.game_name_intro_text, True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surf.get_rect(
            center=(self.display_width / 2, 280)
        )
        self.render_intro_start()
        self.render_intro_end()
        
    #renderiza o aparecimento do texto na tela
    def render_intro_start(self):
        for alpha in range(255, 0, -1):
            pygame.event.get()
            self.fade.set_alpha(alpha)
            self.get_display().blit(self.intro_credits_surf, self.intro_credits_rect)
            self.get_display().blit(self.fade, (0, 0))

            if (self.__skip):
                break
            self.all_sprites.update()
            self.all_sprites.draw(self.get_display())

            pygame.display.flip()
            pygame.time.delay(8)
    
    #renderiza o desaparecimento do texto na tela
    def render_intro_end(self):    
        for alpha in range(0, 255):
            pygame.event.get()
            self.fade.set_alpha(alpha)
            self.get_display().blit(self.intro_credits_surf, self.intro_credits_rect)
            self.get_display().blit(self.fade, (0, 0))

            if (self.__skip):
                break
            self.all_sprites.update()
            self.all_sprites.draw(self.get_display())
 
            pygame.display.flip()
            pygame.time.delay(8)
    
    #conteúdo da tela é formado pelas apresentações
    def screen_content(self):
        self.company_intro()
        self.association_intro()
        self.present_intro()
        self.game_name_intro()
    
    #após a introdução vai para o menu principal
    def handle_transition(self):
        self.get_owner().change_state('MainMenu')

    
    def handle_update(self):
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
 
 