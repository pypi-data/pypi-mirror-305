
import pygame
import sys
# Initialize Pygame
pygame.init()
# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Move Rectangle with Arrow Keys")
# Set up rectangle properties
rect_width, rect_height = 50, 50
rect_x, rect_y = width // 2, height // 2
rect_speed = 5
# Colors
black = (0, 0, 0)
white = (255, 255, 255)
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed
    # Ensure the rectangle stays within the window boundaries
    if rect_x < 0:
        rect_x = 0
    if rect_x > width - rect_width:
        rect_x = width - rect_width
    if rect_y < 0:
        rect_y = 0
    if rect_y > height - rect_height:
        rect_y = height - rect_height
    # Fill screen with black
    screen.fill(black)
    # Draw the rectangle
    pygame.draw.rect(screen, white, (rect_x, rect_y, rect_width, rect_height))
    # Update the display
    pygame.display.flip()
    # Control the frame rate
    pygame.time.Clock().tick(60)
   
