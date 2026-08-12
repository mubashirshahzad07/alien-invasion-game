import pygame

from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage ship."""

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/fighter.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Precisely store and increase the value, even when ship speed is float
        # - self.rect.x will store every value as int, when ship speed is float
        # the values stored would be incorrect.
        # To overcome this error we introduce a new attribute that will keep
        # the float changes and at last is used to update self.rect.x value.
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.settings = game.settings

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        if self.moving_up and self.rect.top > self.screen_rect.top + 110:
            self.y -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update Rect object using modified self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at the current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Places the ship at the center."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
