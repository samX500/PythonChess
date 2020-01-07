from board import Board
from piece.Direction import Direction
from piece.Movement import Movement
from piece.Piece import Piece
from piece.PieceType import PieceType
from utility.Position import Position


class King(Piece):

    def __init__(self, color):
        Piece.__init__(self, PieceType.KING, color, self.__build_movement())

    def get_legal_move(self, board: Board, position: Position):
        legal_move = super().get_legal_move(board, position)
        to_remove = []
        for move in legal_move:
            piece = board.get_at_coordinate(move)
            board.move_piece(position, move)
            enemy_move = self.__get_all_enemy_move(board)

            if move in enemy_move:
                to_remove.append(move)

            board.move_piece(move, position)
            board.add_piece(move, piece)

        for move in to_remove:
            legal_move.remove(move)

        return legal_move

    @staticmethod
    def __get_enemy_king_move(board, position):
        king_move = []
        for direction in Direction:
            clone = position.clone()
            clone.add(*direction.value)
            king_move.append(clone)

        return king_move

    def __get_all_enemy_move(self, board: Board):
        size = board.get_size()
        enemy_move = []
        for x in range(size[0]):
            for y in range(size[1]):
                piece = board.get_at_xy(x, y)
                if not piece.get_piece_type() == PieceType.TILE and not piece.get_color() == self.get_color():
                    if piece.get_piece_type() == PieceType.KING:
                        enemy_move += King.__get_enemy_king_move(board, Position(x, y))
                        enemy_move = list(dict.fromkeys(enemy_move))
                    else:
                        enemy_move += piece.get_legal_move(board, Position(x, y))
                        enemy_move = list(dict.fromkeys(enemy_move))

        return enemy_move

    @staticmethod
    def __build_movement():
        movement = []
        for value in Direction:
            movement.append(Movement(value, 1))
        return movement
