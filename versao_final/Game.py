import pygame
from States.MainMenu import MainMenu
from States.AsteroidGame import AsteroidGame
from States.SelectProfile import SelectProfile
from States.Result import Result 
from Utility.GameData import GameData

class Game:
    def __init__(self, name = 'Asteroid'):
        pygame.init()
        self.__running = True
        self.__display_width = 1440
        self.__display_height = 1080
        self.__game_data = GameData()

        self.display = pygame.display.set_mode((self.display_width, self.display_height))
        #dicionário com os estados do jogo
        self.__states_dictionary = {'MainMenu': MainMenu,
                                    'AsteroidGame': AsteroidGame,
                                    'SelectProfile': SelectProfile,
                                    'Result': Result}
        #estado atual (começa no Main Menu)
        self.__current_state = MainMenu(self)

    def run(self):

        pygame.display.set_caption("ASTEROIDS")

        while self.running:
            self.handle_update()
            self.handle_transition()
 
        
        pygame.quit()
    
    #altera o estado atual com base na string que informa o nome do próximo estado
    def change_state(self, next_state_str):
        next_state = self.get_states_dictionary()[next_state_str](self)
        self.set_current_state(next_state)
 
    def close(self):
        self.__running = False
        
    def get_current_state(self):
        return self.__current_state
    
    def set_current_state(self, next_state):
        self.__current_state = next_state
        
    def get_states_dictionary(self):
        return self.__states_dictionary
  
    def get_display(self):
        return self.display
    
    def handle_transition(self):
        return self.get_current_state().handle_transition()
    
    def handle_update(self):
        return self.get_current_state().handle_update()

    @property
    def game_data(self):
        return self.__game_data

    @property
    def display_width(self):
        return self.__display_width

    @property
    def display_height(self):
        return self.__display_height

    @property
    def running(self):
        return self.__running
 