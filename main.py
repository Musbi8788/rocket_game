import sys
import pygame
from rocket import Rocket
from settings import Settings

class RocketGame():
    """A class to manage the rocket game
    """
    def __init__(self) -> None:
        """Initialize the game
        """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption(self.settings.game_title)

        self.rocket = Rocket(self)

    def run_game(self):
        """keep the game running.
        """
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        """Response to  keypress
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypress

        Args:
            event (_type_): _description_
        """
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Repsond to key releast

        Args:
            event (_type_): keyboard 
        """
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
            


    def _update_screen(self):
        """Update the screen and display the image.
        """
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        pygame.display.flip()



if __name__ == "__main__":
        """make the rocket instance and run the game
        """
        rg = RocketGame()
        rg.run_game()