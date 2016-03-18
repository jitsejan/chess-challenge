""" chess/board.py """
################################################################################
# Application:      Chess
# File:             board.py
# Goal:             Defines the class Board for the chess board
# Input:            width, height
# Output:           board with dimensions width x height
# Examples:
#
# History:          2016-03-16 - JJ     Creation of the file
#
################################################################################
# Imports
################################################################################
from chess.pieces import King, Queen, Rook, Bishop, Knight

################################################################################
# Definitions
################################################################################

################################################################################
# Functions
################################################################################
import copy

class Board(object):
    """ Defines the Board class """

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._grid = self._set_grid()
        self._pieces = []
        self._solutions = []

    def _set_grid(self):
        """ Creates a matrix with spaces """
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        return grid

    def _print_grid(self, char='x'):
        """ Prints the grid to console """
        for _ in range(self.width*2+1):
            print '-',
        print ''
        for row in range(self.height):
            print '|',
            for col in range(self.width):
                print self.grid[row][col].replace('x', char), '|',
            print ''
            for _ in range(self.width*2+1):
                print '-',
            print ''

    def __repr__(self):
        return "Board()"

    def __str__(self):
        return "Board("+str(self.width) +"x"+str(self.height)+")"

    @property
    def width(self):
        """ Return width of the board """
        return self._width

    @property
    def height(self):
        """ Return height of the board """
        return self._height

    @property
    def grid(self):
        """ Return grid of the board """
        return self._grid

    @property
    def pieces(self):
        """ Return pieces of the board """
        return self._pieces

    @property
    def solutions(self):
        """ Return solutions of the board """
        return self._solutions

    def get_value(self, posx, posy):
        """ Returns value on grid on given position """
        return self.grid[posx][posy]

    def set_pieces(self, inputpieces):
        """ Set pieces of the board """
        if 'queen' in inputpieces:
            for _ in range(inputpieces['queen']):
                self._pieces.append(Queen())
        if 'rook' in inputpieces:
            for _ in range(inputpieces['rook']):
                self._pieces.append(Rook())
        if 'bishop' in inputpieces:
            for _ in range(inputpieces['bishop']):
                self._pieces.append(Bishop())
        if 'king' in inputpieces:
            for _ in range(inputpieces['king']):
                self._pieces.append(King())
        if 'knight' in inputpieces:
            for _ in range(inputpieces['knight']):
                self._pieces.append(Knight())

    def set_piece_on_grid(self, piece, pos):
        """ Puts the piece on the grid and allocates the space around it """
        if 0 <= pos[1] < self.width and 0 <= pos[0] < self.height:
            self.grid[pos[1]][pos[0]] = piece.abbrevation
            for opt in piece.get_space(pos[0], pos[1], self.width, self.height):
                self.grid[opt[1]][opt[0]] = 'x'
            return True
        else:
            return False

    def is_space(self, piece, row, col):
        """ Calculates if the footprint of the piece fits on the grid """
        for opt in piece.get_space(row, col, self.width, self.height):
            if self.get_value(opt[0], opt[1]) not in [' ', 'x']:
                return False
        return True

    def get_options(self, piece):
        """ Calculates where the piece could be placed on the grid """
        options = []
        height = self.height
        for row in range(height):
            width = self.width
            for col in range(width):
                if self.get_value(row, col) == ' ':
                    if self.is_space(piece, row, col):
                        options.append([col, row])
        return options

    def get_options_after_fill(self, piece, placedpieces=None):
        """ Get the options after putting the already placed pieces """
        self._grid = self._set_grid()
        options = []
        if placedpieces:
            for item in placedpieces:
                if item[1] is not None:
                    self.set_piece_on_grid(item[0], item[1])
        options = self.get_options(piece)
        return options

    def get_solutions(self, positions, index=0):
        """ Get position """
        piece = self.pieces[index]
        options = self.get_options_after_fill(piece, positions)
        for option in options:
            positions[index][1] = option
            if len(self.pieces) > index+1:
                for i in range(index+1, len(self.pieces)):
                    positions[i][1] = None
                self.get_solutions(positions, index+1)
            else:
                if self.check_duplicate(self.solutions, positions) is False:
                    self._solutions.append(copy.deepcopy(positions))
                    # self.print_solution(positions)
        return True

    def put_pieces(self):
        """ Put the pieces on the grid and set the solutions """
        positions = []
        for piece in self.pieces:
            positions.append([piece, None])
        self.get_solutions(positions)

    def print_solutions(self):
        """ Prints the solution on the grid """
        if len(self.solutions) > 0:
            for solution in self.solutions:
                self.print_solution(solution)
        else:
            print 'No solutions found!'

    def print_solution(self, solution, char=' '):
        """ Prints a single solution """
        self._grid = self._set_grid()
        for item in solution:
            self.set_piece_on_grid(item[0], item[1])
        self._print_grid(char)

    @classmethod
    def check_duplicate(cls, solutions, newsolution):
        """ Check if the new solution already exists in the solutions """
        if solutions is not None:
            for solution in solutions:
                result = []
                for item in newsolution:
                    positions = cls.get_positions_for_item(solution, item[0])
                    if item[1] in positions:
                        result.append(True)
                    else:
                        result.append(False)
                if all(val is True for val in result):
                    # Duplicate found. All positions match
                    return True
        return False

    @classmethod
    def get_positions_for_item(cls, solution, item):
        """ Returns the positions of an item in a given solution """
        positions = []
        # Loop through the pieces in a solution
        for piece in solution:
            # Compare the types of all the pieces in a solution
            if type(piece[0]) is type(item):
                # Append the position to the result list
                positions.append(piece[1])
        return positions
        