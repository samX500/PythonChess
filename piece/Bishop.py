from piece.Direction import Direction
from piece.Movement import Movement
from piece.Piece import Piece
from piece.PieceType import PieceType


class Bishop(Piece):

    MOVEMENT = [Movement(Direction.UP_RIGHT, -1), Movement(Direction.UP_LEFT, -1),
                Movement(Direction.DOWN_RIGHT, -1),
                Movement(Direction.DOWN_LEFT, -1)]

    def __init__(self, color):
        Piece.__init__(self, PieceType.BISHOP, color, self.MOVEMENT)
