import pygame


class InputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.__rect = pygame.Rect(x, y, width, height)
        self.__text = ""
        self.__font = pygame.font.Font(None, 52)
        self.__active = False
        self.__image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.__width = width
        self.__height = height
        self.__cursor_pos = len(self.text)
        pygame.draw.rect(self.image, (50, 50, 50), (0, 0, 300, 100))


    def update(self):
        keys = pygame.key.get_pressed()
        mouse_buttons = pygame.mouse.get_pressed()

        if mouse_buttons[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.active = True
            else:
                self.active = False

        if self.active:
            if keys[pygame.K_LEFT]:
                self.cursor_pos = max(0, self.cursor_pos - 1)
            elif keys[pygame.K_RIGHT]:
                self.cursor_pos = min(len(self.text), self.cursor_pos + 1)
            elif keys[pygame.K_HOME]:
                self.cursor_pos = 0
            elif keys[pygame.K_END]:
                self.cursor_pos = len(self.text)
                
            elif keys[pygame.K_RETURN]:
                print(self.text)
                
            elif keys[pygame.K_BACKSPACE]:
                self.text = self.text[:-1]
            elif keys[pygame.K_DELETE]:
                self.text = self.text[1:]
            else:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        self.text += event.unicode
        self.render_text()


        print(self.text)

    def render_text(self):
        x = 0  
        y = self.height // 2 
        cursor_x = self.cursor_pos
        
        self.change_color()

        for char in self.text:
            char_surface = self.font.render(char, True, (255, 255, 255))
            char_rect = char_surface.get_rect(topleft=(x, y))
            self.image.blit(char_surface, char_rect)
            x += char_rect.width + 2

        if self.active:
            for i in range(self.cursor_pos):
                char_surface = self.font.render(self.text[i], True, (255, 255, 255))
                cursor_x += char_surface.get_width() + 2

            cursor_surface = self.font.render("|", True, (255, 255, 255))
            cursor_rect = cursor_surface.get_rect(topleft=(cursor_x, y))
            self.image.blit(cursor_surface, cursor_rect.move((0, 2)))  
           
        
    def verify_text_box_collision(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.active = True

        else:
            self.active = False
            self.change_color()

    def text_detect(self, keys):
        if keys[pygame.K_RETURN]:
            print(self.text)
            self.text = ""
        elif keys[pygame.K_BACKSPACE]:
            self.text = self.text[:-1]
        else:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.text += event.unicode
    

    def change_color(self):
        if self.active:
            pygame.draw.rect(self.image, (100, 100, 100), (0, 0, 300, 100))
        else:
            pygame.draw.rect(self.image, (50, 50, 50), (0, 0, 300, 100))


    @property
    def rect(self):
        return self.__rect
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height

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
    def cursor_pos(self):
        return self.__cursor_pos

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
    
    @cursor_pos.setter
    def cursor_pos(self, position):
        self.__cursor_pos = position
        
