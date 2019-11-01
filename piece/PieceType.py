from enum import Enum

from piece.Direction import Direction
from piece.KnightDirection import KnightDirection


class PieceType(Enum):
    PAWN = [Direction.NORTH, Direction.NORTH_EAST, Direction.NORTH_WEST]
    ROOK = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
    KNIGHT = [direction.value for direction in KnightDirection]
    BISHOP = [Direction.NORTH_EAST, Direction.SOUTH_EAST, Direction.SOUTH_WEST, Direction.NORTH_WEST]
    QUEEN = [direction.value for direction in Direction]
    KING = [direction.value for direction in Direction]
    TILE = [Direction.NONE]

    def getPieceType(self, char):
        if char == 'P':
            return self.PAWN
        elif char == 'R':
            return self.ROOK
        elif char == 'N':
            return self.KNIGHT
        elif char == 'B':
            return self.BISHOP
        elif char == 'Q':
            return self.QUEEN
        elif char == 'K':
            return self.KNIGHT
        elif char == 'T':
            return self.TILES

    def __str__(self):
        return Enum.name