class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg_color = (230, 230, 230)

        self.ship_speed = 2.5
        self.ship_lives_limit = 2

        self.bullet_speed = 2.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        self.alien_speed = 1.0
        self.alien_points = 50
        self.fleet_drop_speed = 150
        # 1 means towards +x axis, -1 means towards -x axis
        self.fleet_direction = 1

        self.speedup_scale = 1.2
        self.score_scale = 1.5

    def reset_game_speeds(self):
        """Reset the speeds when the game is restarted."""
        self.ship_speed = 2.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        self.alien_points = 50
        self.fleet_direction = 1

    def increase_game_speed(self):
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)
