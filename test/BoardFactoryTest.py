import unittest

from board.BoardFactory import BoardFactory
from piece.Bishop import Bishop
from piece.Color import Color
from piece.King import King
from piece.Knight import Knight
from piece.Queen import Queen
from piece.Rook import Rook


class MyTestCase(unittest.TestCase):

    def test_build_board(self):
        board = BoardFactory.build_board(8, 8, BoardFactory.DEFAULT_BOARD)

        assert board.get_piece_at(0, 0) == Rook(Color.WHITE)
        assert board.get_piece_at(0, 1) == Knight(Color.WHITE)
        assert board.get_piece_at(0, 2) == Bishop(Color.WHITE)
        assert board.get_piece_at(0, 3) == Queen(Color.WHITE)
        assert board.get_piece_at(0, 4) == King(Color.WHITE)
        assert board.get_piece_at(0, 5) == Bishop(Color.WHITE)
        assert board.get_piece_at(0, 6) == Knight(Color.WHITE)
        assert board.get_piece_at(0, 7) == Rook(Color.WHITE)

    if __name__ == '__main__':
        unittest.main()
