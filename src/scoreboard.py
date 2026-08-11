import pygame


class ScoreBoard:
    """Handles information related to game score."""

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prepare_score()

    def prepare_score(self):
        """Render an image from the score text."""
        self.score_img = self.font.render(
            str(self.stats.score),
            True,
            self.text_color,
            self.settings.screen_bg_color
        )

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def display_score(self):
        self.screen.blit(self.score_img, self.score_rect)
