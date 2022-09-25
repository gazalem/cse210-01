"""
Author: Alan Montoya
Version: 1.0.0
Date: Sep 20th, 2022
Problem Statement:
    Create the Tic Tac Toe game
Language:
    Python
"""

# Plugins or Utils obtain OS utils
import shutil
import os
import random as rd
import time


# Obtain number of column of the shell
TERMINAL_SIZE = shutil.get_terminal_size().columns
PROGRAM_TITLE = 'Tic Tac Toe'
GAME_MARKS = ["X", "O"]
PLAYER_ONE = {}
PLAYER_TWO = {}

def clear_console():
    """ Clear the console accorging the the OS
    Returns: nothing
    """
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')


# Print title center based on the size of their shell
def title_print(my_tittle: str):
    """Print a center title in console
    Parameters:
        my_tittle: String of the tittle
    Returns: nothing
    """
    tittle = f'{my_tittle}  - \U0001f601  \n'
    print(tittle.center(TERMINAL_SIZE))


def draw_board(board: list[int], position: int=1, mark: str="1"):
    """Draw the Tic Tac Toe board on screen
    Parameters:
    board(array): number of position of the board
    position(int): position on the board
    mark(str): mark to set on the board.
    """
    clear_console()
    title_print(PROGRAM_TITLE)
    if not board:
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    board[position-1] = mark.upper()
    # show player board positions
    # to select in the board
    print("Tic Tac Toe Positions")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\n"*3)

    # show user selection on
    # the game board
    # Actual Game
    print("Tic Tac Toe Game")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n"*3)
    return board


def check_winner(board: list[int], player_name: str, player_mark: str, winner: bool):
    """Check if a player win the match
    Parameters:
    board: the updated array with the marks
    player_mark: the player used mark X or O
    player_name: the player moves being checked
    winner: flag to check winner
    """
    if board[0] == player_mark and board[1] == player_mark and board[2] == player_mark:
        print(f"{player_name} win!\n")
        winner = True
    elif board[3] == player_mark and board[4] == player_mark and board[5] == player_mark:
        print(f"{player_name} win!\n")
        winner = True
    elif board[6] == player_mark and board[7] == player_mark and board[8] == player_mark:
        print(f"{player_name} win!\n")
        winner = True
    elif board[0] == player_mark and board[3] == player_mark and board[6] == player_mark:
        print(f"{player_name} win!\n")
        winner = True
    elif board[1] == player_mark and board[4] == player_mark and board[7] == player_mark:
        print(f"{player_name} win!\n")
        winner = True
    elif board[2] == player_mark and board[5] == player_mark and board[8] == player_mark:
        print(f"{player_name} win!\n")
        winner = True
    elif board[0] == player_mark and board[4] == player_mark and board[8] == player_mark:
        print(f"{player_name} win!\n")
        winner = True
    elif board[2] == player_mark and board[4] == player_mark and board[6] == player_mark:
        print(f"{player_name} win!\n")
        winner = True
    else:
        print("It's a draw!\n")
        winner = False
    return winner


def welcome_message():
    """Rafle for game player and mark used
    """
    clear_console()
    title_print(PROGRAM_TITLE)
    player_1_name = input("Player 1 - Enter your name: ")
    player_2_name = input("Player 2 - Enter your name: ")
    player_1_mark = rd.choice(GAME_MARKS)
    if GAME_MARKS.index(player_1_mark) == 0:
        player_2_mark = GAME_MARKS[1]
    else:
        player_2_mark = GAME_MARKS[0]
    PLAYER_ONE.update({"Name": player_1_name, "Mark": player_1_mark})
    PLAYER_TWO.update({"Name": player_2_name, "Mark": player_2_mark})
    return PLAYER_ONE, PLAYER_TWO


def player_moves(board: list, game_turn: int, player_turn: int, game_winner: bool):
    """UPDATE Board variable with player mark and
    check the if the player win.
    return:
    """
    print(f"\nPlayer One will be: {PLAYER_ONE.get('Name')} and will use: {PLAYER_ONE.get('Mark')}")
    print(f"Player Two will be: {PLAYER_TWO.get('Name')} and will use: {PLAYER_TWO.get('Mark')}")
    time.sleep(3)
    draw_board(board, position=1, mark="1")
    while not game_winner and game_turn < 9:
        if (player_turn % 2) == 1:
            player_position = int(input(f"{PLAYER_ONE.get('Name')}. Enter the position of your mark: "))
            draw_board(board, player_position, PLAYER_ONE.get("Mark"))
            game_winner = check_winner(board, PLAYER_ONE.get("Name"), PLAYER_ONE.get("Mark"), game_winner)
            game_turn += 1
            player_turn += 1
        else:
            player_position = int(input(f"{PLAYER_TWO.get('Name')}. Enter the position of your mark: "))
            draw_board(board, player_position, PLAYER_TWO.get("Mark"))
            game_winner = check_winner(board, PLAYER_TWO.get("Name"), PLAYER_TWO.get("Mark"), game_winner)
            game_turn += 1
            player_turn -= 1



def main():
    """ Entry point of the program
    """
    welcome_message()
    game_turn = 0
    player_turn = 1
    game_winner = False
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player_moves(board, game_turn, player_turn, game_winner)


if __name__ == "__main__":
    main()
