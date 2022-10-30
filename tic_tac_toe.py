import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'

def check_rows(s):
    
        if (board[0][0]==s and board[0][1]==s and board[0][2]==s)or(board[1][0]==s and board[1][1]==s and board[1][2]==s)or(board[2][0]==s and board[2][1]==s and board[2][2]==s):
            return True
            
def check_columns(s):
    
        if (board[0][0]==s and board[1][0]==s and board[2][0]==s)or(board[0][1]==s and board[1][1]==s and board[2][1]==s)or(board[0][2]==s and board[1][2]==s and board[2][2]==s):
            return True
            
def check_diagonals(s):
    
        if (board[0][0]==s and board[1][1]==s and board[2][2]==s) or (board[0][2]==s and board[1][1]==s and board[2][0]==s):
            return True
def won(sym):
    return check_rows(sym) or check_columns(sym) or check_diagonals(sym)
def place(symbol):
    print(numpy.matrix(board))
    while(1):
        rows=int(input("Enter a row -1 or 2 or 3:"))
        cols=int(input("Enter a column-1 or 2 or 3:"))
        if((rows>0)and(rows<4)and(cols>0)and(cols<4)and(board[rows-1][cols-1]=='-')):
            break
        else:
            print("invalid input, please enter a correct input")
    board[rows-1][cols-1]=symbol 
def play():
    for turn in range(9):
        if(turn%2==0):
            print("player1 it it is your turn and your symbol is 'X':")
            place(p1s)
            if won(p1s):
                print(p1s,"player1, won the game!")
                print(numpy.matrix(board))
                break
        else:
             print("player2 it it is your turn and your symbol is 'O':")
             place(p2s)
             if won(p2s):
                print(p2s,"player2, won the game!")
                print(numpy.matrix(board))
                break
    if not(won(p1s)) and not(won(p2s)):
        print("Draw")

play()


