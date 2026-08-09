class GameStats:
    """Tracks game statistics"""

    def __init__(self, game):
        self.settings = game.settings

        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_lifes_limit