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
BLACK = (0, 0, 0)
BROWN = (58, 31 ,4)

SIZE = 800

# Font

font = pygame.font.SysFont('arial',20)


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

def draw_pieces():
    # pygame.draw.rect(screen , BLACK , x )
        for i in range(8):
            for j in range (8):
                match(pieces[i][j]):
                    case 1: #p
                        text = font.render('p', True , BLACK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 10: #P
                        text = font.render('P', True , BLACK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 5: #r
                        text = font.render('r', True , BLACK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 50: #R
                        text = font.render('R', True , BLACK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 3: #n
                        text = font.render('n', True , BLACK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 30: #N
                        text = font.render('N', True , BLACK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 4: #b
                        text = font.render('b', True , BLACK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 40: #B
                        text = font.render('B', True , BLACK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 9: #q
                        text = font.render('q', True , BLACK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 90: #Q
                        text = font.render('Q', True , BLACK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 2: #k
                        text = font.render('k', True , BLACK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case 20: #K
                        text = font.render('K', True , BLACK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)                    
                    case _:
                        pass
                          
                    
                   
               





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
        set_start()
        draw_pieces()
        #draw_pieces(R1) 
        #draw_pieces(R2)
        
        









        pygame.display.flip()


main()

# Quit pygame
pygame.quit()
