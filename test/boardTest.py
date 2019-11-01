import unittest

from Board.Board import Board


class MyTestCase(unittest.TestCase):
    pass


def contructorTest():
    board = Board(8, 8)
    print(board)


if __name__ == '__main__':
    unittest.main()
