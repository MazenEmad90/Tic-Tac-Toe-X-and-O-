import random

board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")
    print("\n")

def check_winner(player):
    win_pos = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[i] == player for i in pos) for pos in win_pos)

def user_move():
    while True:
        try:
            move = int(input("Choose your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid or taken. Try again.")
        except:
            print("Enter a number from 1 to 9.")

def computer_move():
    empty = [i for i in range(9) if board[i] == " "]
    if empty:
        move = random.choice(empty)
        board[move] = "O"

def play_game():
    print("Tic-Tac-Toe: You = X, Computer = O")
    print_board()
    
    for _ in range(5):
        user_move()
        print_board()
        if check_winner("X"):
            print("You win!")
            return
        computer_move()
        print_board()
        if check_winner("O"):
            print("Computer wins!")
            return
        if " " not in board:
            break

    print("It's a draw!")

play_game()

