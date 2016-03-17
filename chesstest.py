""" chess/chesstest.py """
################################################################################
# Application:      Chess
# File:             chesstest.py
# Goal:             Defines the tests for the chess application
# Input:
# Output:
# Examples:
#
# History:          2016-03-16 - JJ     Creation of the file
#
################################################################################
# Imports
################################################################################
import unittest
from chess.board import Board
from chess.pieces import King

################################################################################
# Definitions
################################################################################

################################################################################
# Functions
################################################################################

class ChessTests(unittest.TestCase):
    """ Tests for the Chess assignment """
    def setUp(self):
        """ Create a 3 by 3 board for all test cases """
        self.board = Board(3, 3)

    def test_example_one(self):
        """ Example 1 from the assignment """
        self.board.set_pieces({'king':2, 'rook':1})
        self.board.put_pieces()
        self.failUnless(len(self.board.solutions) == 4)

    def test_example_two(self):
        """ Example 2 from the assignment """
        self.board = Board(4, 4)
        self.board.set_pieces({'rook': 2, 'knight' : 4})
        self.failUnless(len(self.board.solutions) == 8)

    def test_put_one_king_left_top(self):
        """ Test the placement of one king on [0, 0] """
        piece = King()
        self.board.set_piece_on_grid(piece, [0, 0])
        self.failUnless(self.board.get_value(0, 0) == 'K' and
                        self.board.get_value(0, 1) == 'x' and
                        self.board.get_value(0, 2) == ' ' and
                        self.board.get_value(1, 0) == 'x' and
                        self.board.get_value(1, 1) == 'x' and
                        self.board.get_value(1, 2) == ' ' and
                        self.board.get_value(2, 0) == ' ' and
                        self.board.get_value(2, 1) == ' ' and
                        self.board.get_value(2, 2) == ' ')

    def test_put_two_kings_center(self):
        """ Test the placement of one king in the center """
        piece = King()
        self.board.set_piece_on_grid(piece, [1, 1])
        self.failUnless(self.board.get_value(0, 0) == 'x' and
                        self.board.get_value(0, 1) == 'x' and
                        self.board.get_value(0, 2) == 'x' and
                        self.board.get_value(1, 0) == 'x' and
                        self.board.get_value(1, 1) == 'K' and
                        self.board.get_value(1, 2) == 'x' and
                        self.board.get_value(2, 0) == 'x' and
                        self.board.get_value(2, 1) == 'x' and
                        self.board.get_value(2, 2) == 'x')

    def test_positions_for_two_kings(self):
        """ Test the positions for the 2nd king after placing the 1st king """
        piece = King()
        # Put the first King
        self.board.set_piece_on_grid(piece, [0, 0])
        positions = []
        positions.append([piece, [0, 0]])
        # Get the positions for the second King
        options = self.board.get_options_after_fill(piece, positions)
        self.failUnless(options == [[2, 0], [2, 1], [0, 2], [1, 2], [2, 2]])

    def test_solution_exists(self):
        """ The solution exists in the list of solutions """
        solutions = [[King, [0, 0]], [King, [0, 2]]]
        newsolution = [[King, [0, 0]], [King, [0, 2]]]
        self.board.check_duplicate(solutions, newsolution)
        self.failUnless(False)

    def test_solution_not_exist(self):
        """ The solution does not exist in the list of solutions """
        # check_duplicate(
        self.failUnless(False)

def main():
    """ main function """
    unittest.main()

if __name__ == '__main__':
    main()
