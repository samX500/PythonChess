from piece.Direction import Direction
from piece.Movement import Movement
from piece.Piece import Piece
from piece.PieceType import PieceType


class Queen(Piece):

    def __init__(self, color):
        Piece.__init__(self, PieceType.QUEEN, color, self.__build_movement())

    @staticmethod
    def __build_movement():
        movement = []
        for value in Direction:
            movement.append(Movement(value, -1))
        return movement

    def get_legal_move(self, position, board):
        return super().get_legal_move(position, board)
