class GameStats:
    """Tracks game statistics"""

    def __init__(self, game):
        self.settings = game.settings
        self.ships_left = self.settings.ship_lives_limit

    def reset_stats(self):
        self.ships_left = self.settings.ship_lives_limit
