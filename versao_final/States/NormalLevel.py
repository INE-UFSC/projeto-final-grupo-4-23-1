import pygame
from States.State import State
from Profiles.Profile import Profile
from Sprites.MovingSprites.Ship.Ship import Ship
from CollisionManager.CollisionManager import CollisionManager
from time import time

class NormalLevel(State):
    def __init__(self, owner) -> None:
        super().__init__(owner)

        self.__colision_manager = CollisionManager(self)

        self.__profile: Profile = self.get_game_data().profile

        self.__ship_group = pygame.sprite.Group()
        self.__ship_bullet_group = pygame.sprite.Group()
        self.__asteroid_group = pygame.sprite.Group()
        self.__basic_enemy_group = pygame.sprite.Group()
        self.__basic_enemy_bullet_group = pygame.sprite.Group()

        life = (3+self.profile.ship_life-1) if (self.get_game_data().ship_life == None) else self.get_game_data().ship_life
        self.get_game_data().set_ship_life(life)

        level = 1 if (self.level == None) else self.level
        self.get_game_data().set_level(level)

        enemies_destroyed = 0 if (self.enemies_destroyed == None) else self.enemies_destroyed
        self.set_enemies_destroyed(enemies_destroyed)
        self.set_score()

        self.__next_level_time = time()+30

        self.add_ship()

        self.__clock = pygame.time.Clock()


    def add_ship(self) -> None:
        vel_max = 10*(1.2)**(self.profile.ship_vel_max-1)
        cooldown = 0.8 - (0.15 * (self.profile.ship_cooldown-1))
        damage = self.profile.ship_damage
        qtd_bullet = self.profile.ship_qtd_bullet

        life = self.get_game_data().ship_life

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

        x_pos = self.display_width//2
        y_pos = self.display_width//2

        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())

        self.text("Level:", x_pos-50, 10, 30, "white")
        self.text(str(self.level), x_pos+10, 10, 30, "yellow")
        self.text("Next Level in %d sec"%int(self.next_level_time-time()), 10, self.display_height-25, 30, "white")

        self.text("Enemies Destroyed:", 10, 10, 30, "white")
        self.text(str(self.enemies_destroyed), 210, 10, 30, "yellow")

        self.text("Score:", 10, 35, 30, "white")
        self.text(str(self.score), 75, 35, 30, "yellow")

        self.text("Life:", self.display_width-80, 10, 30, "white")
        self.text(str(self.ship.life),self.display_width-30, 10, 30, "yellow")

    def level_transition(self):
        if (self.next_level_time-time() <= 0):
            self.__next_level_time = time() + 30
            self.get_game_data().set_level(self.level+1)
            if ((self.level % 5) != 0):
                self.get_sound_mixer().play_lvl_up_sfx()

            if ((self.level % 5) == 0):
                self.get_owner().change_state("BossTransition")

    def set_enemies_destroyed(self, num: int) -> None:
        self.get_game_data().set_enemies_destroyed(num)

    def set_score(self) -> None:
        self.get_game_data().set_score(self.enemies_destroyed*self.level)

    def handle_update(self):
        self.clock.tick(60)
        pygame.display.update()
        self.background(0.2*8)
        self.screen_content()
        self.collision_manager.collisions_normal_level()
        self.level_transition()
        pygame.display.update()

    @property
    def collision_manager(self):
        return self.__colision_manager

    @property
    def level(self):
        return self.get_game_data().level

    @property
    def score(self):
        return self.get_game_data().score

    @property
    def enemies_destroyed(self):
        return self.get_game_data().enemies_destroyed

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
    def ship_bullet_group(self):
        return self.__ship_bullet_group

    @property
    def asteroid_group(self):
        return self.__asteroid_group

    @property
    def basic_enemy_group(self):
        return self.__basic_enemy_group

    @property
    def basic_enemy_bullet_group(self):
        return self.__basic_enemy_bullet_group

    @property
    def next_level_time(self):
        return self.__next_level_time