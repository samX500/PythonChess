from piece.PieceType import PieceType
from piece.Direction import Direction
from piece.KnightDirection import KnightDirection
from piece.Movement import Movement
from piece.Piece import Piece
from Board.Board import Board


class Knight(Piece):

    def __init__(self, color):
        Piece.__init__(self,PieceType.KNIGHT, color, self.__build_movement__())

    def __build_movement__(self):
        movement = []
        for value in KnightDirection:
            movement.append(Movement(value, 1))
        return movement

    def get_legal_move(self, position, board):
        return self.get_legal_move(position, board)