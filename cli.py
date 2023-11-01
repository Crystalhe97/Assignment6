# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board


# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = 'O'
    while winner is None:
        player = other_player(player)
        print("It's " + player + "'s turn!")
        print(board)
        x, y = [int(i) for i in input("The coordinate of your move: ").split(",")]
        board[x][y] = player
        winner = get_winner(board)
    print(winner + " wins the game!")
