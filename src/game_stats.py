class GameStats:
    """Tracks game statistics"""

    def __init__(self, game):
        self.settings = game.settings

        self.ships_left = self.settings.ship_lives_limit
        self.highest_score = 0
        self.score = 0
        self.level = 0

        self._load_highest_score()

    def reset_stats(self):
        self.ships_left = self.settings.ship_lives_limit
        self.score = 0
        self.level = 0

    def _load_highest_score(self):
        try:
            with open("highest_score.txt") as hs_file:
                prev_highest = hs_file.read().strip()
                if prev_highest.isnumeric():
                    self.highest_score = int(prev_highest)
                else:
                    self.highest_score = 0
        except FileNotFoundError:
            self.highest_score = 0
