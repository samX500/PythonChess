from piece.KnightDirection import KnightDirection
from piece.Movement import Movement
from piece.Piece import Piece
from piece.PieceType import PieceType


class Knight(Piece):

    def __init__(self, color):
        Piece.__init__(self, PieceType.KNIGHT, color, self.__build_movement())

    @staticmethod
    def __build_movement():
        movement = []
        for value in KnightDirection:
            movement.append(Movement(value, 1))
        return movement
