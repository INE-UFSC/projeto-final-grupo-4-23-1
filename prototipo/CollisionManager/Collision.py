import pygame

class Collision:
    def __init__(self, group1, group2):
        self.__group1 = group1
        self.__group2 = group2

    def detect_collision(self):
        #nos parametros é dado 2 sprite.group, e quando detecta colisao
        #é retornado um dicionario em que as chaves são os sprites que "bateram" do grupo 1
        # e nos valores é uma lista dos sprites que colidiram
        collision_dict = pygame.sprite.groupcollide(self.group1, self.group2, False, False)

        if (collision_dict):
            collision_mask = pygame.sprite.groupcollide(self.group1, self.group2, False, False, pygame.sprite.collide_mask)

            if (collision_mask):
                group1 = collision_dict.keys()
                group2 = collision_dict.values()

                for x1 in group1:
                    x1.hit()

                for g2 in group2:
                    for x2 in g2:
                        x2.hit()

                return True
        else:
            return False

    @property
    def group1(self):
        return self.__group1

    @property
    def group2(self):
        return self.__group2