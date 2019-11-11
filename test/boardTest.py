import unittest

from Board.Board import Board
from utility.Position import Position


class MyTestCase(unittest.TestCase):

    def test_constructor(self):
        board = Board(8, 8)

    def test_get_possible_move(self):
        board = Board(8, 8)

        assert board.get_possible_move(Position(0, 0)) == [], 'Rook no move failed'

        # TODO test for special pawn case
        assert board.get_possible_move(Position(1, 1)) == [(2, 0), (2, 1), (2, 2), (3, 1)], 'pawn move failed'

        assert board.get_possible_move(Position(6, 1)) == [(5, 0), (5, 1), (5, 2)], 'opposite pawn move failed'

        assert board.get_possible_move(Position(0, 1)) == [(0, 2), (2, 2)], 'Knight over moved failed'

        board.move_piece(Position(0, 0), Position(4, 4))
        assert board.get_possible_move(Position(4, 4)) == [(0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4),
                                                           (4, 2),
                                                           (4, 3), (4, 5), (4, 6)], "Rook all side move failed"

        board.move_piece(Position(0, 1), Position(4, 4))
        board.move_piece(Position(1, 3), Position(2, 3))
        assert board.get_possible_move(Position(4, 4)) == [(2, 5), (3, 6), (5, 6), (6, 5), (6, 3), (5, 2),
                                                           (3, 2)], 'Knight all side move failed'
        board.move_piece(Position(2, 3), Position(1, 3))

        board.move_piece(Position(0, 2), Position(4, 4))
        assert board.get_possible_move(Position(4, 4)) == [(2, 2), (3, 3), (5, 5), (6, 6), (3, 5), (2, 6), (3, 6),
                                                           (2, 7)], 'Bishop all side move failed'

        board.move_piece(Position(0, 3), Position(4, 4))
        assert board.get_possible_move(Position(4, 4)) == [(0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4),
                                                           (4, 2),
                                                           (4, 3), (4, 5), (4, 6), (2, 2), (3, 3), (5, 5), (6, 6),
                                                           (3, 5),
                                                           (2, 6), (3, 6),
                                                           (2, 7)], 'Queen all side move failed'
        board.move_piece((Position(0, 4), Position(4, 4)))
        assert board.get_possible_move(Position(4, 4)) == [(3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3),
                                                           (4, 3)], 'King all side move failed'


if __name__ == '__main__':
    unittest.main()
