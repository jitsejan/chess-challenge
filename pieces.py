""" chess/pieces.py """
################################################################################
# Application:      Chess
# File:             pieces.py
# Goal:             Defines the class Piece for the chess pieces
# Input:            name, abbrevation, move, step
# Output:           Piece with name, abbrevation, step and move in 3 directions
# Examples:
#
# History:          2016-03-16 - JJ     Creation of the file
#
################################################################################
# Imports
################################################################################

################################################################################
# Definitions
################################################################################

################################################################################
# Class
################################################################################

class Piece(object):
    """ Defines the Piece class """
    def __init__(self, name, abbrevation, move, step):
        self._name = name
        self._abbrevation = abbrevation
        self._hmove = move[0]
        self._vmove = move[1]
        self._dmove = move[2]
        self._step = step

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    @property
    def name(self):
        """ Return the name of the piece """
        return self._name

    @property
    def abbrevation(self):
        """ Return the abbrevation of the piece """
        return self._abbrevation

    @property
    def hmove(self):
        """ Return if piece moves horizontal """
        return self._hmove

    @property
    def vmove(self):
        """ Return if piece moves vertical """
        return self._vmove

    @property
    def dmove(self):
        """ Return if piece moves diagonal """
        return self._dmove

    @property
    def step(self):
        """ Return the step of the piece """
        return self._step

    def get_space(self, xpos, ypos, width, height):
        """ Get the allocation for a piece """
        footprint = []
        # The knight has a different footprint
        if self.name is 'Knight':
            footprint = self.get_knight_footprint(xpos, ypos, width, height)
        else:
            if self.hmove:
                for pos in self.get_hor_footprint(xpos, ypos, width):
                    footprint.append(pos)
            if self.vmove:
                for pos in self.get_ver_footprint(xpos, ypos, height):
                    footprint.append(pos)
            if self.dmove:
                for pos in self.get_diag_footprint(xpos, ypos, width, height):
                    footprint.append(pos)
        return footprint

    def get_diag_footprint(self, xpos, ypos, width, height):
        """ Return the diagonal footprint for a piece """
        footprint = []
        # If the stepsize is infinite, put the limit to the size of the board
        if self.step is 'inf':
            if height > width:
                self._step = height
            else:
                self._step = width
        # Append positions to the footprint
        for i in [j for j in range(-1*self.step, self.step+1) if j != 0]:
            xgrid = xpos+i
            ygrid = ypos+i
            if 0 <= ygrid < height and 0 <= xgrid < width:
                footprint.append([xgrid, ygrid])
            xgrid = xpos-i
            if 0 <= ygrid < height and 0 <= xgrid < width:
                footprint.append([xgrid, ygrid])
        return footprint

    def get_ver_footprint(self, xpos, ypos, height):
        """ Returns the vertical footprint for a given position """
        footprint = []
        # If the stepsize is infinite, put the limit to the size of the board
        if self.step is 'inf':
            self._step = height
        # Append positions to the footprint
        for i in [j for j in range(-1*self.step, self.step+1) if j != 0]:
            ygrid = ypos+i
            if 0 <= ygrid < height:
                footprint.append([xpos, ygrid])
        return footprint

    def get_hor_footprint(self, xpos, ypos, width):
        """ Returns the horizontal footprint for a given position """
        footprint = []
        # If the stepsize is infinite, put the limit to the size of the board
        if self.step is 'inf':
            self._step = width
        # Append positions to the footprint
        for i in [j for j in range(-1*self.step, self.step+1) if j != 0]:
            xgrid = xpos+i
            if 0 <= xgrid < width:
                footprint.append([xgrid, ypos])
        return footprint

    @classmethod
    def get_knight_footprint(cls, xpos, ypos, width, height):
        """ Returns the footprint of the knight for a given position """
        footprint = []
        kpositions = [[1, 2], [2, 1],
                      [-2, -1], [-1, -2],
                      [1, -2], [2, -1],
                      [-1, 2], [-2, 1]]
        # Append positions to the footprint
        for pos in kpositions:
            xgrid = xpos + pos[0]
            ygrid = ypos + pos[1]
            if 0 <= ygrid < height and 0 <= xgrid < width:
                footprint.append([xgrid, ygrid])
        return footprint

class Queen(Piece):
    """ Initialize a Queen piece """
    def __init__(self):
        super(Queen, self).__init__('Queen', 'Q', [True, True, True], 'inf')

class King(Piece):
    """ Initialize a King piece """
    def __init__(self):
        super(King, self).__init__('King', 'K', [True, True, True], 1)

class Rook(Piece):
    """ Initialize a Rook piece """
    def __init__(self):
        super(Rook, self).__init__('Rook', 'R', [True, True, False], 'inf')

class Knight(Piece):
    """ Initialize a Knight piece """
    def __init__(self):
        super(Knight, self).__init__('Knight', 'N', [False, False, False], 0)

class Bishop(Piece):
    """ Initialize a Bishop piece """
    def __init__(self):
        super(Bishop, self).__init__('Bishop', 'B', [False, False, True], 'inf')
