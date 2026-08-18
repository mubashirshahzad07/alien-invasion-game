import pygame


class EasyButton:
    """Create easy button for the game and change the initial settings accordingly."""

    def __init__(self, game, message):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.rect.y += 100

        self._prepare_message(message)

    def _prepare_message(self, message):
        self.msg_image = self.font.render(
            message,
            True,
            self.text_color,
            self.button_color
        )

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def initialize_easy_settings(self):
        self.settings.ship_speed -= 1
        self.settings.ship_lives_limit = 5 

        self.settings.bullet_speed -= 1
        self.settings.bullets_allowed = 7

        self.settings.alien_speed -= 1.0
        self.settings.alien_points -= 30

        self.settings.alien_bullets_limit = 1

        self.settings.speedup_scale = 1.1
        self.settings.score_scale = 1.4

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)