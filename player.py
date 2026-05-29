import pygame

class Player:

    def __init__(self):

        self.x = 350
        self.y = 500

        self.width = 50
        self.height = 50

        self.speed = 5

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed

        if keys[pygame.K_RIGHT] and self.x < 750:
            self.x += self.speed

    def draw(self, screen):

        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))

    def get_rect(self):

        return pygame.Rect(self.x, self.y, self.width, self.height)
