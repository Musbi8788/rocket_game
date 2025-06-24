import sys
import pygame

class Rocket():
    """A class to manage the rocket game
    """
    def __init__(self) -> None:
        """Initialize the game
        """
        pygame.init()

        self.screen = pygame.display.set_mode((320, 320))
        pygame.display.set_caption("Rocket Game")

        self.bg_color = (196, 206, 211)

    def run_game(self):
        """keep the game running.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self._update_screen()


    def _update_screen(self):
        """Update the screen and display the image.
        """
        self.screen.fill(self.bg_color)
        pygame.display.flip()



if __name__ == "__main__":
        """make the rocket instance and run the game
        """
        rg = Rocket()
        rg.run_game()