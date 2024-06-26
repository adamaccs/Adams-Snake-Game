import pygame
from utilities import BLOCK_SIZE, BLACK, SCORE_AREA

# Define the GameBase class (parent class).
class GameBase:
    def __init__(self, width, height):
        self.width = width
        # Initialize height with score area.
        self.height = height + SCORE_AREA 
        
        #Initialize the display
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.score = 0
        
        #Initialize the default game direction
        self.direction = None
        
    def DrawGrid(self):
        #Set the size of the grid lock
        for x in range(0, self.width, BLOCK_SIZE):
            for y in range(SCORE_AREA, self.height, BLOCK_SIZE):
                
        # Start drawing grid below score area.
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(self.display, BLACK, rect, 1)
                