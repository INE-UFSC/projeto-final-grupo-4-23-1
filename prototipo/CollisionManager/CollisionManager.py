import pygame
from CollisionManager.Collision import Collision

class CollisionManager:
    def __init__(self, ship_group, all_asteroids):

        self.__ship_group = ship_group
        self.__all_asteroids = all_asteroids


    def all_colisions(self):
        #colisao da nave com asteroids
        self.collision_asteroid_ship()

    def collision_asteroid_ship(self):
        if (Collision(self.__ship_group, self.all_asteroids).detect_collision()):
            return True

        

    @property
    def asteroid_game(self):
        return self.__asteroid_game

    @property
    def ship_group(self):
        return self.__ship_group

    @property
    def all_asteroids(self):
        return self.__all_asteroids