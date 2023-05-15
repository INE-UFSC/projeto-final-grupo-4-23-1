import pygame
from CollisionManager.Collision import Collision

class CollisionManager:
    #recebe grupo de sprites para detectar colisao
    def __init__(self, ship_group: pygame.sprite.Group,
                 all_asteroids: pygame.sprite.Group,
                 all_bullets: pygame.sprite.Group) -> None:

        self.__ship_group = ship_group
        self.__all_asteroids = all_asteroids
        self.__all_bullets = all_bullets

    #colisao entre asteroids e ship
    def collision_asteroid_ship(self) -> bool:
        if (Collision(self.ship_group, self.all_asteroids).detect_collision()):
            return True
        else:
            return False

    #colisao bullet e asteroids
    def collision_bullet_asteroid(self) -> bool:
        if (Collision(self.all_bullets, self.all_asteroids).detect_collision()):
            return True
        else:
            return False

    @property
    def ship_group(self):
        return self.__ship_group

    @property
    def all_asteroids(self):
        return self.__all_asteroids

    @property
    def all_bullets(self):
        return self.__all_bullets
