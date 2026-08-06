import pygame


class Ship:
    """A class to manage ship."""

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/fighter.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at the current location."""
        self.screen.blit(self.image, self.rect)
