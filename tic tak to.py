
board=[".",".",".",".",".",".",".",".","."]
count=0
boardChecker=[a for a in board if "X" in a]
 

game=True
def game_board ():
    global board
    print(board[0],"   |   ",board[1],"   |   ",board[2])
    print("     ++        ++"   )
    print(board[3],"   |   ",board[4],"   |   ",board[5])
    print("     ++        ++"   )
    print(board[6],"   |   ",board[7],"   |   ",board[8])


def game_play ():
    global board, user_input, turn,count
    
    
    try:
        user_input=(input("where you want to play:"))
        if   board[int(user_input)-1]=="." :
            board[int(user_input)-1]= turn
        else:
            print("that is not avalable")
            count -= 1
            if turn =="X":
                turn="O"
            else:
                turn="X"
    except:
        print("some thing run roung,try again with 1-10")
        count -=1
        if turn =="X":
            turn="O"
        else:
            turn="X"
        
        

   
    

turn="X"
    

while count < 9:
   
    game_board()
    game_play()
    

    if board[0]=="X" and board[1]== "X" and board[2]=="X" or board[3]=="X" and board[4]== "X" and board[5]=="X" or board[6]=="X" and board[7]== "X" and board[8]=="X" or board[1]=="X" and board[4]== "X" and board[7]=="X" or board[2]=="X" and board[5]== "X" and board[8]=="X" or board[0]=="X" and board[3]== "X" and board[6]=="X"or board[2]=="X" and board[4]== "X" and board[6]=="X" or board[0]=="X" and board[4]== "X" and board[8]=="X" :
        game_board()
        print(turn," won")
        break
    elif  board[0]=="O" and board[1]== "O" and board[2]=="O" or board[3]=="O" and board[4]== "O" and board[5]=="O" or board[6]=="O" and board[7]== "O" and board[8]=="O" or board[1]=="O" and board[4]== "O" and board[7]=="O" or board[2]=="O" and board[5]== "O" and board[8]=="O" or board[0]=="O" and board[3]== "O" and board[6]=="O"or board[2]=="O" and board[4]== "O" and board[6]=="O" or board[0]=="O" and board[4]== "O" and board[8]=="O" :
        game_board()
        print(turn ," won")
        break
    else:
        count += 1
    
    if turn =="X":
        turn="O"
    else:
        turn="X"
       
if count == 9:
    print("its a tie")