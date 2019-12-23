from enum import Enum


class PieceType(Enum):
    PAWN = 'P'
    ROOK = 'R'
    KNIGHT = 'N'
    BISHOP = 'B'
    QUEEN = 'Q'
    KING = 'K'
    TILE = 'T'

    @staticmethod
    def get_piece_type(char):
        if char == 'P':
            return PieceType.PAWN
        elif char == 'R':
            return PieceType.ROOK
        elif char == 'N':
            return PieceType.KNIGHT
        elif char == 'B':
            return PieceType.BISHOP
        elif char == 'Q':
            return PieceType.QUEEN
        elif char == 'K':
            return PieceType.KING
        elif char == 'T':
            return PieceType.TILES

    def __str__(self):
        return self.name
