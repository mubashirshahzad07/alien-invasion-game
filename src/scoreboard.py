import pygame

from ship import Ship


class ScoreBoard:
    """Handles information related to game score."""

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.render_score()
        self.render_high_score()
        self.render_level()
        self.render_ships()

    def render_score(self):
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

    def render_high_score(self):
        """Render an image from the highest score text."""
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

    def render_level(self):
        """Render an image from the level text."""
        self.level_img = self.font.render(
            str(self.stats.level),
            True,
            self.text_color,
            self.settings.screen_bg_color
        )

        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def render_ships(self):
        """Shows how many ships are left."""
        self.ships = pygame.sprite.Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def display_scoreboard(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.highest_score_img, self.highest_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)

    def update_highest_score(self):
        if self.stats.score > self.stats.highest_score:
            self.stats.highest_score = self.stats.score
            self.render_high_score()
