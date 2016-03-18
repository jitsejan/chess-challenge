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
#                   2016-03-16 - JJ     Split of classes pieces, board
#                   2016-03-17 - JJ     Clean-up before delivery
#
################################################################################
# Imports
################################################################################
from chess.board import Board
from argparse import ArgumentParser
import datetime

################################################################################
# Definitions
################################################################################

################################################################################
# Functions
################################################################################

def assignment():
    """ Assignment """
    board = Board(5, 5)
    pieces = {}
    pieces['king'] = 2
    pieces['queen'] = 2
    pieces['bishop'] = 2
    pieces['rook'] = 0
    pieces['knight'] = 1
    start = datetime.datetime.now()
    print 'Start', start
    board.set_pieces(pieces)
    board.put_pieces()
    end = datetime.datetime.now()
    print 'End', end
    print 'Duration', end-start
    print 'Found '+str(len(board.solutions))+ ' solutions'
    exit()

def main():
    """ Main function """
    parser = ArgumentParser()
    parser.add_argument("-x", "--horizontal", dest="width", default=3, type=int,
    help="Horizontal dimension (default=3)")
    parser.add_argument("-y", "--vertical", dest="height", default=3, type=int,
    help="Vertical dimension (default=3)")
    parser.add_argument("-k", "--kings", dest="king", default=0, type=int,
    help="Number of kings")
    parser.add_argument("-q", "--queens", dest="queen", default=0, type=int,
    help="Number of queens")
    parser.add_argument("-b", "--bishops", dest="bishop", default=0, type=int,
    help="Number of bishops")
    parser.add_argument("-r", "--rooks", dest="rook", default=0, type=int,
    help="Number of rooks")
    parser.add_argument("-n", "--knights", dest="knight", default=0, type=int,
    help="Number of knights")
    parser.add_argument("-p", "--print", dest="printsolutions", default=False,
    help="Print the solutions", action='store_true')
    args = parser.parse_args()

    if sum([args.king, args.queen, args.bishop, args.rook, args.knight]) == 0:
        print 'No chess pieces given. Nothing to do. Running the assignment!'
        assignment()
    else:
        print 'Chess pieces:'
        print '- Kings ' + str(args.king)
        print '- Queens ' + str(args.queen)
        print '- Bishops ' + str(args.bishop)
        print '- Rooks ' + str(args.rook)
        print '- Knights ' + str(args.knight)

    board = Board(args.width, args.height)
    pieces = {}
    pieces['king'] = args.king
    pieces['queen'] = args.queen
    pieces['bishop'] = args.bishop
    pieces['rook'] = args.rook
    pieces['knight'] = args.knight
    board.set_pieces(pieces)
    print 'Start', datetime.datetime.now()
    board.put_pieces()
    print 'End', datetime.datetime.now()
    print 'Found '+str(len(board.solutions))+ ' solutions'
    if args.printsolutions is True:
        board.print_solutions()

################################################################################
# main
################################################################################
if __name__ == "__main__":
    main()
