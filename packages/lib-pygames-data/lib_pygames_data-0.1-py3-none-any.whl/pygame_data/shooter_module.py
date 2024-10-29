import pygame
import random
# Initialize Pygame
pygame.init()
# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ENEMY_COLOR = (255, 0, 0)
PLAYER_COLOR = (0, 255, 0)
BULLET_COLOR = (255, 255, 255)
# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
# Game variables
player_pos = [WIDTH // 2, HEIGHT - 50]
enemies = []
bullets = []
score = 0
level = 1
enemy_count = 10
game_over = False
enemy_speed = 1
def spawn_enemies(count):
    for _ in range(count):
        enemies.append([random.randint(0, WIDTH - 50), random.randint(0, 150)])
# Initial enemy spawn
spawn_enemies(enemy_count)
# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= 5
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - 50:
            player_pos[0] += 5
        if keys[pygame.K_SPACE]:
            bullets.append([player_pos[0] + 20, player_pos[1]])
        # Update bullet positions
        bullets = [[b[0], b[1] - 10] for b in bullets if b[1] > 0]
        # Update enemy positions
        for enemy in enemies:
            enemy[1] += enemy_speed
        # Draw player
        pygame.draw.rect(screen, PLAYER_COLOR, (player_pos[0], player_pos[1], 50, 30))
        # Draw enemies
        for enemy in enemies:
            pygame.draw.rect(screen, ENEMY_COLOR, (enemy[0], enemy[1], 50, 30))
        # Draw bullets
        for bullet in bullets:
            pygame.draw.rect(screen, BULLET_COLOR, (bullet[0], bullet[1], 5, 10))
        # Check for collisions
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet[0] in range(enemy[0], enemy[0] + 50) and bullet[1] in range(enemy[1], enemy[1] + 30):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    break
        # Check if all enemies are defeated
        if not enemies:
            level += 1
            enemy_count += 5  # Increase enemy count for next level
            spawn_enemies(enemy_count)
        # Check game over condition
        for enemy in enemies:
            if enemy[1] + 30 >= player_pos[1]:
                game_over = True
                break
    else:
        # Game over screen
        font = pygame.font.SysFont('Arial', 40)
        text = font.render(f"Game Over! Score: {score}", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
