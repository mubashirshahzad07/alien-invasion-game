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
        self.prepare_high_score()

    def prepare_score(self):
        """Render an image from the score text."""
        score = f"{round(self.stats.score, -1): ,}"
        self.score_img = self.font.render(
            score,
            True,
            self.text_color,
            self.settings.screen_bg_color
        )

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prepare_high_score(self):
        """Render an image from the score text."""
        highest_score = f"{round(self.stats.highest_score, -1): ,}"
        self.highest_score_img = self.font.render(
            highest_score,
            True,
            self.text_color,
            self.settings.screen_bg_color
        )

        self.highest_score_rect = self.highest_score_img.get_rect()
        self.highest_score_rect.centerx = self.screen_rect.centerx
        self.highest_score_rect.top = self.score_rect.top

    def display_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.highest_score_img, self.highest_score_rect)

    def update_highest_score(self):
        if self.stats.score > self.stats.highest_score:
            self.stats.highest_score = self.stats.score
            self.prepare_high_score()
