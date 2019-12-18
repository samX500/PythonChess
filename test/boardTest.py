import unittest

from Board.Board import Board
from utility.Position import Position


class MyTestCase(unittest.TestCase):

    def print_list(self, list):
        for position in sorted(list):
            print(position)

    def list_equal(self, list1, list2):
        return sorted(list1) == sorted(list2)

    def test_constructor(self):
        board = Board(8, 8)

    def test_tile_is_empty(self):
        board = Board(8, 8)

        # assert not board.tile_is_empty(Position(0, 0)), 'Tile not empty'
        # assert board.tile_is_empty(Position(0, 2))
        # TODO Assert raise

    def test_get_possible_move(self):
        board = Board(8, 8)

        assert board.get_possible_move(Position(0, 0)) == [], 'Rook no move failed'

        # TODO test for special pawn case
        test_list = [Position(2, 0), Position(2, 1), Position(2, 2),
                     Position(3, 1)]

        assert self.list_equal(board.get_possible_move(Position(1, 1)), test_list), 'pawn move failed'

        test_list = [Position(5, 0), Position(5, 1),
                     Position(5, 2),
                     Position(4, 1)]
        assert self.list_equal(board.get_possible_move(Position(6, 1)), test_list), 'opposite pawn move failed'

        assert sorted(board.get_possible_move(Position(0, 1))) == sorted([Position(2, 0),
                                                                          Position(2, 2)]), 'Knight over moved failed'

        board.move_piece(Position(0, 0), Position(4, 4))

        assert sorted(board.get_possible_move(Position(4, 4))) == sorted(
            [Position(4, 0), Position(4, 1), Position(4, 2),
             Position(4, 3), Position(4, 5), Position(4, 6),
             Position(4, 7),
             Position(2, 4),
             Position(3, 4), Position(5, 4),
             Position(6, 4)]), "Rook all side move failed"

        board.move_piece(Position(0, 1), Position(4, 4))
        board.move_piece(Position(1, 3), Position(2, 3))
        assert sorted(board.get_possible_move(Position(4, 4))) == sorted(
            [Position(2, 5), Position(3, 6), Position(5, 6),
             Position(6, 5), Position(6, 3), Position(5, 2),
             Position(3, 2)]), 'Knight all side move failed'
        board.move_piece(Position(2, 3), Position(1, 3))

        board.move_piece(Position(0, 2), Position(4, 4))
        assert sorted(board.get_possible_move(Position(4, 4))) == sorted(
            [Position(2, 2), Position(3, 3), Position(5, 5),
             Position(6, 6), Position(5, 3), Position(2, 6),
             Position(6, 2), Position(3, 5)
             ]), 'Bishop all side move failed'

        board.move_piece(Position(0, 3), Position(4, 4))
        assert sorted(board.get_possible_move(Position(4, 4))) == sorted(
            [Position(4, 0), Position(4, 1), Position(4, 2),
             Position(4, 3), Position(4, 5), Position(4, 6),
             Position(4, 7),
             Position(2, 4),
             Position(3, 4), Position(5, 4), Position(6, 4),
             Position(2, 2), Position(3, 3), Position(5, 5),
             Position(6, 6),
             Position(2,6),
             Position(3,5),
             Position(5, 3),
             Position(6, 2)]), 'Queen all side move failed'

        board.move_piece(Position(0, 4), Position(4, 4))
        assert sorted(board.get_possible_move(Position(4, 4))) == sorted(
            [Position(3, 3), Position(4, 3), Position(5, 3),
             Position(5, 4), Position(5, 5), Position(4, 5),
             Position(3, 5),
             Position(3, 4)]), 'King all side move failed'


if __name__ == '__main__':
    unittest.main()
