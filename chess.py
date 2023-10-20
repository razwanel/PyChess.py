import pygame
import numpy as np

# chess pieces # White , Black
P , p = 1 , 10 # pawn
R , r = 5 , 50 # rook
B , b = 4 , 40 # biishop
N , n = 3 , 30 # knight
Q , q = 9 , 90 # queen
K , k = 2 , 20 # king




# Initialize pygame
pygame.init()

# Define parameters
WHITE = (255, 255, 255)
BLACK =(0, 0, 0)
PINK = (199, 21, 133)
BROWN = (58, 31 ,4)


#swap
AUX=PINK
PINK=BROWN
BROWN=AUX

SIZE = 800

# Font
font = pygame.font.SysFont('arial',25)

# Set up the display
screen_size = (SIZE, SIZE)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Chess')

# Define the size of each square
square_size = screen_size[0] // 8

#('a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h') 
FILES = (0 , 1 , 2 , 3 , 4 , 5 , 6 , 7)      # Vertical lines
RANKS = (0 , 1 , 2 , 3 , 4 , 5 , 6 , 7)      # Horizontal lines

# Array to store pieces in each position
pieces = np.array([[0]*8]*8) 

# starting postion for pieces 
def set_start():
        for i in range(8):
            for j in range(8):
                match (i,j):
                    case (1,j):
                        pieces[i][j] = p
                    case (6,j):
                        pieces[i][j] = P
                    case _:
                        pieces[i][j] = 0
        pieces[0][0]= r
        pieces[0][1]= n
        pieces[0][2]= b
        pieces[0][3]= q
        pieces[0][4]= k
        pieces[0][5]= b
        pieces[0][6]= n
        pieces[0][7]= r

        pieces[7][0]= R
        pieces[7][1]= N
        pieces[7][2]= B
        pieces[7][3]= Q
        pieces[7][4]= K
        pieces[7][5]= B
        pieces[7][6]= N
        pieces[7][7]= R

# Draw the chessboard
def draw_board():
        
        for row in RANKS:
            for col in FILES:
                square_color = WHITE if (row + col) % 2 == 0 else BROWN
                pygame.draw.rect(screen, square_color, (col * square_size, row * square_size, square_size, square_size))

# Draw the pieces using 'pieces' array
def draw_pieces():
        for i in range(8):
            for j in range (8):
                match(pieces[i][j]):
                    case 10: #
                        text = font.render('p', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 1: #P
                        text = font.render('P', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 50: #r
                        text = font.render('r', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 5: #R
                        text = font.render('R', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 30: #n
                        text = font.render('n', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 3: #N
                        text = font.render('N', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 40: #b
                        text = font.render('b', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 4: #B
                        text = font.render('B', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 90: #q
                        text = font.render('q', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 9: #Q
                        text = font.render('Q', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 20: #k
                        text = font.render('k', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 2: #K
                        text = font.render('K', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)                    
                    case _:
                        pass

# Check for click


# Main loop
def main():

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        
        
        draw_board()   
        set_start()
        draw_pieces()
        
        
        









        pygame.display.flip()


main()

# Quit pygame
pygame.quit()
