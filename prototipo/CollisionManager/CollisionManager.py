import pygame
from CollisionManager.Collision import Collision

class CollisionManager:
   #def __init__(self, ship_group, all_asteroids, all_bullets):
    def __init__(self, ship_group, all_asteroids):

        self.__ship_group = ship_group
        self.__all_asteroids = all_asteroids
        #self.__all_bullets = all_bulets


    def all_colisions(self):
        #colisao da nave com asteroids
        self.collision_asteroid_ship()

    def collision_asteroid_ship(self):
        if (Collision(self.ship_group, self.all_asteroids).detect_collision()):
            return True

    def collision_bullet_ship(self):
        # if (Collision(self.bullet_group, self.all_asteroids).detect_collitsion()):
        #return True
        pass


    @property
    def ship_group(self):
        return self.__ship_group

    @property
    def all_asteroids(self):
        return self.__all_asteroids