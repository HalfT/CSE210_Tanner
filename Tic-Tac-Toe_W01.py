# Tic-Tac-Toe W01
# Tanner Chadaz

def board_show(board):
    print ()
    print (f"{board[0]} | {board[1]} | {board[2]}")
    print ("- + - + -")
    print (f"{board[3]} | {board[4]} | {board[5]}")
    print ("- + - + -")
    print (f"{board[6]} | {board[7]} | {board[8]}")
    print ()

def next_player(current):
    if current == "O":
        return "X"
    elif current == "X":
        return "O"

def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6]) 

def draw(board):
    for grid in range(9):
        if board[grid] != "X" and board[grid] != "O":
            return False
    return True
    

def move(player, board):
    grid = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[grid -1] = player


def main():
    print("Welcome to Tic-Tac-Toe")
    board = [1,2,3,4,5,6,7,8,9]
    player = "O"    

    while not (winner(board) or draw(board)):
        board_show(board)
        player = next_player(player)
        move(player, board)
    board_show(board)

    print (f"{winner(board)}")
    print("Good game. Thanks for playing!")

main()
