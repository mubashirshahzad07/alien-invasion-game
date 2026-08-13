import pygame

from pygame.sprite import Sprite


class RainDrop(Sprite):

    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/drop.bmp")

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y