import unittest
import random

from tateti import moves, winning_combinations, board
from tateti import select_char, can_win, space_exist, make_move, computer_move, can_move

class TicTacToeTest(unittest.TestCase):

    """
    Our main testing class. Here we'll define
    methods to test various functions of our 
    module.
    """
    def test_select_char_gives_opposite_results(self):
        player1, player2 = select_char()
        
        self.assertNotEqual(player1, player2)
    
    def test_cannot_move_to_occupied_position(self):
        for i in range(1,10):
            make_move('X', i)
        self.assertFalse(can_move(3))

    def test_can_win(self):
        board = ['X','X',2,3,4,5,6,7,8]
        self.assertFalse(can_win('X', 9))

    def test_space_exist(self):
        self.assertFalse(space_exist())

if __name__ == '__main__':
    unittest.main()

