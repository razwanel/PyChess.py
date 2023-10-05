import pygame

# Initialize pygame
pygame.init()

# Define parameters
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (58, 31 ,4)

SIZE = 800

# Set up the display
screen_size = (SIZE, SIZE)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Chessboard')

# Define the size of each square
square_size = screen_size[0] // 8

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the chessboard
    for row in range(8):
        for col in range(8):
            square_color = BROWN if (row + col) % 2 == 0 else WHITE
            pygame.draw.rect(screen, square_color, (col * square_size, row * square_size, square_size, square_size))










    pygame.display.flip()

# Quit pygame
pygame.quit()
