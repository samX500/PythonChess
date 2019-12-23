from piece import *


class PieceFactory():

    @staticmethod
    def build_piece(char, color):

        if char == 'R':
            return Rook(color)
        elif char == 'N':
            return Knight(color)
        elif char == 'B':
            return Bishop(color)
        elif char == 'Q':
            return Queen(color)
        elif char == 'K':
            return King(color)
        elif char == 'P':
            return Pawn(color, True)
        elif char == 'E':
            return Empty(color)

        raise Exception('character ', char, ' cannot be used to create a piece')

    @staticmethod
    def build_used_pawn(color):
        return Pawn(color, False)

    @staticmethod
    def build_empty():
        return Empty(Color.NONE)
