import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        self.snake = [(WIDTH / 2, HEIGHT / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.food = self.generate_food()

        self.score = 0

    def generate_food(self):
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        return x, y

    def draw(self):
        self.screen.fill(BLACK)
        for segment in self.snake:
            pygame.draw.rect(self.screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, RED, (self.food[0], self.food[1], CELL_SIZE, CELL_SIZE))

    def move_snake(self):
        head = (self.snake[0][0] + self.direction[0] * CELL_SIZE, self.snake[0][1] + self.direction[1] * CELL_SIZE)
        if head == self.food:
            self.score += 1
            self.snake.insert(0, head)
            self.food = self.generate_food()
        else:
            self.snake.insert(0, head)
            self.snake.pop()

    def check_collision(self):
        if (self.snake[0][0] < 0 or self.snake[0][0] >= WIDTH or
            self.snake[0][1] < 0 or self.snake[0][1] >= HEIGHT or
            self.snake[0] in self.snake[1:]):
            return True
        return False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != DOWN:
                        self.direction = UP
                    elif event.key == pygame.K_DOWN and self.direction != UP:
                        self.direction = DOWN
                    elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                        self.direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.direction = RIGHT

            self.move_snake()

            if self.check_collision():
                running = False

            self.draw()
            pygame.display.flip()
            self.clock.tick(10)

        print("Game Over! Your score is:", self.score)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()

    pygame.quit()
