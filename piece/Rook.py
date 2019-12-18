from piece.PieceType import PieceType
from piece.Direction import Direction
from piece.Movement import Movement
from piece.Piece import Piece


class Rook(Piece):

    def __init__(self, color):
        Piece.__init__(self,PieceType.ROOK, color, self.__build_movement__())

    def __build_movement__(self):
        return [Movement(Direction.UP, -1), Movement(Direction.RIGHT, -1), Movement(Direction.DOWN, -1),
                Movement(Direction.LEFT, -1)]

    def get_legal_move(self, position, board):
        return super().get_legal_move(position, board)