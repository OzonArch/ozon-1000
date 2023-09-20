""" In ALien Invasion, the player controls a rocket ship that appears at the bottom center of the screen.
The player player can move the ship right and left using the arrow keys and shoot bullets
using the spacebar.When the game begins, a fleet of aliens fills the sky and moves across and down the screen.
The player shoots and destroys the aliens.If the player shoots all the aliens, a new fleet appears that moves faster than the previous fleet.
If any alien hits the player's ship or reaches the bottom of the screen, the player loses ship. If the player loses three ships, the game ends.

For the first development phase, we'll make a ship that can move right and left and fires bullets
when the player presses the spacebar. After setting up this behavior, we can create the aliens and refine the gameplay."""


# Creating a Pygame Window and Responding to User Input

import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        pygame.init() # Initializes the background setting
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get(): # Access the events
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, run the game.
    ai = AlienInvasion()
    ai.run_game()