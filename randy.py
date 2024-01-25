import pygame
from random import *

class randy(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        x = randint(0, 500)
        y = randint(0, 500)
        self.rect.x = x
        self.rect.y = y

