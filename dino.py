import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dinosaur Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Dinosaur settings
DINO_WIDTH = 40
DINO_HEIGHT = 60
dino_x = 50
dino_y = SCREEN_HEIGHT - DINO_HEIGHT - 10
dino_vel_y = 0
is_jumping = False

# Obstacle settings
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 50
obstacle_x = SCREEN_WIDTH
obstacle_y = SCREEN_HEIGHT - OBSTACLE_HEIGHT - 10
obstacle_vel_x = -10

# Game settings
clock = pygame.time.Clock()
running = True
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                dino_vel_y = -15

    # Update dinosaur
    if is_jumping:
        dino_vel_y += 1  # Simulate gravity
        dino_y += dino_vel_y
        if dino_y >= SCREEN_HEIGHT - DINO_HEIGHT - 10:
            dino_y = SCREEN_HEIGHT - DINO_HEIGHT - 10
            is_jumping = False
            dino_vel_y = 0

    # Update obstacle
    obstacle_x += obstacle_vel_x
    if obstacle_x < 0:
        obstacle_x = SCREEN_WIDTH
        score += 1

    # Check for collision
    if (dino_x + DINO_WIDTH > obstacle_x and
        dino_x < obstacle_x + OBSTACLE_WIDTH and
        dino_y + DINO_HEIGHT > obstacle_y):
        running = False

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (dino_x, dino_y, DINO_WIDTH, DINO_HEIGHT))
    pygame.draw.rect(screen, BLACK, (obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
             