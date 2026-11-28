class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        self.screen_width = 1200
        self.screen_height = 800

        # RGB, 0 to 255 each
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_img = 'resources/ship.bmp'
        self.ship_speed = 5.5

        # Aliens settings
        self.alien_img = 'resources/alien.bmp'
        self.alien_speed = 2.5

        # Bullet settings
        self.bullets_allowed = 6
        self.bullet_speed = 11
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)