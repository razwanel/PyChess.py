import pygame
import numpy as np
import time

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
move_counter = 0 #counter for number of moves

SIZE = 800
PANEL_WIDTH = 400

# Font
font = pygame.font.SysFont('arial',25)

# Set up the display
screen_size = (SIZE + PANEL_WIDTH, SIZE)
screen = pygame.display.set_mode(screen_size)
screen.fill(WHITE)
pygame.display.set_caption('Chess')

# clocks
clock_font = pygame.font.SysFont('arial', 36)

clock_surface_white = pygame.Surface((200, 100))
clock_surface_black = pygame.Surface((200, 100))

#panel for captured pieces
white_captured_pieces_surface = pygame.Surface((240, 240))
black_captured_pieces_surface = pygame.Surface((240, 240))
contor_pozitii_ocupate_alb = 0
contor_pozitii_ocupate_negru = 0

#grid dimensions for captured pieces surface
sq_size = 240 // 4

#lists for captured pieces
white_captured = []
black_captured = []

# var. for clock
start_time_white = None
start_time_black = None

white_time_played = 0
black_time_played = 0

running_w_clock = False
running_b_clock = False

# Define the size of each square
square_size = SIZE // 8

#('a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h') 
FILES = (0 , 1 , 2 , 3 , 4 , 5 , 6 , 7)      # Vertical lines
RANKS = (0 , 1 , 2 , 3 , 4 , 5 , 6 , 7)      # Horizontal lines

# Array to store piece positions
pieces = np.array([[0]*8]*8) 
copy = np.array([[0]*8]*8)

#array for positions in grid (of captured pieces surface)
grid_white = np.array([[0]*4]*4)
grid_black = np.array([[0]*4]*4)
nr_of_sq = 0
for i in range(4):
    for j in range(4):
            grid_white[i][j] = nr_of_sq
            grid_black[i][j] = nr_of_sq
            nr_of_sq += 1    

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
        
    for row in RANKS:
        for col in FILES:
            square_color = WHITE if (row + col) % 2 == 0 else PINK
            pygame.draw.rect(screen, square_color, (col * square_size, row * square_size, square_size, square_size))


# Draw the pieces 
            
image_dict = {}

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

    return i,j #returneaza x,y; (0,0) e coltul din stanga sus


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
    global move_counter
    #inCheck(activePlayer, pieces)
    #checkmate(activePlayer, pieces)
    #mate(activePlayer, pieces)
    if pieces[activeSq]:
        
        event = pygame.event.wait()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 1:
                takeSquare = mouse_square(event.pos)
                move = activeSq , takeSquare
                if legal(*move, pieces) and not willCheck(*move):
                    #check if piece is captured
                    captured = is_captured(activeSq, takeSquare, pieces)

                    pieces[takeSquare] = pieces[activeSq]
                    pieces[activeSq] = 0

                    check_promotion(takeSquare, pieces) #verific daca se poate face promotie

                    #updating the counter
                    if captured or pieces[takeSquare] in [cs.P, cs.p]:
                        move_counter = 0 #resets if pawn moved or piece captured
                    else:
                        move_counter += 1 #increments counter

                    activePlayer = not activePlayer
                    highlightBool = False
                    checkmate(activePlayer, pieces)


            if event.button == 3:
                highlightBool = False
    


def colour(pieceValue):
    if pieceValue in range(1,10):
        #print("colour: White")
        return "White"
    elif pieceValue > 10 :
        #print("colour: Black")
        return "Black"
    elif pieceValue == 0 :
        #print("colour: Empty")
        return "Empty"
    
def canTake(attackValue , defendValue):
    # print("canTake:")
    # print(( colour(attackValue) == "White" ) and ( colour(defendValue)  == "Black" ) or \
    #        ( colour(attackValue) == "Black" ) and ( colour(defendValue)  == "White" ))
    
    return ( colour(attackValue) == "White" ) and ( colour(defendValue)  == "Black" ) or \
           ( colour(attackValue) == "Black" ) and ( colour(defendValue)  == "White" )

