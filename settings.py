class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        self.screen_width = 1200
        self.screen_height = 800

        # RGB, 0 to 255 each.
        self.bg_color = (230, 230, 230)

        self.ship_img = 'resources/ship.bmp'
        self.ship_speed = 5