class GameStats:
    """Tracks game statistics"""

    def __init__(self, game):
        self.settings = game.settings
        self.ships_left = self.settings.ship_lives_limit

        self.highest_score = 0
        self.score = 0
        self.level = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_lives_limit
        self.score = 0
        self.level = 0
