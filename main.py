import pygame
import numpy as np

# chess pieces # White , Black

class cs:
    P , p = 1 , 11 # pawn
    R , r = 5 , 50 # rook
    B , b = 4 , 40 # bishop
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
activePlayer = True # true = white


SIZE = 800

# Font
font = pygame.font.SysFont('arial',25)

# Set up the display
screen_size = (SIZE, SIZE)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Chess')

# Define the size of each square
square_size = screen_size[0] // 8

# Array to store piece positions
pieces = np.array([[0]*8]*8) 
copy = np.array([[0]*8]*8)

# Set starting postion for pieces 
def set_start():
        
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

    global whiteKing 
    whiteKing = [7,4]
    global blackKing 
    blackKing = [0,4]

   

# Draw the chessboard
def draw_board():
        
    for row in range(8):
        for col in range(8):
            square_color = WHITE if (row + col) % 2 == 0 else PINK
            pygame.draw.rect(screen, square_color, (col * square_size, row * square_size, square_size, square_size))


# Draw the pieces 
def load_images():

    image_dict = {
    'p': pygame.transform.scale(pygame.image.load('images/' + 'bP' + '.png'), (square_size, square_size)),
    'r': pygame.transform.scale(pygame.image.load('images/' + 'bR' + '.png'), (square_size, square_size)),
    'n': pygame.transform.scale(pygame.image.load('images/' + 'bN' + '.png'), (square_size, square_size)),
    'b': pygame.transform.scale(pygame.image.load('images/' + 'bB' + '.png'), (square_size, square_size)),
    'q': pygame.transform.scale(pygame.image.load('images/' + 'bQ' + '.png'), (square_size, square_size)),
    'k': pygame.transform.scale(pygame.image.load('images/' + 'bK' + '.png'), (square_size, square_size)),
    'P': pygame.transform.scale(pygame.image.load('images/' + 'wP' + '.png'), (square_size, square_size)),
    'R': pygame.transform.scale(pygame.image.load('images/' + 'wR' + '.png'), (square_size, square_size)),
    'N': pygame.transform.scale(pygame.image.load('images/' + 'wN' + '.png'), (square_size, square_size)),
    'B': pygame.transform.scale(pygame.image.load('images/' + 'wB' + '.png'), (square_size, square_size)),
    'Q': pygame.transform.scale(pygame.image.load('images/' + 'wQ' + '.png'), (square_size, square_size)),
    'K': pygame.transform.scale(pygame.image.load('images/' + 'wK' + '.png'), (square_size, square_size)),
}
    return image_dict

def draw_pieces(images):
    
    
    drawDict = {
    cs.p: 'p',
    cs.P: 'P',
    cs.r: 'r',
    cs.R: 'R',
    cs.n: 'n',
    cs.N: 'N',
    cs.b: 'b',
    cs.B: 'B',
    cs.q: 'q',
    cs.Q: 'Q',
    cs.k: 'k',
    cs.K: 'K',
}

    for i in range(8):
            for j in range (8):
                if pieces[i][j] in drawDict.keys():
                    image = images[drawDict[pieces[i][j]]]
                    imageRect = image.get_rect()
                    imageRect.center = ((j+0.5) * square_size , (i+0.5) * square_size)
                    screen.blit(image, imageRect)
    
# Mouse position -> board square
def mouse_square(x):
    j = x[0] // square_size
    i = x[1] // square_size

    return i,j #return x,y; (0,0) is top left corner


# Highlight square 
def highlight(sq):                                  # P1  P2
    x = sq[1] * square_size                         #   X
    y = sq[0] * square_size                         # P4  P3 
    P1=(x + square_size/10 , y + square_size/10)
    P2=(x + 9/10 * square_size , y + square_size/10)
    P3=(x + 9/10 * square_size , y + 9/10 * square_size)   
    P4=(x + square_size/10 , y + 9/10 * square_size)    
    pygame.draw.polygon(screen, (255,0,0), [P1,P2,P3,P4], width=5)   



# Move piece
def move(activeSq):
    global highlightBool
    global activePlayer

    if pieces[activeSq]:
        
        event = pygame.event.wait()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 1:
                takeSquare = mouse_square(event.pos)
                move = activeSq , takeSquare
                if legal(*move, pieces) and not willCheck(*move, pieces):
                    pieces[takeSquare] = pieces[activeSq]
                    pieces[activeSq] = 0
                    
                    activePlayer = not activePlayer
                    highlightBool = False
                    checkmate(activePlayer, pieces)


            if event.button == 3:
                highlightBool = False
    

# Returns colour(string) of piece
def colour(pieceValue):
    if pieceValue in range(1,10):

        return "White"
    elif pieceValue > 10 :

        return "Black"
    elif pieceValue == 0 :

        return "Empty"
    
def canTake(attackValue , defendValue):

    return ( colour(attackValue) == "White" ) and ( colour(defendValue)  == "Black" ) or \
           ( colour(attackValue) == "Black" ) and ( colour(defendValue)  == "White" )

