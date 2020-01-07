from board import Board
from piece.Direction import Direction
from piece.Movement import Movement
from piece.Piece import Piece
from piece.PieceType import PieceType
from utility import Position


class Pawn(Piece):
    MOVEMENT = [Movement(Direction.UP, 1), Movement(Direction.UP_RIGHT, 0), Movement(Direction.UP_LEFT, 0)]

    UP_INDEX = 0
    UP_RIGHT_INDEX = 1
    UP_LEFT_INDEX = 2

    def __init__(self, color, is_first_move):
        Piece.__init__(self, PieceType.PAWN, color, self.MOVEMENT)
        self.__is_first_move = is_first_move

    def __reset_movement__(self):
        self.movement[self.UP_INDEX].set_lenght(1)
        self.movement[self.UP_RIGHT_INDEX].set_lenght(0)
        self.movement[self.UP_LEFT_INDEX].set_lenght(0)

    def is_first_move(self):
        return self.__is_first_move

    def move(self):
        self.__is_first_move = False

    def __is_faced(self, position: Position, board: Board):
        test_position = position.clone()
        add = Direction.UP.value[0] * self.get_color().value, Direction.UP.value[1]
        test_position.add(*add)

        return board.is_in_bound(test_position) and not board.get_at_coordinate(
            test_position).get_piece_type() == PieceType.TILE

    def __is_capture(self, position: Position, board: Board, direction: Direction):
        test_position = position.clone()
        add = direction.value[0] * self.get_color().value, direction.value[1]
        test_position.add(*add)
        if board.is_in_bound(test_position):
            piece = board.get_at_coordinate(test_position)
            return not piece.pieceType == PieceType.TILE and not piece.get_color() == self.get_color()
        return False

    def get_legal_move(self, board, position):
        # TODO code special case

        if self.__is_faced(position, board):
            self.movement[self.UP_INDEX].set_lenght(0)
        elif self.__is_first_move:
            self.movement[self.UP_INDEX].set_lenght(2)

        if self.__is_capture(position, board, Direction.UP_LEFT):
            self.movement[self.UP_LEFT_INDEX].set_lenght(1)

        if self.__is_capture(position, board, Direction.UP_RIGHT):
            self.movement[self.UP_RIGHT_INDEX].set_lenght(1)

        legal_move = super().get_legal_move(board, position)

        self.__reset_movement__()

        return legal_move
