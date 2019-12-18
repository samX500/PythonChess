from piece.PieceType import PieceType
from piece.Piece import Piece




class Empty(Piece):

    def __init__(self, color):
        Piece.__init__(self,PieceType.TILE, color, self.__build_movement__())

    def __build_movement__(self):
        return None

    def get_legal_move(self, position, board):
        return None