def legal(start , finish, board): # start, finish = pieces(i , j)
    start_value = board[start] 
    finish_value = board[finish]

    same_colour = colour(start_value) == colour(finish_value)   
    
    if same_colour: 
        return False
    
    if start == finish:
        return False

    startX , startY = start[1] , start[0]
    finishX , finishY = finish[1] , finish[0]
    
    

    match(start_value):
    #piece logic    
        
        case cs.p: 
            if (startX == finishX) and (finishY == 3) and (startY == 1): #first move !!
                return (finish_value == 0) and (board[startY+1][finishX] == 0) #can't capture vertically
            
            if (startX == finishX) and (finishY - startY) == 1: # 1 square down vertically
                return finish_value == 0
            
            if ( abs(startX - finishX) == 1 ) and ( (finishY - startY) == 1 ) : #capture
                return canTake(start_value, finish_value)

        case cs.P:
            if (startX == finishX) and (finishY == 4) and (startY == 6): 
                return (finish_value == 0) and (board[startY-1][finishX] == 0)
            
            if (startX == finishX) and (startY - finishY)  == 1: # 1 square up vertically
                return finish_value == 0
            
            if ( abs(startX - finishX) )== 1 and ( (finishY - startY) == -1 ) : #capture
                return canTake(start_value, finish_value)
        
        case cs.n | cs.N:


            return ( abs(startX-finishX) + abs(startY-finishY) ) == 3 and ( abs(startX-finishX) <= 2 ) and \
            ( abs(startY-finishY) <= 2 )
                
        case cs.b | cs.B:
            if abs(startX-finishX) == abs(startY-finishY):

                return blocked(start, finish, board)

        case cs.r | cs.R:
            if startX == finishX or startY == finishY:

                return blocked(start, finish, board)        

        case cs.q | cs.Q:
            if startX == finishX or startY == finishY or ( abs(startX-finishX) == abs(startY-finishY) ):

                return blocked(start, finish, board)

        case cs.k | cs.K: 
            return ( abs(startX-finishX) <= 1 ) and ( abs(startY-finishY) <= 1 )   
            

        
        case _: return False 
    
def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    else:
        return 0

def blocked(start, finish, board):

    startX , startY = start[1] , start[0]
    finishX , finishY = finish[1] , finish[0]

    # 4 possible directions: Ox, Oy, 2 diagonals
    
    dx = sign(finishX -startX)
    dy = sign(finishY - startY)

    while (startX != finishX -dx) or (startY != finishY -dy):

        startX = startX + dx
        startY = startY + dy

        if board[startY][startX]:
            return False
    
    return True

# Check if player to move selected one of their pieces

def turn(selectedValue, whitesMove):
    selectedColour = colour( selectedValue )
    
    if selectedColour == 'Empty':
        return False
    
    whitesTurn = selectedColour == 'White'
    
    if whitesTurn == whitesMove:
        return True
    
    return False
    

def inCheck(whitesTurn, board): 
    seenSquares = set()    
    literalTurn = 'Black' if whitesTurn else 'White'
    #check every possible move for enemy player

    for i in range(8):
        for j in range(8):
        
            if board[i][j] != 0:
          
                for r in range(8):
                    for c in range(8):
                        if ( colour(board[i][j]) == literalTurn ) and legal( (i,j) , (r,c), board):
                            # account for pawns not capturing in front of them
                            if (board[i][j] == cs.p) or (board[i][j] == cs.P):
                                if j != c:
                                    seenSquares.add( (r,c) )
                            else:
                                seenSquares.add( (r,c) )
    
    for square in seenSquares:
        
        if board[square] == cs.K:

            return True
    
        if board[square] == cs.k:

            return True

    return False    


    
#Check if a move will result in own king being in check (not allowed)
def willCheck(start, finish, board ):

    global activePlayer

    copy = np.copy(board)
    copy[finish] = copy[start]
    copy[start] = 0

    if inCheck(activePlayer, copy):

        return True
    else:

        return False

        
def checkmate(whitesTurn, board):
    
    possibleMoves = set()
    stringTurn = 'White' if whitesTurn else 'Black'

    for i in range(8):
        for j in range(8):
            
            if board[i][j] != 0:
            
                for r in range(8):
                    for c in range(8):
                        move = ((i,j), (r,c))

                        if ( colour(board[i][j]) == stringTurn  ) and legal(*move, board) and not willCheck(*move, board):
                            possibleMoves.add(move)
    
    if len(possibleMoves) == 0:
        if inCheck(whitesTurn, board):
            print(stringTurn + ' is checkmated')
            return ('mate')
        else:
            print('stalemate')
            return ('stalemate')
    
    return None


# Main loop
def main():
    global highlightBool
    global activeSquare
    global activePlayer

    set_start()
    
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)

    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])

    images = load_images()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    activeSquare = mouse_square(event.pos)

                    if turn( pieces[activeSquare], activePlayer ) :
                        highlightBool = True
                    else:
                        highlightBool = False
                
                else: highlightBool = False

                    

                
        
        draw_board()

        if highlightBool:
            highlight(activeSquare)  
            move(activeSquare)
        draw_pieces(images)
        

        pygame.display.flip()

if __name__ == "__main__":
    main()

# Quit pygame
pygame.quit()