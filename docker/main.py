"""Dock'er – the game.
"""

import pyxel

#############
# Constants #
#############

WIDTH = 256
HEIGHT = 256

###################
# The game itself #
###################


class App:

    def __init__(self):
        """Initiate pyxel, set up initial game variables, and run."""

        pyxel.init(WIDTH, HEIGHT, caption="Dock'er", scale=1, fps=22)

    ##############
    # Game logic #
    ##############

    def update(self):
        """Update logic of game."""



    ##############
    # Draw logic #
    ##############

    def draw(self):
        """Draw the stuff."""



if __name__ == "__main__":
    App()
