#!/usr/bin/env python3
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PACMAN_SIZE = 30

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pac-Man')

# Pac-Man properties
pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
pacman_speed = 5

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Boundaries check
    if pacman_x < 0:
        pacman_x = 0
    elif pacman_x > WIDTH - PACMAN_SIZE:
        pacman_x = WIDTH - PACMAN_SIZE
    if pacman_y < 0:
        pacman_y = 0
    elif pacman_y > HEIGHT - PACMAN_SIZE:
        pacman_y = HEIGHT - PACMAN_SIZE

    # Draw Pac-Man
    pygame.draw.circle(screen, YELLOW, (pacman_x + PACMAN_SIZE // 2, pacman_y + PACMAN_SIZE // 2), PACMAN_SIZE // 2)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

