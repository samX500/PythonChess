from builtins import range

from piece.Color import Color
from piece.Direction import Direction
from piece.PieceType import PieceType

from piece.Piece import Piece
from utility.Position import Position


class Board:
    DEFAULT_LAYOUT = 'RNBQKBNR'

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.pieces = self.instantiateBoard()

    def instantiateBoard(self):
        # Make this better once I understand loop better
        column = []
        column.append(self.build_piece_row(Color.WHITE))
        column.append(self.build_pawn_row(Color.WHITE))
        column.append(self.build_empty_row())
        column.append(self.build_empty_row())
        column.append(self.build_empty_row())
        column.append(self.build_empty_row())
        column.append(self.build_pawn_row(Color.BLACK))
        column.append(self.build_piece_row(Color.BLACK))

        return column

    def build_piece_row(self, color):
        row = []

        # The isFirstRow can probably be put in the for if I try hard enough
        if color == Color.WHITE:
            for char in self.DEFAULT_LAYOUT:
                row.append(Piece(PieceType.get_piece_type(char), color))
        else:
            for char in self.DEFAULT_LAYOUT[::-1]:
                row.append(Piece(PieceType.get_piece_type(char), color))

        return row

    def build_pawn_row(self, color):
        row = []
        for char in range(self.width):
            row.append(Piece(PieceType.PAWN, color))

        return row

    def build_empty_row(self):
        row = []
        for char in range(self.width):
            row.append(Piece(PieceType.TILE, Color.NONE))

        return row

    def get_possible_move(self,position):
        piece = self.pieces[position.get_x()][position.get_y()]
        movement = piece.get_movement()
        possible_move = []

        for value in movement:
            for i in range(value.get_length()):
                position.add(*value.get_direction().value)
                if self.tile_is_empty(position):
                    possible_move.append(position)

    def tile_is_empty(self,position):
        return self.pieces[position.get_x()][position.get_y()].pieceType == PieceType.TILE

    def move_piece(self, original_position, new_position):
        piece = self.pieces[original_position.get_x()][original_position.get_y()]
        self.pieces[new_position.get_x()][new_position.get_y()] = piece
        self.pieces[original_position.get_x()][original_position.get_y()] = Piece(PieceType.TILE, Color.NONE)

    def __str__(self):
        str = ' '
        for row in range(self.height):
            for piece in range(self.width):
                str += self.pieces[row][piece].__str__ + ', '

            str += '\n'

        return str


if __name__ == '__main__':
    board = Board(8, 8)

    print(board.get_possible_move(Position(1,1)))
    print(board)