def legal(start , finish, board): # start, finish = pieces (i , j)
    #start, finish = board(y, x)
    #print(f"start: {start}")
    #print(f"finish: {finish}")
    start_value = board[start] 
    finish_value = board[finish]
    #print(f"Start value:{start_value}")
    #print(f"Finish value:{finish_value}")
    
    same_colour = colour(start_value) == colour(finish_value)   
    
    if same_colour: 
        return False
    
    if start == finish:
        return False

    startX , startY = start[1] , start[0]
    finishX , finishY = finish[1] , finish[0]
    
    

    match(start_value):
    #implementeaza cazuri pt piese    
        
        case cs.p: 
            if (startX == finishX) and (finishY == 3) and (startY == 1): #first move !!poate sari piese
                return finish_value == 0 #nu poate captura vertical
            
            if (startX == finishX) and (finishY - startY) == 1: # 1 square down vertically
                return finish_value == 0
            
            if ( abs(startX - finishX) == 1 ) and ( (finishY - startY) == 1 ) : #capture
                return canTake(start_value, finish_value)

        case cs.P:
            if (startX == finishX) and (finishY == 4) and (startY == 6): 
                return finish_value == 0
            
            if (startX == finishX) and (startY - finishY)  == 1: # 1 square up vertically
                return finish_value == 0
            
            if ( abs(startX - finishX) )== 1 and ( (finishY - startY) == -1 ) : #capture
                return canTake(start_value, finish_value)
        
        case cs.n | cs.N:


            return ( abs(startX-finishX) + abs(startY-finishY) ) == 3 and ( abs(startX-finishX) <= 2 ) and \
            ( abs(startY-finishY) <= 2 )
                
        case cs.b | cs.B:
            if abs(startX-finishX) == abs(startY-finishY):
                #momentan poate sari peste piese
                return blocked(start, finish, board)
                pass

        case cs.r | cs.R:
            if startX == finishX or startY == finishY:
                #momentan poate sari peste piese
                return blocked(start, finish, board)        
                pass

        case cs.q | cs.Q:
            if startX == finishX or startY == finishY or ( abs(startX-finishX) == abs(startY-finishY) ):
                #momentan poate sari peste piese
                return blocked(start, finish, board)
                pass

        case cs.k | cs.K: #done
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

    # am 4 directii pe care pot sa avansez: Ox, Oy, si 2 bisectoare
    
    dx = sign(finishX -startX)
    dy = sign(finishY - startY)
    #print(f"dx: {dx}")
    #print(f"dy: {dy}")

    # e suficient sa verific pana la finish -1

    while (startX != finishX -dx) or (startY != finishY -dy):

        startX = startX + dx
        startY = startY + dy
        #print(pieces[startY][startX])

        if board[startY][startX]:
            return False
    
    return True

# Verifica daca piesa selectata este a jucatorului care trebuie sa mute:

def turn(selectedValue, whitesMove):
    selectedColour = colour( selectedValue )
    
    if selectedColour == 'Empty':
        return False
    
    whitesTurn = selectedColour == 'White'
    #blacksTurn = colour( selectedValue ) == 'Black'
    
    

    if whitesTurn == whitesMove:
        
       # activePlayer = not activePlayer
        return True
    
    
    return False
    

def inCheck(whitesTurn, board): 
    seenSquares = set()    
    literalTurn = 'Black' if whitesTurn else 'White'
    #print(f'{whitesTurn} , {literalTurn}')
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
                                    #print(f'{(j,i)} sees {(c,r)}')
                            else:
                                seenSquares.add( (r,c) )
                                #print(f'{(j,i)} sees {(c,r)}')
    
    #print(sorted(seenSquares))
    for square in seenSquares:
        
        if board[square] == cs.K:
            #print(f'White in check from {square}')
            return True
    
        if board[square] == cs.k:
            #print(f'Black in check from {square}')
            return True

    return False    


    

def willCheck(start, finish):
    global copy
    global pieces
    global activePlayer

    copy = np.copy(pieces)
    copy[finish] = copy[start]
    copy[start] = 0

    #probabil pot sa iau direct activePlayer
    player = True if (copy[finish] < 10) else False

    if inCheck(activePlayer, copy):
        #print('willcheck True')
        return True
    else:
        #print('willCheck False')
        return False

    #TODO: stalemate checkmate, castling, 50 move rule
        
def checkmate(whitesTurn, board):
    aux = whitesTurn
    
    possibleMoves = set()
    stringTurn = 'White' if whitesTurn else 'Black'

    for i in range(8):
        for j in range(8):
            
            if board[i][j] != 0:
            
                for r in range(8):
                    for c in range(8):
                        move = ((i,j), (r,c))

                        if ( colour(board[i][j]) == stringTurn  ) and legal(*move, board) and not willCheck(*move):
                            possibleMoves.add(move)
    
    if len(possibleMoves) == 0:
        if inCheck(whitesTurn, board):
            print(stringTurn + ' is checkmated')
            return ('mate')
        else:
            print('stalemate')
            return ('stalemate')
    
    return None

def findKing(side, board):
    # side = True for white / False for black
    king = cs.K if side else cs.k
    for i in range(8):
        for j in range(8):

            if board[i][j] == king:
                
                return i,j
            #(row, col) for king


