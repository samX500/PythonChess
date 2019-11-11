from enum import Enum

from piece.Direction import Direction
from piece.KnightDirection import KnightDirection
from piece.Movement import Movement


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

    @staticmethod
    def get_piece_move(piece):
        if piece == PieceType.PAWN:
            return [Movement(Direction.NORTH, 2), Movement(Direction.NORTH_EAST, 1),
                    Movement(Direction.NORTH_WEST, 1)]
        elif piece == PieceType.ROOK:
            return [Movement(Direction.NORTH, -1), Movement(Direction.EAST, -1), Movement(Direction.SOUTH, -1),
                    Movement(Direction.WEST, -1)]
        elif piece == PieceType.KNIGHT:
            movement = []
            for value in KnightDirection:
                movement.append(Movement(value, -1))
            return movement
        elif piece == PieceType.BISHOP:
            return [Movement(Direction.NORTH_EAST, -1), Movement(Direction.NORTH_WEST, -1),
                    Movement(Direction.SOUTH_EAST, -1),
                    Movement(Direction.SOUTH_WEST, -1)]
        elif piece == PieceType.QUEEN:
            movement = []
            for value in Direction:
                movement.append(Movement(value, -1))
            return movement
        elif piece == PieceType.KING:
            movement = []
            for value in Direction:
                movement.append(Movement(value, 1))
            return movement

    def __str__(self):
        return self.name
