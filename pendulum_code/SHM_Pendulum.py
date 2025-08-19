import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
length = 150  # Length of the pendulum
origin = (400, 100)  # Origin point of the pendulum
bob_radius = 20  # Radius of the pendulum bob

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pendulum Animation")

# Function to calculate the position of the pendulum bob
def calculate_bob_position(angle):
    x = origin[0] + length * math.sin(angle)
    y = origin[1] + length * math.cos(angle)
    return int(x), int(y)

# Main loop
clock = pygame.time.Clock()
angle = math.pi / 4  # Initial angle
angle_velocity = 0.1  # Angular velocity
running = True

while running:
    screen.fill(WHITE)
    
    # Draw the pendulum arm
    pygame.draw.line(screen, BLACK, origin, calculate_bob_position(angle), 5)
    
    # Draw the pendulum bob
    pygame.draw.circle(screen, RED, calculate_bob_position(angle), bob_radius)
    
    # Update angle for next frame
    angle += angle_velocity
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