def Check(whitesTurn, board): 

    kingPos = findKing(whitesTurn, board)
    
    for i in range(8):
        for j in range(8):

            if legal( (i,j) , kingPos , board ):
                return True
    return False


def futureCheck(whiteToMove, start, finish):
    global pieces
    global copy

    copy = np.copy(pieces)
    copy[finish] = copy[start]
    copy[start] = 0

    print(copy)
    
    if Check(whiteToMove, copy):
        #print('willcheck True')
        return True
    else:
        #print('willCheck False')
        return False

def mate(whitesTurn, board):
    
    possibleMoves = set()
    stringTurn = 'White' if whitesTurn else 'Black'

    for i in range(8):
        for j in range(8):
            
            if board[i][j] != 0:
            
                for r in range(8):
                    for c in range(8):
                        move = ((i,j), (r,c))

                        if legal(*move, board) and not futureCheck(whitesTurn, *move):
                            possibleMoves.add(move)
    
    if len(possibleMoves) == 0:
        if Check(whitesTurn, board):
            print(stringTurn + ' is checkmated')
            return ('mate')
        else:
            print(stringTurn + ': stalemate')
            return ('stalemate')
    
    return None

#check for pawn promotion:
def check_promotion(takeSquare, board): # takeSquare - (i , j) 
    
    position = takeSquare[0] 
    print('checking for promotion')

    #verific daca e pion alb + daca pozitia pionului este in rank
    if board[takeSquare] == 11 and position == 7: #nu functioneaza cu cs.p, asa ca am pus valorile date in clasa, 1 si 11
        print('promoting pawn to black queen')
        board[takeSquare] = cs.q 

    elif board[takeSquare] == 1 and position == 0:
            print('promoting pawn to white queen')
            board[takeSquare] = cs.Q


def is_captured(start_position, end_position, board):
    global activePlayer 
    global contor_pozitii_ocupate_alb, contor_pozitii_ocupate_negru
    global black_captured, white_captured

    start_piece = board[start_position[0]][start_position[1]] 
    print('start_piece')
    print(start_piece)
    end_piece = board[end_position[0]][end_position[1]]
    print('end_piece')
    print(end_piece)
    if end_piece!=0 : #empty square is represented by 0
        if (start_piece > 10 and end_piece in range(1, 10)): #verific ca piesele sunt de culori diferite
            white_captured.append(end_piece)
            print(white_captured)
            contor_pozitii_ocupate_alb += 1
            return True #captured
        
        elif (end_piece > 10 and start_piece in range(1, 10)):
            black_captured.append(end_piece)
            print(black_captured)
            contor_pozitii_ocupate_negru += 1
            return True

    return False #not captured

#displaying clock + additional info
def draw_panel():
    global white_time_played, black_time_played

  #convert seconds to string in format 00:00:00
    w_time_format = time.strftime('%H:%M:%S', time.gmtime(white_time_played))
    b_time_format = time.strftime('%H:%M:%S', time.gmtime(black_time_played))

#clocks:
    #updating the clock display:
        # render + blit + center

        # white player:
    clock_surface_white.fill(WHITE)
    text_clock_w = clock_font.render(w_time_format, True, BLACK) #clock for person that plays with white pieces
    text_clock_rect = text_clock_w.get_rect(center=clock_surface_white.get_rect().center)
    clock_surface_white.fill(WHITE)
    clock_surface_white.blit(text_clock_w, text_clock_rect)

        # black player
    clock_surface_black.fill(WHITE)
    text_clock_b = clock_font.render(b_time_format, True, BLACK) #clock for person that plays with white pieces
    text_clock_rect = text_clock_b.get_rect(center=clock_surface_black.get_rect().center)
    clock_surface_black.fill(WHITE)
    clock_surface_black.blit(text_clock_b, text_clock_rect)

    # render the clock onto display

        #white player:
    white_position_x = 900
    white_position_y = 680
    screen.blit(clock_surface_white, (white_position_x, white_position_y))

        #black player:
    black_position_x = 900
    black_position_y = 25
    screen.blit(clock_surface_black, (black_position_x, black_position_y))

