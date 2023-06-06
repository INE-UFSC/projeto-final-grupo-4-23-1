import pygame
from States.State import State
from Sprites.Button.Button import Button

class Result(State):
    def __init__(self, owner):
        super().__init__(owner)
        self.create_button()


    def screen_content(self):
        self.get_display().fill("black")

        x_pos = self.display_width//2
        y_pos = self.display_height//2

        self.text("-=-=RESULT=-=-", x_pos-150, y_pos-250, 50, "white")
        
        self.text("Level:", x_pos-150, y_pos - 100, 30, "white")
        self.text(str(self.level), x_pos-75, y_pos - 100, 30, "yellow")
        
        self.text("Enemies Destroyed:", x_pos-150, y_pos -50, 30, "white")
        self.text(str(self.enemies_destroyed), x_pos + 50, y_pos -50, 30, "yellow")
        
        self.text("Score:", x_pos-150, y_pos, 30, "white")
        self.text(str(self.score), x_pos-75, y_pos, 30, "yellow")


    def create_button(self) -> None:
        x_pos = self.display_width//2
        y_pos = self.display_height//2

        retry = Button(x_pos-310, y_pos+150, 300, 100, "RETRY", self.retry)
        self.all_sprites.add(retry)

        menu =Button(x_pos+10, y_pos+150, 300, 100, "MENU", self.menu)
        self.all_sprites.add(menu)
    
    def reset_data(self):
        self.get_game_data().set_enemies_destroyed(0) 
        self.get_game_data().set_level(1) 
        
        life = 3 + self.get_owner().game_data.profile.ship_life
        self.get_game_data().set_ship_life(life)
    
    def retry(self):
        self.reset_data()
        self.get_owner().change_state('NormalLevel')
    
    def menu(self):
        self.reset_data()
        self.get_owner().change_state('ProfileMenu')
    

    def handle_update(self):
        pygame.display.update()
        self.screen_content()
        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())
        pygame.display.update()

    @property
    def level(self):
        return self.get_game_data().level

    @property
    def score(self):
        return self.get_game_data().score

    @property
    def enemies_destroyed(self):
        return self.get_game_data().enemies_destroyed

