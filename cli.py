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
        print("TODO: take a turn!")
        print(board)
        x, y = input("The coordinate of your move:")
        board[x][y] = player
        winner = get_winner(board)