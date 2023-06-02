import pygame

class InputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        
        self.__rect = pygame.Rect(x, y, width, height)
        self.__text = ''
        self.__font = pygame.font.Font(None, 32)
        self.__active = False
        self.__image = pygame.Surface([width, height], pygame.SRCALPHA)
        
        pygame.draw.rect(self.__image, (50, 50, 50), (0, 0, 300, 100))
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.__image.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        

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
        keys = pygame.key.get_pressed()
        mouse_buttons = pygame.mouse.get_pressed()

        if mouse_buttons[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.active = True

            else:
                self.active = False
            self.change_color()

        if self.active:
            if keys[pygame.K_RETURN]:
                print(self.text)
                self.text = ''
            elif keys[pygame.K_BACKSPACE]:
                self.text = self.text[:-1]
            else:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        self.text += event.unicode

        
        print(self.text)

    def change_color(self):
        if self.active:
            return pygame.draw.rect(self.image, (100, 100, 100), (0, 0, 300, 100))
        else:
            return pygame.draw.rect(self.__image, (50, 50, 50), (0, 0, 300, 100))
    
    @property 
    def rect(self):
        return self.__rect
    @property
    def image(self):
        return self.__image
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
    @rect.setter 
    def rect(self, rect):
        self.__rect = rect
    @color.setter 
    def color(self, color):
        self.__color = color
    @text.setter
    def text(self, text):
        self.__text = text
    @font.setter
    def font(self, font):
        self.__font = font
    @active.setter
    def active(self, active):
        self.__active = active