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
        if (self.collision_enemy_ship()):
            self.ship_life_detect()

        #colisao ship <-> enemy_bullet
        if (self.collision_enemy_bullet_ship()):
            self.ship_life_detect()

        #colisao ship_bullet <-> asteroid
        if (self.collision_bullet_asteroid()):
            #aumento em 1 a pontuação conforme asteroid destruido
            score = self.game.score + 1
            self.game.set_score(score)

        if (self.collision_bullet_enemy()):
            #aumento em 1 a pontuação conforme asteroid destruido
            score = self.game.score + 1
            self.game.set_score(score)

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
            self.game.get_owner().change_state("BossTransition")

    def ship_life_detect(self):
        if (self.ship.life <= 0):
            #passo certos parametros pra result, para poder passar pra tela de RESULT

            #passo pro resultData o tempo de vida
            alive_time = time() - self.game.init__time
            self.game.get_result().set_alive_time(alive_time)
            #passo a pontuação
            self.game.get_result().set_score(self.game.score)
            #troco de estado kkkkkk
            self.game.get_owner().change_state("Result")

    def collision_boss_ship(self) -> bool:
        if (Collision(self.ship_group, self.boss_group).detect_collision()):
            return True
        else:
            return False

    def collision_bullet_boss(self) -> bool:
        if (Collision(self.ship_bullets, self.boss_group).detect_collision()):
            return True
        else:
            return False
    
    def collision_boss_bullet_ship(self) -> bool:
        if (Collision(self.boss_bullets, self.ship_group).detect_collision()):
            return True
        else:
            return False

    #colisao entre asteroids e ship
    def collision_asteroid_ship(self) -> bool:
        if (Collision(self.ship_group, self.all_asteroids).detect_collision()):
            return True
        else:
            return False

    #colisão entre inimigo e ship
    def collision_enemy_ship(self) -> bool:
        if (Collision(self.ship_group, self.enemy_group).detect_collision()):
            return True
        else:
            return False

    #colisão entre tiro do inimigo e ship
    def collision_enemy_bullet_ship(self) -> bool:
        if (Collision(self.ship_group, self.enemy_bullets).detect_collision()):
            return True
        else:
            return False

    #colisao bullet da nave e asteroids
    def collision_bullet_asteroid(self) -> bool:
        if (Collision(self.ship_bullets, self.all_asteroids).detect_collision()):
            return True
        else:
            return False

    #colisaõ entre bullet da nave e inimigo
    def collision_bullet_enemy(self) -> bool:
        if (Collision(self.ship_bullets, self.enemy_group).detect_collision()):
            return True
        else:
            return False


    @property
    def game(self):
        return self.__game

    @property
    def enemy_group(self):
        return self.game.enemy_group

    @property
    def enemy_bullets(self):
        return self.game.enemy_bullets_group

    @property
    def ship_group(self):
        return self.game.ship_group

    @property
    def all_asteroids(self):
        return self.game.all_asteroids

    @property
    def ship_bullets(self):
        return self.game.ship_bullets_group

    @property
    def ship(self):
        return self.game.ship

    @property
    def boss_group(self):
        return self.game.boss_group

    @property
    def boss_bullets(self):
       return self.game.boss_bullets_group 

    @property
    def boss(self):
        return self.game.boss