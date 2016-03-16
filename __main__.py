""" chess/__main__.py """
################################################################################
# Application:      Chess
# File:             __main__.py
# Goal:
# Input:            - The dimensions of the board: M, N
#                   - The number of pieces of each type (King, Queen, Bishop,
#                     Rook and Knight) to try and place on the board.
# Output:           - All the unique configurations to the console for which all
#                     of the pieces can be placed on the board without
#                     threatening each other.
# Examples:         Input:  2 kings and 1 rook
#                   Output: 4 options
#
#                   Input:  2 rooks and 4 knights
#                   Output: 8 options
#
# History:          2016-03-09 - JJ     Creation of the file
#                   2016-03-10 - JJ     Added Board class
#                   2016-03-14 - JJ     Added further calculation, no recursion
#                   2016-03-15 - JJ     Added tests + assignment
#                   2016-03-16 - JJ     Added recursion + pylint fixes

################################################################################
# Imports
################################################################################
from argparse import ArgumentParser
import copy
import datetime

################################################################################
# Definitions
################################################################################

################################################################################
# Functions
################################################################################

class Piece(object):

    def __init__(self):
        self._type = None
        self._h = False
        self._v = False
        self._d = False
        self._range = 0
        self._footprint = None

    def __repr__(self):
        return self._type

    def __str__(self):
        return self._type

    @property
    def range(self):
        return self._range

    def _get_footprint(self, xpos, ypos, width, height):
        fp = []
        if self._type is 'Night':
            kpositions = [[1,2], [2,1], [-2,-1], [-1,-2], [1,-2], [2, -1], [-1,2], [-2,1]]
            for pos in kpositions:
                x = xpos + pos[0]
                y = ypos + pos[1]
                if y >= 0 and y < height and x >= 0 and x < width:
                    fp.append([x,y])
        else:
            if self._h:
                if self.range is 'inf':
                    self._range = width
                for i in range(-1*self.range, self.range+1):
                    if i != 0:
                        x = xpos+i
                        if x >= 0 and x < width:
                            fp.append([x,ypos])

            if self._v:
                if self.range is 'inf':
                    self._range = height
                for i in range(-1*self.range, self.range+1):
                    if i != 0:
                        y = ypos+i
                        if y >= 0 and y < height:
                            fp.append([xpos,y])
            if self._d:
                if self.range is 'inf':
                    if height > width:
                        self._range = height
                    else:
                        self._range = width
                for i in range(-1*self.range, self.range+1):
                    if i != 0:
                        x = xpos+i
                        y = ypos+i
                        if y >= 0 and y < height and x >= 0 and x < width:
                            fp.append([x,y])
                        x = xpos-i
                        if y >= 0 and y < height and x >= 0 and x < width:
                            fp.append([x,y])
        return fp

class Queen(Piece):

    def __init__(self):
        super(Queen, self).__init__()
        self._type = 'Queen'
        self._h = True
        self._v = True
        self._d = True
        self._range = 'inf'

class King(Piece):

    def __init__(self):
        super(King, self).__init__()
        self._type = 'King'
        self._h = True
        self._v = True
        self._d = True
        self._range = 1

class Rook(Piece):

    def __init__(self):
        super(Rook, self).__init__()
        self._type = 'Rook'
        self._h = True
        self._v = True
        self._d = False
        self._range = 'inf'

class Knight(Piece):
    # L-shape
    def __init__(self):
        super(Knight, self).__init__()
        self._type = 'Night'
        self._h = False
        self._v = False
        self._d = False

class Bishop(Piece):

    def __init__(self):
        super(Bishop, self).__init__()
        self._type = 'Bishop'
        self._h = False
        self._v = False
        self._d = True
        self._range = 'inf'

class Board(object):

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._grid = self._set_grid()
        self._pieces = None
        self._solutions = []

    def _set_grid(self):
        """ Creates a matrix with spaces """
        grid = [[' ' for w in range(self.width)] for h in range(self.height)]
        return grid

    def _print_grid(self, char=None):
        """ Prints the grid to console """
        for hcol in range(self.width*2+1):
            print '-',
        print ''
        for row in range(self.height):
            print '|',
            for col in range(self.width):
                print self.grid[row][col].replace('x', char), '|',
            print ''
            for hcol in range(self.width*2+1):
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

    def set_piece_on_grid(self, piece, option):
        """ Puts the piece on the grid and allocates the space around it """
        self.grid[option[1]][option[0]] = piece._type[0:1]
        piece._footprint = piece._get_footprint(option[0], option[1], self.width, self.height)
        for p in piece._footprint:
            self.grid[p[1]][p[0]] = 'x'

    def get_options(self, piece):
        """ Calculates where the piece could be placed on the grid """
        options = []
        for row in range(self.height):
            for col in range(self.width):
                piece._footprint = piece._get_footprint(row, col, self.width, self.height)
                if self.grid[row][col] == ' ' and self.isspace(piece):
                    options.append([col, row])
        return options

    def isspace(self, piece):
        """ Calculates if the footprint of the piece fits on the grid """
        for p in piece._footprint:
            if self.grid[p[0]][p[1]] != ' ' and self.grid[p[0]][p[1]] != 'x':
                return False
        return True

    def set_pieces(self, kings, queens, bishops, rooks, knights):
        """ Set pieces of the board """
        pieces = []
        for q in range(queens):
            pieces.append(Queen())
        for k in range(kings):
            pieces.append(King())
        for r in range(rooks):
            pieces.append(Rook())
        for b in range(bishops):
            pieces.append(Bishop())
        for n in range(knights):
            pieces.append(Knight())

        self._pieces = pieces
        self.put_pieces()
        if self.solutions is not None:
            for index, sol in enumerate(self.solutions):
                print 'Solution '+str(index+1)
                self.print_solution(sol)

    def ble(self, piece, placedpieces=None):
        """ Ble """
        self._grid = self._set_grid()
        if placedpieces:
            for item in placedpieces:
                if item[1] is not None:
                    self.set_piece_on_grid(item[0], item[1])
        options = self.get_options(piece)

        return options

    def get_pos(self, positions, index=0):
        """ Get postion """
        piece = self.pieces[index]
        options = self.ble(piece, positions)

        for option in options:
            positions[index][1] = option
            if len(self.pieces) > index+1:
                for i in range(index+1, len(self.pieces)):
                    positions[i][1] = None
                self.get_pos(positions, index+1)
            else:
                if self.check_duplicate(positions) is False:
                    self._solutions.append(copy.deepcopy(positions))
        return True

    def put_pieces(self):
        """ Put pieces """
        pls = []
        positions = []
        for p in self.pieces:
            positions.append([p, None])

        self.get_pos(positions)
        print len(self.solutions)
        for solution in self.solutions:
            self.print_solution(solution)
        return pls

    def print_solution(self, solution):
        """ Prints the solution on the grid """
        self._grid = self._set_grid()
        for item in solution:
            self.set_piece_on_grid(item[0], item[1])
        self._print_grid(' ')

    def check_duplicate(self, newsolution):
        """ Check if the new solution already exists in the solutions """
        if self.solutions is not None:
            for solution in self.solutions:
                result = []
                for item in newsolution:
                    positions = self.get_positions_for_item(solution, item[0])
                    if item[1] in positions:
                        result.append(True)
                    else:
                        result.append(False)
                if all(val is True for val in result):
                    # Duplicate found. All positions match
                    return True
        return False

    def get_positions_for_item(self, solution, item):
        """ Returns the positions of an item in a given solution """
        positions = []
        # Loop through the pieces in a solution
        for piece in solution:
            # Compare the types of all the pieces in a solution
            if type(piece[0]) is type(item):
                # Append the position to the result list
                positions.append(piece[1])
        return positions

def main():
    """ Main function """
    parser = ArgumentParser()
    parser.add_argument("-x", "--horizontal", dest="width", default=3, type=int,
    help="Horizontal dimension (default=3)")
    parser.add_argument("-y", "--vertical", dest="height", default=3, type=int,
    help="Vertical dimension (default=3)")
    parser.add_argument("-k", "--kings", dest="kings", default=0, type=int,
    help="Number of kings")
    parser.add_argument("-q", "--queens", dest="queens", default=0, type=int,
    help="Number of queens")
    parser.add_argument("-b", "--bishops", dest="bishops", default=0, type=int,
    help="Number of bishops")
    parser.add_argument("-r", "--rooks", dest="rooks", default=0, type=int,
    help="Number of rooks")
    parser.add_argument("-n", "--knights", dest="knights", default=0, type=int,
    help="Number of knights")
    args = parser.parse_args()

    if sum([args.kings, args.queens, args.bishops, args.rooks, args.knights]) == 0:
        input_kings = raw_input("Number of kings ")
        try:
            args.kings = int(input_kings)
        except ValueError:
            print 'No chess pieces given. Nothing to do. Exiting!'
            exit(2)
    else:
        print 'Chess pieces:'
        print '- Kings ' + str(args.kings)
        print '- Queens ' + str(args.queens)
        print '- Bishops ' + str(args.bishops)
        print '- Rooks ' + str(args.rooks)
        print '- Knights ' + str(args.knights)

    board = Board(args.width, args.height)
    print 'Start', datetime.datetime.now()
    board.set_pieces(args.kings, args.queens, args.bishops, args.rooks, args.knights)
    print 'End', datetime.datetime.now()

    # Test 1
    board_test_1 = Board(3, 3)
    print 'Start', datetime.datetime.now()
    board_test_1.set_pieces(2, 0, 0, 1, 0)
    print 'End', datetime.datetime.now()
    if len(board_test_1.solutions) == 4:
        print 'Test succeeded!'

    # Test 2
    board_test_2 = Board(4, 4)
    print 'Start', datetime.datetime.now()
    board_test_2.set_pieces(0, 0, 0, 2, 4)
    print 'End', datetime.datetime.now()
    if len(board_test_2.solutions) == 8:
        print 'Test succeeded!'

    # Assignment
    # board = Board(7, 7)
    # print 'Start', datetime.datetime.now()
    # board.set_pieces(2, 2, 2, 0, 1)
    # print 'Start', datetime.datetime.now()

################################################################################
# main
################################################################################
if __name__ == "__main__":
    main()
