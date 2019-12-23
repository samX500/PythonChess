from piece.Direction import Direction
from piece.Movement import Movement
from piece.Piece import Piece
from piece.PieceType import PieceType


class King(Piece):

    def __init__(self, color):
        Piece.__init__(self, PieceType.KING, color, self.__build_movement())

    @staticmethod
    def __build_movement():
        movement = []
        for value in Direction:
            movement.append(Movement(value, 1))
        return movement
