from piece.PieceType import PieceType
from piece.Direction import Direction
from piece.Movement import Movement
from piece.Piece import Piece


class Bishop(Piece):

    def __init__(self, color):
        Piece.__init__(self,PieceType.BISHOP, color, self.__build_movement__())

    def __build_movement__(self):
        return [Movement(Direction.UP_RIGHT, -1), Movement(Direction.UP_LEFT, -1),
                    Movement(Direction.DOWN_RIGHT, -1),
                    Movement(Direction.DOWN_LEFT, -1)]

    def get_legal_move(self, position, board):
        return super().get_legal_move(position, board)