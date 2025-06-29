import pygame

class Rocket():
    """A class to manage the rocket.
    """

    def __init__(self, rocket_game):
        """Initialize the rocket and set it's position 
        """

        self.screen = rocket_game.screen
        self.settings = rocket_game.settings
        self.screen_rect = rocket_game.screen.get_rect()

        # Load the image and get it's rect
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        # Start the rocket at the center on the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the rocket at in current location
        """
        self.screen.blit(self.image, self.rect)