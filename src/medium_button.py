import pygame


class MediumButton:
    """Create medium button for the game and change the initial settings accordingly."""

    def __init__(self, game, message):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

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

    def initialize_medium_settings(self):
        self.ship_speed = 2
        self.ship_lives_limit = 3

        self.bullet_speed = 2.5

        self.bullet_width = 3
        self.bullet_height = 15
        self.ship_bullet_color = (3, 102, 252)
        self.bullets_allowed = 5

        self.alien_speed = 1.0
        self.alien_points = 50
        self.fleet_drop_speed = 15
        self.fleet_direction = 1   # 1 means towards +x axis, -1 means towards -x axis

        self.alien_bullets_limit = 2
        self.alien_bullet_color = (252, 3, 44)

        self.raindrop_speed = 3

        self.speedup_scale = 1.5
        self.score_scale = 1.7

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)