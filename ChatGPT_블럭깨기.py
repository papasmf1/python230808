import pygame
import random

# Define the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the paddle properties
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
PADDLE_COLOR = GREEN

# Define the ball properties
BALL_RADIUS = 10
BALL_COLOR = BLUE
BALL_SPEED = 5

# Define the block properties
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 20
BLOCK_COLORS = [RED, GREEN, BLUE]

pygame.init()

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Breaking Game")

# Create the paddle
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create the ball
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS, SCREEN_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = random.choice([-BALL_SPEED, BALL_SPEED])
ball_speed_y = -BALL_SPEED

# Create the blocks
blocks = []
for row in range(3):
    for col in range(10):
        block = pygame.Rect(col * (BLOCK_WIDTH + 5) + 30, row * (BLOCK_HEIGHT + 5) + 50, BLOCK_WIDTH, BLOCK_HEIGHT)
        blocks.append(block)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= 5
    if keys[pygame.K_RIGHT]:
        paddle.x += 5

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Check collisions with the walls
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # Check collision with the paddle
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y

    # Check collisions with blocks
    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y

    # Check if the ball goes out of the screen
    if ball.bottom >= SCREEN_HEIGHT:
        # Reset the ball
        ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        ball_speed_x = random.choice([-BALL_SPEED, BALL_SPEED])
        ball_speed_y = -BALL_SPEED

    # Clear the screen
    screen.fill(WHITE)

    # Draw the paddle, ball, and blocks
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)
    pygame.draw.circle(screen, BALL_COLOR, ball.center, BALL_RADIUS)
    for block in blocks:
        pygame.draw.rect(screen, random.choice(BLOCK_COLORS), block)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(60)

# Quit the game
pygame.quit()
