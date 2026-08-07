class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg_color = (230, 230, 230)

        self.ship_speed = 2.5

        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1 means towards +x axis, -1 means towards -x axis
        self.fleet_direction = 1
