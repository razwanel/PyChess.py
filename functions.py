import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (58, 31 ,4)

SIZE=800

# Set up the display
screen_size = (SIZE, SIZE)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Clickable Chessboard')

# Define the size of each square
square_size = screen_size[0] // 8

# Create a list to keep track of clickable areas
clickable_areas = []

for row in range(8):
    for col in range(8):
        square_rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
        clickable_areas.append(square_rect)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for index, area in enumerate(clickable_areas):
                    if area.collidepoint(event.pos):
                        
                        row = 8 - index // 8 
                        col = chr(index % 8 + 97) 
                        #pygame.draw.circle(screen , BLACK , (row*square_size , (ord(col)-97)*square_size) , 50)
                        print(f"Clicked on square ({col}{row})")
                      #  print(ord(col)-97)
                       # time.sleep(3)

    for row in range(8):
        for col in range(8):
            square_color = BROWN if (row + col) % 2 == 0 else WHITE
            pygame.draw.rect(screen, square_color, (col * square_size, row * square_size, square_size, square_size))

    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
