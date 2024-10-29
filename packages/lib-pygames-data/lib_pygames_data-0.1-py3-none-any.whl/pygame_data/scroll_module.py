#image scroll
import pygame
import sys
# Initialize Pygame
pygame.init()
# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
# Load and scale the background image
background = pygame.image.load('game.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Infinite Scrolling Background")
# Variables for background scrolling
y1 = 0
y2 = -HEIGHT  # Second background image positioned above the first one
# Set up the clock
clock = pygame.time.Clock()
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Scroll the background
    y1 += 1
    y2 += 1

    # Reset background positions when they move off screen
    if y1 >= HEIGHT:
        y1 = -HEIGHT
    if y2 >= HEIGHT:
        y2 = -HEIGHT
    # Draw the background images
    screen.blit(background, (0, y1))
    screen.blit(background, (0, y2))
    # Update the display
    pygame.display.flip()
    # Cap the frame rate
    clock.tick(FPS)

