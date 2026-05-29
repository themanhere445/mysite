import pygame
import random

class Enemy:

    def __init__(self):

        self.x = random.randint(0, 750)
        self.y = 0

        self.width = 50
        self.height = 50

        self.speed = 5

    def move(self):

        self.y += self.speed

    def reset(self):

        self.y = 0
        self.x = random.randint(0, 750)

    def draw(self, screen):

        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def get_rect(self):

        return pygame.Rect(self.x, self.y, self.width, self.height)
