import unittest

from board.Board import Board


class MyTestCase(unittest.TestCase):

    def print_list(self, list):
        for position in sorted(list):
            print(position)

    def list_equal(self, list1, list2):
        return sorted(list1) == sorted(list2)

    def test_constructor(self):
        board = Board(8, 8)

    def test_tile_is_empty(self):
        # assert not board.tile_is_empty(Position(0, 0)), 'Tile not empty'
        # assert board.tile_is_empty(Position(0, 2))
        # TODO Assert raise
        board = Board(8, 8)


if __name__ == '__main__':
    unittest.main()
