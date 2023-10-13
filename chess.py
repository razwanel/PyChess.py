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
pygame.display.set_caption('Chess')

# Define the size of each square
square_size = screen_size[0] // 8

#('a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h') 
FILES = (0 , 1 , 2 , 3 , 4 , 5 , 6 , 7)      # Vertical lines
RANKS = (0 , 1 , 2 , 3 , 4 , 5 , 6 , 7)      # Horizontal lines
 




# Draw the chessboard
def draw_board():
        
        for row in RANKS:
            for col in FILES:
                square_color = WHITE if (row + col) % 2 == 0 else BROWN
                pygame.draw.rect(screen, square_color, (col * square_size, row * square_size, square_size, square_size))

def draw_pieces(R):
    pygame.draw.rect(screen , BLACK , R )
     





# Main loop
def main():

    R1 = pygame.Rect(square_size/10 , square_size*7.1 , 0.8*square_size , 0.8*square_size)
    R2 = pygame.Rect(square_size*7.1 , square_size*7.1 , 0.8*square_size , 0.8*square_size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board()   
        draw_pieces(R1) 
        draw_pieces(R2)
        









        pygame.display.flip()


main()

# Quit pygame
pygame.quit()
