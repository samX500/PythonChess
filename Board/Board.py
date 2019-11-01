from builtins import range

from piece.Color import Color
from piece.Direction import Direction
from piece.PieceType import PieceType

from piece.Piece import Piece


class Board:
    DEFAULT_LAYOUT = 'RNBQKBNR'

    pieces = []
    height = 0
    width = 0

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.pieces = self.instantiateBoard()

    def instantiateBoard(self):
        # Make this better once I understand loop better
        column = []
        column.append(self.buildPieceRow(Color.WHITE))
        column.append(self.buildPawnRow(Color.WHITE))
        column.append(self.buildEmptyRow())
        column.append(self.buildEmptyRow())
        column.append(self.buildEmptyRow())
        column.append(self.buildEmptyRow())
        column.append(self.buildPawnRow(Color.BLACK))
        column.append(self.buildPieceRow(Color.BLACK))

        return column

    def buildPieceRow(self, color):
        row = []

        # The isFirstRow can probably be put in the for if I try hard enough
        if color == Color.WHITE:
            for char in self.DEFAULT_LAYOUT:
                row.append(Piece(PieceType.getPieceType(PieceType, char), color))
        else:
            for char in self.DEFAULT_LAYOUT[::-1]:
                row.append(Piece(PieceType.getPieceType(PieceType, char), color))

        return row

    def buildPawnRow(self, color):
        row = []
        for char in range(self.width):
            row.append(Piece(PieceType.PAWN, color))

        return row

    def buildEmptyRow(self):
        row = []
        for char in range(self.width):
            row.append(Piece(PieceType.TILE, Color.NONE))

        return row

    def __str__(self):
        str  = ' '
        for row in range(self.height):
            for piece in range(self.width):
                str += self.pieces[row][piece].__str__() + ', '

        print(str)
        return str


if __name__ == '__main__':
    board = Board(8, 8)
    print(board)
