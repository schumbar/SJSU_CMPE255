import random

# Initialize the game board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Function to display the game board
def display_board():
    print("   0  1  2")
    for i in range(3):
        print(i, " ", end="")
        for j in range(3):
            print(board[i][j], end="")
            if j < 2:
                print(" | ", end="")
        print()

# Function to check if a player has won by a row
def check_row(player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True, i, 0, i, 1, i, 2
    return False, None, None, None, None, None, None

# Function to check if a player has won by a column
def check_column(player):
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True, 0, j, 1, j, 2, j
    return False, None, None, None, None, None, None

# Function to check if a player has won by a diagonal
def check_diagonal(player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True, 0, 0, 1, 1, 2, 2
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True, 0, 2, 1, 1, 2, 0
    else:
        return False, None, None, None, None, None, None

# Function to check if a player has won
def check_win(player):
    row_win, row_i, row_j1, row_i, row_j2, row_i, row_j3 = check_row(player)
    if row_win:
        return True, row_i, row_j1, row_i, row_j2, row_i, row_j3
    column_win, col_i1, col_j, col_i2, col_j, col_i3, col_j = check_column(player)
    if column_win:
        return True, col_i1, col_j, col_i2, col_j, col_i3, col_j
    diagonal_win, diag_i1, diag_j1, diag_i2, diag_j2, diag_i3, diag_j3 = check_diagonal(player)
    if diagonal_win:
        return True, diag_i1, diag_j1, diag_i2, diag_j2, diag_i3, diag_j3
    return False, None, None, None, None, None, None

# Function to get the next move from the player
def get_move(player):
    while True:
        try:
            if player == "X":
                row = int(input("Enter row (0-2) for X: "))
                col = int(input("Enter column (0-2) for X: "))
            else:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
            if row < 0 or row > 2 or col < 0 or col > 2:
                raise ValueError
            if board[row][col] != " ":
                raise ValueError
            break
        except ValueError:
            print("Invalid move, please try again")
    return row, col

# Function to play the game
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You will be playing against the computer.")
    print("You are X and the computer is O.")
    print("Enter the row and column of your move when prompted.")
    print("The game board is shown below.")
    display_board()
    player = "X"
    while True:
        row, col = get_move(player)
        board[row][col] = player
        display_board()
        win, i1, j1, i2, j2, i3, j3 = check_win(player)
        if win:
            print("Congratulations, player", player, "has won!")
            print("The winning spaces are:", i1, j1, i2, j2, i3, j3)
            break
        if player == "X":
            player = "O"
        else:
            player = "X"
        if all([board[i][j] != " " for i in range(3) for j in range(3)]):
            print("The game is a tie!")
            break

if __name__ == "__main__":
    play_game()