from piece.Piece import Piece
from piece.PieceType import PieceType


class Empty(Piece):

    def __init__(self, color):
        super().__init__(PieceType.TILE, color, self.__build_movement())

    def __build_movement(self):
        return None

    def get_legal_move(self, position, board):
        return None
