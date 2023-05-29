import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, text: str, callback) -> None:
        super().__init__()

        self.__callback = callback
        self.__norm_image = pygame.Surface([300, 100], pygame.SRCALPHA)
        pygame.draw.rect(self.__norm_image, (50,50,50), (0, 0, 300, 100))
        pygame.draw.rect(self.__norm_image, (5,5,5), (10, 10, 280, 80))

        self.__hover_image = pygame.Surface([300, 100], pygame.SRCALPHA)
        pygame.draw.rect(self.__hover_image, (50, 50, 50), (0, 0, 300, 100))
        pygame.draw.rect(self.__hover_image, (150, 150, 150), (10, 10, 280, 80))

        self.__font = pygame.font.SysFont(None, 30)
        textSurface = self.__font.render(text, True, (255, 255, 255))
        textRect = textSurface.get_rect(center = (150, 50))
        self.__norm_image.blit(textSurface, textRect)
        self.__hover_image.blit(textSurface, textRect)

        self.__image = self.__norm_image
        self.__rect = self.__image.get_rect(topleft=(x, y))

    def update(self) -> None:
        if self.__rect.collidepoint(pygame.mouse.get_pos()):
            self.__image = self.__hover_image
            if pygame.mouse.get_pressed()[0]:
                self.__callback()
        else:
            self.__image = self.__norm_image

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect