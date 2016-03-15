
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
#                   2016-03-08 - JJ     Added Board class
#
################################################################################

################################################################################
# Imports
################################################################################
from argparse import ArgumentParser

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

    def __str__(self):
        return self._type+' (horizontal='+str(self._h)+', vertical='+str(self._v)+', diagonal='+str(self._d)+')'

    @property
    def name(self):
        return self._name

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
        self._range = '1'

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
        self._type = 'Knight'
        self._h = True
        self._v = True
        self._d = False
        self._range = 'inf'

class Bishop(Piece):

    def __init__(self):
        super(Bishop, self).__init__()
        self._type = 'Bishop'
        self._h = False
        self._v = False
        self._d = True
        self._range = 'inf'

class Pawn(Piece):

    def __init__(self):
        super(Pawn, self).__init__()
        self._type = 'Pawn'
        self._h = True
        self._v = True
        self._d = False
        self._range = 'inf'

class Board(object):

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._grid = self._set_grid()

    def _set_grid(self):
        return [[' ' for w in range(self.width)] for h in range(self.height)]

    def _print_grid(self):
        for hcol in range(self.width*2+1):
            print '-',
        print ''
        for row in range(self.height):
            print '|',
            for col in range(self.width):
                print self.grid[row][col], '|',
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
        return self._width

    @property
    def height(self):
    	return self._height

    @property
    def grid(self):
        return self._grid

    def set_piece_on_grid(self, piece):
        if piece._v:
            print 'Vertical', piece._range
        else:
            print 'No move in vertical direction'

        if piece._h:
            print 'Horizontal', piece._range
        else:
            print 'No move in horizontal direction'

        if piece._d:
            print 'Diagonal', piece._range
        else:
            print 'No move in diagonal direction'

        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == ' ':
                    self.grid[row][col] = piece._type[0:1]
                    return True
        return False

    def set_pieces(self, kings, queens, bishops, rooks, knights, pawns):
        for q in range(queens):
            qp = Queen()
            print qp

        for k in range(kings):
            p = King()
            self.set_piece_on_grid(p)

        for b in range(bishops):
            p = Bishop()
            print bp

        for r in range(rooks):
            p = Rook()
            self.set_piece_on_grid(p)

        for n in range(knights):
            np = Knight()
            print np

        for p in range(pawns):
            pp = Pawn()
            print pp

################################################################################
# main
################################################################################
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-x", "--horizontal", dest="width", default=3, type=int,
                  help="Horizontal dimension")
    parser.add_argument("-y", "--vertical", dest="height", default=3, type=int,
                  help="Vertical dimension")
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
    parser.add_argument("-p", "--pawns", dest="pawns", default=0, type=int,
                  help="Number of pawns")
    args = parser.parse_args()

    if sum([args.kings, args.queens, args.bishops, args.rooks, args.knights]) == 0:
        print 'No chess pieces given. Nothing to do. Exiting!'
        exit(2)
    else:
        print 'Chess pieces:'
        print '- Kings ' + str(args.kings)
        print '- Queens ' + str(args.queens)
        print '- Bishops ' + str(args.bishops)
        print '- Rooks ' + str(args.rooks)
        print '- Knights ' + str(args.knights)
        print '- Pawns ' + str(args.pawns)

        board = Board(args.width, args.height)
        board._print_grid()
        board.set_pieces(args.kings, args.queens, args.bishops, args.rooks, args.knights, args.pawns)
        board._print_grid()
