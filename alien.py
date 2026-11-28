import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent an alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""

        super().__init__()

        self.settings = ai_game.settings
        self.screen = ai_game.screen

        self.image = pygame.image.load(self.settings.alien_img)
        self.rect = self.image.get_rect()

        # Start the new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)