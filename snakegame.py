import pygame
import random
from utilities import Direction, Point, WHITE, BLACK, BLUE, RED, GREEN, YELLOW, BLOCK_SIZE, SPEED, SCORE_AREA, SPEED_INC
from gamebase import GameBase

pygame.font.init()
# Initialize font.
font = pygame.font.SysFont("arial", 25)


#Define class SnakeGame. Subclass and uses inheritance from Gamebase parentclass.
class SnakeGame(GameBase):
    # Initialize width, height, and set default values.
    def __init__(self, width = 640, height = 480):
        super().__init__(width, height)
        
        # Initialize snake starting direction.
        self.direction = None
        
        # Increase height for score display.
        self.height = height + SCORE_AREA
        
        # Initialize the diplay.
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake")
        self.clock.tick(SPEED)
        
        
        
        
        # Snake head starting location (middle).
        self.head = Point(self.width / 2, (self.height - SCORE_AREA) / 2)
        self.snake = [self.head, 
                      # Body (Each point is a cell of the snakes' body).
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)
        ]
            
        
        self.food = None
        
        # '_' Before place to make it a private for this class.
        self._place_food()
        
        # Load and resize the apple image.
        self.apple_img = pygame.image.load("C:/Users/atall/Desktop/AdvCodProject/apple.jpg")
        self.apple_img = pygame.transform.scale(self.apple_img, (BLOCK_SIZE, BLOCK_SIZE))
        
        
        #  Load and resize the snake head image.
        self.snakehead_img = pygame.image.load("C:/Users/atall/Desktop/AdvCodProject/snakehead.png")
        self.snakehead_img = pygame.transform.scale(self.snakehead_img, (BLOCK_SIZE, BLOCK_SIZE))
        
        
        
    # Define the _place_food method. Places an apple in a random location.
    def _place_food(self):
        while True:
            x = random.randint(0, (self.width - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            y = random.randint(SCORE_AREA // BLOCK_SIZE, (self.height - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            self.food = Point(x, y)
            if self.food not in self.snake:
                break
    
    # Define the play_step method.   
    def play_step(self):
        # User button press and function.
        # Prevent going into itself and ending game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and  self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.direction != Direction.UP:
                    self.direction = Direction.DOWN
                    
        
        # Move only if the direction is set.
        if self.direction is not None:
            # Updates the head
            self._move(self.direction) 
            self.snake.insert(0, self.head)

        # Check if game over.
            if self._is_collision():
                return True, self.score

        # Place new apple or just move.
            if self.head == self.food:
                self.score += 1
                if self.score >= 15:
                    self.speed = SPEED + SPEED_INC  
                self._place_food()
            else:
                self.snake.pop()
        
        # Update UI and clock.
        self._update_ui()
        self.clock.tick(SPEED)
        
        # Return game over and score.
        return False, self.score
    
    # Define the _is_collision method, checks if the snake has colided with the borders.
    def _is_collision(self):
        # Hits boundary.
        if self.head.x > self.width - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.height - BLOCK_SIZE or self.head.y < SCORE_AREA:
            return True
        # Hits itself.
        if self.head in self.snake[1:]:
            return True
        return False
        
     # Define the _update_ui method. Updates the ui etc... 
    def _update_ui(self):
        self.display.fill(WHITE)
        self.DrawGrid()
        
        # Determine the orientation of the snake head based on direction.
        if self.direction == Direction.RIGHT:
            snakehead_to_draw = pygame.transform.rotate(self.snakehead_img, 90)
        elif self.direction == Direction.LEFT:
            snakehead_to_draw = pygame.transform.rotate(self.snakehead_img, -90)
        elif self.direction == Direction.UP:
            snakehead_to_draw = pygame.transform.flip(self.snakehead_img, False, True)
        elif self.direction == Direction.DOWN:
            snakehead_to_draw = pygame.transform.flip(self.snakehead_img, True, False)
        else:
            snakehead_to_draw = self.snakehead_img
        
        # Snake body design/color.
        for pt in self.snake[1:]:
            pygame.draw.rect(self.display, GREEN, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, YELLOW, pygame.Rect(pt.x+4, pt.y+4, 12, 12))
            
        # Draw the apple image .
        self.display.blit(self.apple_img, (self.food.x, self.food.y))
        
        # Draw snake head image. 
        self.display.blit(snakehead_to_draw, (self.head.x, self.head.y))
            
        # Display Score.
        text = font.render("Score: " + str(self.score), True, BLACK)
        self.display.blit(text, [0, 0])
        pygame.display.flip()
        
     # Define the move method, move snake in the specified direction.
    def _move(self, direction):
         x = self.head.x
         y = self.head.y
         if direction == Direction.RIGHT:
             x += BLOCK_SIZE
         elif direction == Direction.LEFT:
             x -= BLOCK_SIZE
         elif direction == Direction.DOWN:
             y += BLOCK_SIZE
         elif direction == Direction.UP:
             y -= BLOCK_SIZE

         self.head = Point(x, y)