from builtins import range

from piece.Color import Color
from piece.PieceType import PieceType
from piece.Piece import Piece
from piece.PieceFactory import PieceFactory

from utility.Position import Position


class Board:

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.pieces = self.instantiate_board()

    def add_piece(self,position,piece):
        if self.is_in_bound(position):
            self.pieces[position.get_x()][position.get_y()] = piece

    def instantiate_board(self):
        column = []

        column.append(self.build_row('WR,WN,WB,WQ,WK,WB,WN,WR'))
        column.append(self.build_row('WP,WP,WP,WP,WP,WP,WP,WP'))
        column.append(self.build_row('NE,NE,NE,NE,NE,NE,NE,NE'))
        column.append(self.build_row('NE,NE,NE,NE,NE,NE,NE,NE'))
        column.append(self.build_row('NE,NE,NE,NE,NE,NE,NE,NE'))
        column.append(self.build_row('NE,NE,NE,NE,NE,NE,NE,NE'))
        column.append(self.build_row('BP,BP,BP,BP,BP,BP,BP,BP'))
        column.append(self.build_row('BR,BN,BB,BK,BQ,BB,BN,BR'))

        return column

    def build_row(self, str):
        pieces = str.split(',')
        row = []

        for piece in pieces:
            color = Color.get_color(piece[0])
            #TODO hardcoded
            if len(piece) == 3:
                row.append(PieceFactory.build_used_pawn(color))
            else:
                row.append(PieceFactory.build_piece(piece[1], color))

        return row

    def get_possible_move(self, position):
        # TODO make special case for pawn
        piece = self.pieces[position.get_x()][position.get_y()]

        return piece.get_legal_move(self, position)

    def tile_is_empty(self, position):
        if not self.is_in_bound(position):
            raise Exception("position not in bound")
        return self.pieces[position.get_x()][position.get_y()].pieceType == PieceType.TILE

    def move_piece(self, original_position, new_position):
        piece = self.pieces[original_position.get_x()][original_position.get_y()]
        self.pieces[new_position.get_x()][new_position.get_y()] = piece
        self.pieces[original_position.get_x()][original_position.get_y()] = PieceFactory.build_piece('E',Color.NONE)

    def get_piece_at(self, position):
        return self.pieces[position.get_x()][position.get_y()]

    def is_in_bound(self, position):
        return 0 <= position.x < self.width and 0 <= position.y < self.height

    def show_possible_move(self, possible_move):
        str = ''
        for row in range(self.height):
            for piece in range(self.width):
                if Position(row, piece) in possible_move:
                    str += 'x'
                str += self.pieces[row][piece].__str__ + ', '
            str += '\n'
        return str

    def __str__(self):
        str = ' '
        for row in range(self.height):
            for piece in range(self.width):
                str += self.pieces[row][piece].__str__ + ', '

            str += '\n'

        return str


if __name__ == '__main__':
    board = Board(8, 8)

    test = board.get_possible_move(Position(1, 1))
    print(test)
    for position in test:
        print(position)

    print(board.show_possible_move(test), '\n')