#captured pieces:
    #panel:  
    white_captured_pieces_surface.fill(WHITE)
    black_captured_pieces_surface.fill(WHITE)

    
    image11= pygame.transform.scale(pygame.image.load('images/' + 'bP' + '.png'), (sq_size, sq_size))
    image50= pygame.transform.scale(pygame.image.load('images/' + 'bR' + '.png'), (sq_size, sq_size))
    image30= pygame.transform.scale(pygame.image.load('images/' + 'bN' + '.png'), (sq_size, sq_size))
    image40= pygame.transform.scale(pygame.image.load('images/' + 'bB' + '.png'), (sq_size, sq_size))
    image90= pygame.transform.scale(pygame.image.load('images/' + 'bQ' + '.png'), (sq_size, sq_size))
    image20= pygame.transform.scale(pygame.image.load('images/' + 'bK' + '.png'), (sq_size, sq_size))
    image1= pygame.transform.scale(pygame.image.load('images/' + 'wP' + '.png'), (sq_size, sq_size))
    image5= pygame.transform.scale(pygame.image.load('images/' + 'wR' + '.png'), (sq_size, sq_size))
    image3= pygame.transform.scale(pygame.image.load('images/' + 'wN' + '.png'), (sq_size, sq_size))
    image4= pygame.transform.scale(pygame.image.load('images/' + 'wB' + '.png'), (sq_size, sq_size))
    image9= pygame.transform.scale(pygame.image.load('images/' + 'wQ' + '.png'), (sq_size, sq_size))
    image2= pygame.transform.scale(pygame.image.load('images/' + 'wK' + '.png'), (sq_size, sq_size))
 

    #blit to screen

    contor_pozitii_ocupate_alb = len(white_captured)  # lungimea listei da numarul de piese capturate
    contor_pozitii_ocupate_negru = len(black_captured)

    for index in range(contor_pozitii_ocupate_alb):
        i = index // 4 #get grid condition
        j = index % 4 
        value = white_captured[index]
        match value:
            case 1:
                image_white = image1
            case 5:
                image_white = image5
            case 4:
                image_white = image4
            case 3:
                image_white = image3
            case 2:
                image_white = image2
            case 9:
                image_white = image9
        
        image_white_rect = image_white.get_rect()   
        image_white_rect.center = ((j + 0.5) * sq_size, (i + 0.5) * sq_size)
        white_captured_pieces_surface.blit(image_white, image_white_rect)

    for index in range(contor_pozitii_ocupate_negru):
        i = index // 4 #get grid position
        j = index % 4  
        value = black_captured[index]
        match value:
            case 11:
                image_black = image11
            case 50:
                image_black = image50
            case 40:
                image_black = image40
            case 30:
                image_black = image30
            case 90:
                image_black = image90
            case 20:
                image_black = image20

        image_black_rect = image_black.get_rect()
        image_black_rect.center = ((j + 0.5) * sq_size, (i + 0.5) * sq_size)
        black_captured_pieces_surface.blit(image_black, image_black_rect)


    white_captured_position_x = 855
    white_captured_position_y = 400
    screen.blit(white_captured_pieces_surface, (white_captured_position_x, white_captured_position_y))

    black_captured_position_x = 855
    black_captured_position_y = 150
    screen.blit(black_captured_pieces_surface, (black_captured_position_x, black_captured_position_y))

def clocks_update():
    global start_time_black, start_time_white
    global running_b_clock, running_w_clock
    global white_time_played, black_time_played

    current_time = time.time()

    if running_w_clock:
        if start_time_white != None:
            elapsed_time = current_time - start_time_white
            white_time_played += elapsed_time
        start_time_white = current_time
    else:
        start_time_white = None

    if running_b_clock:
        if start_time_black != None:
            elapsed_time = current_time - start_time_black
            black_time_played += elapsed_time
        start_time_black = current_time
    else:
        start_time_black = None






# Main loop
def main():
    global highlightBool
    global activeSquare
    global activePlayer
    global move_counter
    global start_time_black, start_time_white
    global running_b_clock, running_w_clock
    clock = pygame.time.Clock()
    FPS = 30
    set_start()
    
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)

    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])

    images = load_images()
    
    running_w_clock = True #white starts
    running_b_clock = False
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #print(" ")
                    activeSquare = mouse_square(event.pos)
                    #print(turn( pieces[activeSquare], activePlayer ))
                    if turn( pieces[activeSquare], activePlayer ) :
                        highlightBool = True
                        
                        if highlightBool: 
                            if activePlayer: #true = white
                                running_b_clock = False
                                running_w_clock = True
                            else:
                                running_w_clock = False
                                running_b_clock = True
                    else:
                        highlightBool = False
                
                else: highlightBool = False

                    

                
        
        draw_board()
        #checkmate(activePlayer, pieces) 
        if highlightBool:
            highlight(activeSquare)  
            move(activeSquare)
        draw_pieces(images)
        
        clocks_update()

        draw_panel()

        #timer stops + game stops at 50 moves - 50 per player
        if move_counter == 100:
            running = False
            print("Draw (50-move rule)")


        pygame.display.flip()
        #clock.tick(FPS)

if __name__ == "__main__":
    main()

# Quit pygame
pygame.quit()