import pygame
from States.State import State
from Profiles.Profile import Profile
from Sprites.MovingSprites.Ship.Ship import Ship
from Sprites.MovingSprites.TankBoss.TankBoss import TankBoss
from CollisionManager.CollisionManager import CollisionManager
from random import randint
from time import time

class BossLevel(State):
    def __init__(self, owner) -> None:
        super().__init__(owner)

        self.__collision_manager = CollisionManager(self)

        self.__profile: Profile = self.get_game_data().profile

        tankboss = TankBoss(game=self, life=10, position=(self.display_width//2, 30))
        self.__boss_list = [tankboss]

        self.__ship_group = pygame.sprite.Group()
        self.__ship_bullet_group = pygame.sprite.Group()
        self.__boss_group = pygame.sprite.Group()
        self.__boss_bullet_group = pygame.sprite.Group()

        life = (3+self.profile.ship_life-1) if (self.get_game_data().ship_life == None) else self.get_game_data().ship_life
        self.get_game_data().set_ship_life(life)

        #apagar dps
        self.init_time = time()

        level = 1 if (self.level == None) else self.level
        self.get_game_data().set_level(level)

        self.add_ship()
        self.sort_boss()

        self.__clock = pygame.time.Clock()

    def sort_boss(self) -> None:
        self.__boss = self.boss_list[randint(0, len(self.boss_list)-1)]
        self.__original_boss_life = self.boss.life
        self.all_sprites.add(self.boss)
        self.boss_group.add(self.boss)

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

    def render_boss_life(self):
        x_poss = self.display_width//2
        y_poss = self.display_height//2

        width = 360

        pygame.draw.rect(self.get_display(), "gray", (x_poss-width//2, self.display_height-40, width, 15))
        pygame.draw.rect(self.get_display(), "red", (x_poss-width//2, self.display_height-40, (width//self.original_boss_life)*self.boss.life, 15))

    def screen_content(self):
        self.get_display().fill("black")

        self.render_boss_life()

        x_pos = self.display_width//2
        y_pos = self.display_width//2

        self.all_sprites.update()
        self.all_sprites.draw(self.get_display())

        self.text("Level:", x_pos-50, 10, 30, "white")
        self.text(str(self.level), x_pos+10, 10, 30, "yellow")

        self.text("Enemies destroyed:", 10, 10, 30, "white")
        self.text(str(self.enemies_destroyed), 210, 10, 30, "yellow")

        self.text("Score:", 10, 35, 30, "white")
        self.text(str(self.score), 75, 35, 30, "yellow")

        self.text("Life:", self.display_width-80, 10, 30, "white")
        self.text(str(self.ship.life), self.display_width-30, 10, 30, "yellow")    

        self.text("BOSS LIFE", x_pos-50, self.display_height-70, 30, "red")

    def level_transition(self):
        pass

    def handle_update(self):
        self.clock.tick(60)
        pygame.display.update()
        self.screen_content()
        self.collision_manager.collisions_boss_level()
        self.level_transition()
        pygame.display.update()

    def set_enemies_destroyed(self, num: int) -> None:
        self.get_game_data().set_enemies_destroyed(num)

    @property
    def original_boss_life(self):
        return self.__original_boss_life

    @property
    def collision_manager(self):
        return self.__collision_manager

    @property
    def enemies_destroyed(self):
        return self.get_game_data().enemies_destroyed

    @property
    def score(self):
        return self.get_game_data().score

    @property
    def level(self):
        return self.get_game_data().level

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
    def boss_list(self):
        return self.__boss_list

    @property
    def boss_group(self):
        return self.__boss_group

    @property
    def boss(self):
        return self.__boss

    @property
    def boss_bullet_group(self):
        return self.__boss_bullet_group