import pygame
from CollisionManager.Collision import Collision

class CollisionManager:
    #recebe grupo de sprites para detectar colisao
    def __init__(self, ship_group: pygame.sprite.Group,
                 all_asteroids: pygame.sprite.Group,
                 all_bullets: pygame.sprite.Group,
                 enemy_group: pygame.sprite.Group,
                 enemy_bullet_group: pygame.sprite.Group) -> None:

        self.__ship_group = ship_group
        self.__all_asteroids = all_asteroids
        self.__all_bullets = all_bullets
        self.__enemy_group = enemy_group
        self.__enemy_bullet_group = enemy_bullet_group

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
        if (Collision(self.ship_group, self.enemy_bullet_group).detect_collision()):
            return True
        else:
            return False

    #colisao bullet da nave e asteroids
    def collision_bullet_asteroid(self) -> bool:
        if (Collision(self.all_bullets, self.all_asteroids).detect_collision()):
            return True
        else:
            return False

    #colisaõ entre bullet da nave e inimigo
    def collision_bullet_enemy(self) -> bool:
        if (Collision(self.all_bullets, self.enemy_group).detect_collision()):
            return True
        else:
            return False

    

    @property
    def enemy_group(self):
        return self.__enemy_group

    @property
    def enemy_bullet_group(self):
        return self.__enemy_bullet_group

    @property
    def ship_group(self):
        return self.__ship_group

    @property
    def all_asteroids(self):
        return self.__all_asteroids

    @property
    def all_bullets(self):
        return self.__all_bullets
