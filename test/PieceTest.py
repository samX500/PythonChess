import unittest

from board.BoardFactory import BoardFactory
from utility.Position import Position


class PieceTest(unittest.TestCase):

    @staticmethod
    def print_list(list):
        for position in sorted(list):
            print(position)

    def test_get_legal_move(self):
        board = BoardFactory.build_board(8, 8, BoardFactory.DEFAULT_BOARD)

        assert board.get_possible_move(Position(0, 0)) == [], 'Rook no move failed'

        # TODO test for special pawn case

        print(board)
        assert sorted(board.get_possible_move(Position(1, 1))) == sorted([Position(2, 1),
                                                                          Position(3, 1)]), 'pawn first move failed'

        assert sorted(board.get_possible_move(Position(6, 1))) == sorted([Position(5, 1),
                                                                          Position(4,
                                                                                   1)]), 'opposite pawn first move failed'

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

        PieceTest.print_list(sorted(board.get_possible_move(Position(4, 4))))
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
             Position(2, 6),
             Position(3, 5),
             Position(5, 3),
             Position(6, 2)]), 'Queen all side move failed'

        board.move_piece(Position(0, 4), Position(4, 4))
        assert sorted(board.get_possible_move(Position(4, 4))) == sorted(
            [Position(3, 3), Position(4, 3), Position(5, 3),
             Position(5, 4), Position(5, 5), Position(4, 5),
             Position(3, 5),
             Position(3, 4)]), 'King all side move failed'

        board.move_piece(Position(1, 1), Position(5, 1))
        assert sorted(board.get_possible_move(Position(5, 1))) == sorted(
            [Position(6, 1), Position(6, 2), Position(6, 0)]), 'Pawn capture failed'

        board.move_piece(Position(6, 5), Position(2, 5))
        assert sorted(board.get_possible_move(Position(2, 5))) == sorted(
            [Position(1, 5), Position(1, 4), Position(1, 6)]), 'Pawn capture failed'


if __name__ == '__main__':
    unittest.main()
