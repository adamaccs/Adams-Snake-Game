from enum import Enum
from collections import namedtuple

# Define the Direction enum for snake movement.
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

# Define a named tuple for points on the grid.
Point = namedtuple("Point", "x, y")

# Define RGB colors. 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (231, 27, 63, 255)
GREEN = (160, 196, 50, 255)
YELLOW = (255, 234, 0)

# Define game constants.
BLOCK_SIZE = 20
SPEED = 15

# Height reserved for the score display
SCORE_AREA = 40
SPEED_INC = 10