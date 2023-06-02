import pygame

class InputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        
        self.__rect = pygame.Rect(x, y, width, height)
        self.__color = pygame.Color('white')
        self.__text = ''
        self.__font = pygame.font.Font(None, 32)
        self.__active = False
        self.__norm_image = pygame.Surface([width, height], pygame.SRCALPHA)
        
        pygame.draw.rect(self.__norm_image, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.__norm_image.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
     
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
   
            self.text = ''

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
            
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
         
                    self.text = self.text[:-1]
                else:
          
                    self.text += event.unicode

    def update(self):

        self.color = pygame.Color('yellow') if self.active else pygame.Color('white')

    def draw(self, screen):

        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
    
    @property 
    def rect(self):
        return self.__rect
    @property 
    def color(self):
        return self.__color
    @property 
    def text(self):
        return self.__text
    @property 
    def font(self):
        return self.__font
    @property 
    def active(self):
        return self.__active