import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite):
    """A class to manage bullets fired from the aliens."""

    def __init__(self, game, alien):
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.alien_bullet_color

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )

        self.rect.midbottom = alien.rect.midbottom
        self.rect.top = alien.rect.bottom

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)