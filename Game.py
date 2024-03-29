# Initialise
import random

board = []
# Create board
for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Start game."
print_board(board)

ship_row = random.randint(0, len(board) - 1)
ship_col = random.randint(0, len(board[0]) - 1)

for move in range(5):
    print "Move: " + str(move + 1)
    guess_row = int(input("Guess Row: (0-4)"))
    guess_col = int(input("Guess Col: (0-4)"))

    if (guess_row == ship_row) and (guess_col == ship_col):
        print "You win."
        board[ship_row][ship_col] = "H"
        print_board(board)
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "That's not on the board"
        elif(board[guess_row][guess_col] == "X"):
            print "You have already guessed there."            
        else:
            print "Miss."
            board[guess_row][guess_col] = "X"
            print_board(board)
            if move == 4:
                print "Game Over."
                  board[ship_row][ship_col] = "S"
                  print_board(board)
