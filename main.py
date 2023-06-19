# Tic Tac Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check if a player has won
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to play the game
def play_game():
    player = 'X'
    while True:
        display_board()
        position = int(input('Enter the position (1-9) to place ' + player + ': ')) - 1
        if board[position] == ' ':
            board[position] = player
            if check_win(player):
                display_board()
                print('Player', player, 'wins!')
                break
            if ' ' not in board:
                display_board()
                print('It\'s a tie!')
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print('That position is already filled. Try again.')

# Start the game
play_game()
