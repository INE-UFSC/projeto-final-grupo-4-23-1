import pygame
from States.State import State
from Profiles.Profile import Profile
from Sprites.Ship.Ship import Ship
from time import time

class BossLevel(State):
    def __init__(self, owner) -> None:
        super().__init__(owner)

        self.__profile: Profile = self.get_owner().game_data.profile

        self.__ship_group = pygame.sprite.Group()
        self.__ship_bullets_group = pygame.sprite.Group()

        #apagar dps
        self.init_time = time()

        level = 1 if (self.level == None) else self.level
        self.get_owner().game_data.set_level(level)

        self.add_ship()

        self.__clock = pygame.time.Clock()


    def add_ship(self) -> None:
        vel_max = 10*(1.2)**(self.profile.ship_vel_max-1)
        cooldown = 0.8 - (0.15 * (self.profile.ship_cooldown-1))
        damage = self.profile.ship_damage
        qtd_bullet = self.profile.ship_qtd_bullet

        life = self.get_owner().game_data.ship_life

        self.__ship = Ship(game = self,
                           speed = vel_max*0.3,
                           vel_max = vel_max,
                           cooldown = cooldown,
                           life = life,
                           damage = damage,
                           qtd_bullet = qtd_bullet)

        self.all_sprites.add(self.ship)
        self.ship_group.add(self.ship)

    def create_button(self):
        pass

    def screen_content(self):
        self.get_display().fill("black")

        x_pos = self.display_width//2
        y_pos = self.display_width//2

        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())

        self.text("Level: %d"%self.level, x_pos-50, 10, 30, "white")
        self.text(str(time() - self.init_time), 10, 10, 30, "white")

    def level_transition(self):
        #não é isso, apagar dps
        if (time() - self.init_time > 5):
            self.get_owner().game_data.set_level(self.level+1)
            self.get_owner().change_state("BossTransition")

    def handle_update(self):
        self.clock.tick(60)
        pygame.display.update()
        self.screen_content()
        self.level_transition()
        pygame.display.update()

    @property
    def level(self):
        return self.get_owner().game_data.level

    @property
    def clock(self):
        return self.__clock

    @property
    def ship(self):
        return self.__ship

    @property
    def profile(self):
        return self.__profile

    @property
    def ship_group(self):
        return self.__ship_group

    @property
    def ship_bullets_group(self):
        return self.__ship_bullets_group
