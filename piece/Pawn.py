from piece.PieceType import PieceType
from piece.Direction import Direction
from piece.Movement import Movement
from piece.Piece import Piece


class Pawn(Piece):
    UP_INDEX = 0
    UP_RIGHT_INDEX = 1
    UP_LEFT_INDEX = 2

    def __init__(self, color,isFirstMove):
        Piece.__init__(self,PieceType.PAWN, color, self.__build_movement__())
        self.isFirstMove = isFirstMove


    def __build_movement__(self):
        return [Movement(Direction.UP, 1), Movement(Direction.UP_RIGHT, 0), Movement(Direction.UP_LEFT, 0)]

    def __reset_movement__(self):
        self.movement[self.UP_INDEX].set_lenght(1)
        self.movement[self.UP_RIGHT_INDEX].set_lenght(0)
        self.movement[self.UP_LEFT_INDEX].set_lenght(0)


    def is_first_move(self):
        return self.isFirstMove

    def __is_capture__(self,position, board,direction):
        test_position = position.clone()
        to_add = direction
        to_add[0] *= self.get_color().value
        test_position.add(*to_add)

        piece = board.get_piece_at(test_position)
        return not piece.pieceType == PieceType.TILE and not piece.get_color() == self.get_color()


    def get_legal_move(self, position, board):
        #TODO code special case
        if self.is_first_move():
            self.movement[self.UP_INDEX].set_lenght(2)

        if self.__is_capture__(position,board,Direction.UP_LEFT):
            self.movement[self.UP_LEFT_INDEX].set_lenght(1)

        if self.__is_capture__(position,board,Direction.UP_RIGHT):
            self.movement[self.UP_RIGHT_INDEX].set_lenght(1)

        legal_move = super().get_legal_move(position,board)

        self.__reset_movement__()

        return legal_move