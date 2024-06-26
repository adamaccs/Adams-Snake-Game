# Import necessary modules.
import pygame
from snakegame import SnakeGame


def main():
    # Initialize Pygame.
    pygame.init()
    pygame.font.init()
    game = SnakeGame()
    

         
if __name__ == '__main__':
    game = SnakeGame()
    
    # Game loop
    while True:
        game_over, score = game.play_step()
    
        # Check if the game is over.
        if game_over:
            break
    
    # Print the final score.
    print("Final score", score)


'''
Directory Structure:

AdvCodProject/
│
├── main.py                    
├── snakegame.py   
├── gamebase.py             
├── utilities.py
├── apple.png
└── snakehead.png              
'''