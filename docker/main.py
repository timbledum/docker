"""Dock'er – the game.
"""
from collections import namedtuple
from itertools import cycle
import pyxel
from random import randint

#############
# Constants #
#############


Point = namedtuple("Point", ["x", "y"])  # Convenience class for coordinates

WIDTH = 256
HEIGHT = 256
STAR_COUNT = 200

DRIFTX = cycle([int(i) for i in "0011111122222222233334444333222222222111110000"])
DRIFTY = cycle([int(i) for i in "443332222222221111100000011111122222222233334"])

###################
# The game itself #
###################


class App:

    def __init__(self):
        """Initiate pyxel, set up initial game variables, and run."""

        pyxel.init(WIDTH, HEIGHT, caption="Dock'er", scale=2, fps=22)
        pyxel.image(1).load(0, 0, 'assets/cockpit.png')
        pyxel.image(0).load(0, 0, 'assets/dock.png')

        self.driftx = self.drifty = 0

        self.stars = []
        for _ in range(STAR_COUNT):
            self.stars.append(Point(randint(0, WIDTH), randint(0, HEIGHT)))

        pyxel.run(self.update, self.draw)

    ##############
    # Game logic #
    ##############

    def update(self):
        """Update logic of game."""
        self.update_drift()
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        
    def update_drift(self):
        self.driftx = next(DRIFTX)
        self.drifty = next(DRIFTY)

    ##############
    # Draw logic #
    ##############

    def draw(self):

        pyxel.cls(col=0)
        for star in self.stars:
            pyxel.pix(star.x, star.y, col=6)

        pyxel.blt(x=self.driftx, y=self.drifty, img=0, sx=0, sy=0, w=WIDTH, h=HEIGHT, colkey=11)

        pyxel.blt(x=0, y=0, img=1, sx=0, sy=0, w=WIDTH, h=HEIGHT, colkey=11)



if __name__ == "__main__":
    App()
