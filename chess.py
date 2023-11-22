import pygame
import numpy as np
# from .header import *

# chess pieces # White , Black

class cs:
    P , p = 1 , 11 # pawn
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

highlightBool = False
activeSquare = 0


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

# Array to store piece positions
pieces = np.array([[0]*8]*8) 

# Set starting postion for pieces 
def set_start():
        '''
            for i in range(8):
            for j in range(8):
                match (i,j):
                    case (1,j):
                        pieces[i][j] = cs.p
                    case (6,j):
                        pieces[i][j] = cs.P
                    case _:
                        pieces[i][j] = 0
        pieces[0][0]= cs.r
        pieces[0][1]= cs.n
        pieces[0][2]= cs.b
        pieces[0][3]= cs.q
        pieces[0][4]= cs.k
        pieces[0][5]= cs.b
        pieces[0][6]= cs.n
        pieces[0][7]= cs.r

        pieces[7][0]= cs.R
        pieces[7][1]= cs.N
        pieces[7][2]= cs.B
        pieces[7][3]= cs.Q
        pieces[7][4]= cs.K
        pieces[7][5]= cs.B
        pieces[7][6]= cs.N
        pieces[7][7]= cs.R
'''
pieces = [[cs.r, cs.n, cs.b, cs.q, cs.k, cs.b, cs.n, cs.r],
    [cs.p, cs.p, cs.p, cs.p, cs.p, cs.p, cs.p, cs.p],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [cs.P, cs.P, cs.P, cs.P, cs.P, cs.P, cs.P, cs.P],
    [cs.R, cs.N, cs.B, cs.Q, cs.K, cs.B, cs.N, cs.R]]    

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
                    case cs.p: #p
                        text = font.render('p', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case cs.P: #P
                        text = font.render('P', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case cs.r: #r
                        text = font.render('r', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case cs.R: #R
                        text = font.render('R', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case cs.n: #n
                        text = font.render('n', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case cs.N: #N
                        text = font.render('N', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case cs.b: #b
                        text = font.render('b', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case cs.B: #B
                        text = font.render('B', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case cs.q: #q
                        text = font.render('q', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case cs.Q: #Q
                        text = font.render('Q', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case cs.k: #k
                        text = font.render('k', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)
                    case cs.K: #K
                        text = font.render('K', True , PINK)
                        textRect = text.get_rect()
                        textRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                        screen.blit(text, textRect)                    
                    case _:
                        pass
    
    
# Mouse position -> board square
def mouse_square(x):
    j = x[0] // square_size
    i = x[1] // square_size

    return i,j

"""
# Check piece colour (White = 1 ; Black = 2 ; empty = 0)
def isWhite(pos):
    global pieces
    j, i = pos
    if i<8 and j<8 and i>=0 and j>=0:
        #print(f'isWhite: {pieces[i][j]<10}\n')
        print(pos)
        print(pieces[i][j])
        if 0 < pieces[i][j] < 10:
            return 1
        if pieces[i][j] >= 10:
            return 2
        if pieces[i][j] == 0: 
            return 0

        

    else: print('isWhite_error: position not whithin board bounds')
"""

# Highlight square 
def highlight(sq):                                  # P1  P2
    x = sq[1] * square_size                         #   X
    y = sq[0] * square_size                         # P4  P3 
    P1=(x + square_size/10 , y + square_size/10)
    P2=(x + 9/10 * square_size , y + square_size/10)
    P3=(x + 9/10 * square_size , y + 9/10 * square_size)   
    P4=(x + square_size/10 , y + 9/10 * square_size)    
    pygame.draw.polygon(screen, (255,0,0), [P1,P2,P3,P4], width=5)   
    #print('debug' + str(P3))                     
                                    
# Move piece
def move(activeSq):
    global highlightBool

    if pieces[activeSq]:
        
        event = pygame.event.wait()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 1:
                takeSquare = mouse_square(event.pos)
                pieces[takeSquare] = pieces[activeSq]
                pieces[activeSq] = 0
                highlightBool = False

            if event.button == 3:
                highlightBool = False

def legal(start , finish): # start, finish = squares (j, i)

    start_value = pieces[start[1]][start[0]] 
    finish_value = pieces[finish[1]][finish[0]]

    same_colour = start_value <10 == finish_value <10    
    
    if same_colour:
        return False

    match(start_value):
        
        
        
        case _: pass 
    


    

    


            


# Main loop
def main():
    global highlightBool
    global activeSquare

    set_start()
    running = True

    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    activeSquare = mouse_square(event.pos)
                    if pieces[activeSquare]:
                        highlightBool = True
                else: highlightBool = False

                    

                
        
        draw_board() 
        if highlightBool:
            highlight(activeSquare)  
            move(activeSquare)
        draw_pieces()
        
        pygame.display.flip()

main()

# Quit pygame
pygame.quit()

#ai facut functie de verificat culoarea, implementeaza in move() sa verifice
#daca piesa pe care o ia este de alta culoare
#adik pe scurt mai bn te apuci sa faci o functie legalMove() 
#bafta


#nu merge coaie isWhite()... vezi cf