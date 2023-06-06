from CollisionManager.Collision import Collision
from time import time

class CollisionManager:
    #recebe grupo de sprites para detectar colisao
    def __init__(self, game) -> None:

        self.__game = game


    #ações realisadas no jogo quando é detectado colisão
    def collisions_normal_level(self) -> None:
        #colisao ship <-> asteroid
        if (self.collision_asteroid_ship()):
            self.ship_life_detect()

        #colisao ship <-> enemy
        if (self.collision_basic_enemy_ship()):
            self.ship_life_detect()

        #colisao ship <-> enemy_bullet
        if (self.collision_basic_enemy_bullet_ship()):
            self.ship_life_detect()

        #colisao ship_bullet <-> asteroid
        if (self.collision_bullet_asteroid()):
            enemys_destroied = self.game.enemys_destroied + 1
            self.game.set_enemys_destroied(enemys_destroied)

        if (self.collision_bullet_enemy()):
            enemys_destroied = self.game.enemys_destroied + 1
            self.game.set_enemys_destroied(enemys_destroied)
       

    def collisions_boss_level(self):
        if (self.collision_boss_ship()):
            self.ship_life_detect()
            self.boss_life_detect()

        if (self.collision_bullet_boss()):
            self.ship_life_detect()
            self.boss_life_detect()

        if (self.collision_boss_bullet_ship()):
            self.ship_life_detect()


    def boss_life_detect(self):
        if (self.boss.life <= 0):
            level = self.game.get_owner().game_data.level + 1
            self.game.get_owner().game_data.set_level(level)

            enemys_destroied = self.game.enemys_destroied + 1
            self.game.set_enemys_destroied(enemys_destroied)
 
            self.game.get_owner().change_state("BossTransition")

    def ship_life_detect(self):
        if (self.ship.life <= 0):
            self.game.get_owner().change_state("Result")

    #boss <-> ship
    def collision_boss_ship(self) -> bool:
        if (Collision(self.ship_group, self.boss_group).detect_collision()):
            return True
        else:
            return False

    #ship_bullet <-> boss
    def collision_bullet_boss(self) -> bool:
        if (Collision(self.ship_bullet, self.boss_group).detect_collision()):
            return True
        else:
            return False
    
    #boss_bullet <-> ship
    def collision_boss_bullet_ship(self) -> bool:
        if (Collision(self.boss_bullet, self.ship_group).detect_collision()):
            return True
        else:
            return False

    #asteroid <-> ship
    def collision_asteroid_ship(self) -> bool:
        if (Collision(self.ship_group, self.asteroid_group).detect_collision()):
            return True
        else:
            return False

    #basic_enemy <-> ship
    def collision_basic_enemy_ship(self) -> bool:
        if (Collision(self.ship_group, self.basic_enemy_group).detect_collision()):
            return True
        else:
            return False

    #basic_enemy_bullet <-> ship
    def collision_basic_enemy_bullet_ship(self) -> bool:
        if (Collision(self.ship_group, self.basic_enemy_bullet).detect_collision()):
            return True
        else:
            return False

    #ship_bullet <-> asteroid
    def collision_bullet_asteroid(self) -> bool:
        if (Collision(self.ship_bullet, self.asteroid_group).detect_collision()):
            return True
        else:
            return False

    #ship_bullet <-> basic_enemy
    def collision_bullet_enemy(self) -> bool:
        if (Collision(self.ship_bullet, self.basic_enemy_group).detect_collision()):
            return True
        else:
            return False


    @property
    def game(self):
        return self.__game

    @property
    def basic_enemy_group(self):
        return self.game.basic_enemy_group

    @property
    def basic_enemy_bullet(self):
        return self.game.basic_enemy_bullet_group

    @property
    def ship_group(self):
        return self.game.ship_group

    @property
    def asteroid_group(self):
        return self.game.asteroid_group

    @property
    def ship_bullet(self):
        return self.game.ship_bullet_group

    @property
    def ship(self):
        return self.game.ship

    @property
    def boss_group(self):
        return self.game.boss_group

    @property
    def boss_bullet(self):
       return self.game.boss_bullet_group 

    @property
    def boss(self):
        return self.game.boss