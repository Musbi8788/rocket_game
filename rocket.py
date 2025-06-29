import pygame

class Rocket:
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

        # Store the x value for the rocket horizontal position.
        self.x = float(self.rect.x)
        # Store the x value for the rocket vertical position.
        self.y = float(self.rect.y)

        # Movement Flage 
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
    
    def update(self):
        """Update the rocket position base on the movement flag.
        """

        # update the value of x not the rect
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.rocket_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.rocket_speed

        # Update the rect object from self.x
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)


    def blitme(self):
        """Draw the rocket at in current location
        """
        self.screen.blit(self.image, self.rect)