
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