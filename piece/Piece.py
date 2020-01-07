from abc import ABC

from board import Board
from utility import Position


class Piece(ABC):

    def __init__(self, piece_type, color, movement):
        self.pieceType = piece_type
        self.color = color
        self.movement = movement

    def get_movement(self):
        return self.movement

    def get_color(self):
        return self.color

    def get_piece_type(self):
        return self.pieceType

    def is_legal_move(self, original_position: Position, new_position: Position, board: Board):
        #TODO test this method
        legal_move = self.get_legal_move(board, original_position)
        if legal_move is None:
            return False
        return new_position in legal_move

    @staticmethod
    def get_legal_move(board : Board, position : Position):
        piece = board.get_at_coordinate(position)
        movement = piece.get_movement()
        possible_move = []

        for move in movement:
            i = 0
            test_position = position.clone()
            while not i == move.get_length():
                to_add = move.get_direction()
                to_add[0] *= piece.get_color().value
                test_position.add(*to_add)
                if board.is_in_bound(test_position):
                    if board.tile_is_empty(test_position):
                        possible_move.append(test_position.clone())
                    else:
                        if board.get_at_coordinate(test_position).get_color() != piece.get_color():
                            possible_move.append(test_position)
                        break
                    i += 1
                else:
                    break

        return possible_move

    def __eq__(self, other):
        return other.isinstance(self) and self.get_color() == other.get_color()

    @property
    def __str__(self):
        return str(self.pieceType)
