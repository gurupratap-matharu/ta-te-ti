
#!/usr/bin/python3
# Simple TicTacToe game in Python - EAO
import random
import sys
import time

board=[i for i in range(0,9)]

# Corners, Center and Others, respectively
moves=((1,7,3,9),(5,),(2,4,6,8))

# Winner combinations
winning_combinations = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

def print_board():
    """Simple prints the board after each turn with current player positions."""

    for count, position in enumerate(board):
        boardPiece=' '
        end = ' | ' 
        
        if (count+1) % 3 == 0:
            end = ' \n' # to enter a new line after every three pieces
            
            if (count+1) == 3 or count+1 == 6: 
                end+='---------\n'; # to print separation lines

        
        if position in ('X','O'):
            boardPiece = position
        
        print(boardPiece,end=end)

def select_char():
    """Randomly assigns 'X' and '0' to computer and player"""

    chars=('X','O')
    
    if random.randint(0,1) == 0:
        return chars[::-1]
    
    return chars

def can_move(position):
    """Checks if the move entered by a player or computer is possible. Returns a boolean."""

    return board[position-1] == position-1

def can_win(turn, move):
    """Finds out if a player has won the game or not. Returns a boolean."""
    temp = board[move-1]
    board[move-1] = turn
    
    
    for row in winning_combinations:
        won = True
        for position in row:
            if board[position] != turn:
                won = False
                break 
        if won:
            board[move -1] = temp
            return won
    
    board[move-1] = temp
    return won


def make_move(turn, move):
    """Register a legitimate move by any player"""
    if can_move(move):
        board[move-1] = turn
        return can_win(turn, move)
    else:
        return False
     
def computer_move():
    """
    Makes the computer take an intelligent move to win the game. Returns True if computer wins
    else False.
    """

    # Let computer check for any possible move to end the game.
    for possibleMove in range(1,10):
        if can_move(possibleMove) and can_win(computer, possibleMove):
    
            make_move(computer, possibleMove)
            return can_win(computer, possibleMove) 
    
    # If player can win, block him.
    for possibleMove in range(1,10):
        if can_move(possibleMove) and can_win(player, possibleMove):
            make_move(computer, possibleMove)
            return can_win(computer, possibleMove)

    # Otherwise, try to take one of desired places.
    for combinations in moves:
        for possibleMove in combinations:
            if can_move(possibleMove):
                make_move(computer, possibleMove)
                return can_win(computer, possibleMove)

def space_exist():
    return board.count('X') + board.count('O') != 9

