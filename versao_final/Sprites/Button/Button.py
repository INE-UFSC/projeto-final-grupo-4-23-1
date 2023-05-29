import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, heigth: int, text: str, callback) -> None:
        super().__init__()

        self.__width = width
        self.__heigth = heigth

        self.__callback = callback
        self.__norm_image = pygame.Surface([self.width, self.heigth], pygame.SRCALPHA)
        pygame.draw.rect(self.__norm_image, (50,50,50), (0, 0, self.width, self.heigth))
        pygame.draw.rect(self.__norm_image, (5,5,5), (self.heigth*0.1, self.heigth*0.1, self.width-2*(self.heigth*0.1), self.heigth-2*(self.heigth*0.1)))

        self.__hover_image = pygame.Surface([self.width, self.heigth], pygame.SRCALPHA)
        pygame.draw.rect(self.__hover_image, (50, 50, 50), (0, 0, self.width, self.heigth))
        pygame.draw.rect(self.__hover_image, (150, 150, 150), (self.heigth*0.1, self.heigth*0.1, self.width-2*(self.heigth*0.1), self.heigth-2*(self.heigth*0.1)))

        self.__font = pygame.font.SysFont(None, 30)
        textSurface = self.__font.render(text, True, (0, 255, 255))
        textRect = textSurface.get_rect(center = (self.width//2, self.heigth//2))
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

    @property
    def width(self):
        return self.__width

    @property
    def heigth(self):
        return self.__heigth