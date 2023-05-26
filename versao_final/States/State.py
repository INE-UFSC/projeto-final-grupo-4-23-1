import pygame
from Profiles.ProfileManager import ProfileManager
from Profiles.Profile import Profile
from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, owner):
        #Game é o parâmetro owner. Assim é possível fazer a transição de estados com o change_state
        self.__owner = owner

        #altura e largura da tela
        self.__display_width = pygame.display.Info().current_w
        self.__display_height = pygame.display.Info().current_h

        #todos os sprites
        self.__all_sprites = pygame.sprite.Group()

    def get_display(self):
        return pygame.display.get_surface()

    def get_owner(self):
        return self.__owner
    
    def get_result(self):
        return self.__owner.result_data

    def get_all_sprites(self):
        return self.__all_sprites

    #verifica se o perfil existe pelo nome
    #True -> perfil existe
    #False -> perfil não existe
    def verify_profile_existence(self, name: str) -> bool:
        return ProfileManager().verify_profile_existence()

    #retorna um perfil pelo nome
    #retorna o perfil se existir
    # se o perfil NAO existir retorna FALSE
    def get_profile(self, name: str) -> Profile:
        return ProfileManager().get_profile(name)

    #retora uma lista ORDENADA de todos os perfils
    def get_all_profiles(self) -> list[Profile]:
        return ProfileManager().get_all_profiles()

    #salva um perfil ja existente
    #True -> salvado com sucesso
    #False -> Perfil não existe
    def save_profile(profile: Profile) -> bool:
        return ProfileManager().save_profile()

    #cria um novo perfil
    #Dá erro se o perfil já existir
    def create_profile(self, name: str,
                       credit: int,
                       max_score: int,
                       ship_damage: int,
                       ship_vel_max: float,
                       ship_life: int,
                       ship_cooldown: int,
                       ship_qtd_bullet: int) -> None:
        return ProfileManager().create_profile(name, credit, max_score, ship_damage, ship_vel_max, ship_life, ship_cooldown, ship_qtd_bullet)
    

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

    @property
    def all_sprites(self):
        return self.__all_sprites