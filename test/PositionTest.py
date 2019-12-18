import unittest

from Board.Board import Board
from utility.Position import Position


class MyTestCase(unittest.TestCase):

    def test_lt(self):
        position1 = Position(0, 0)
        position2 = Position(1, 0)
        position3 = Position(0, 1)
        position4 = Position(1, 1)

        assert not position1.__lt__(position1)
        assert position1.__lt__(position2)
        assert position1.__lt__(position3)
        assert position1.__lt__(position4)

        assert not position2.__lt__(position1)
        assert not position2.__lt__(position2)
        assert not position2.__lt__(position3)
        assert position2.__lt__(position4)

        assert not position3.__lt__(position1)
        assert position3.__lt__(position2)
        assert not position3.__lt__(position3)
        assert position3.__lt__(position4)

        assert not position4.__lt__(position1)
        assert not position4.__lt__(position2)
        assert not position4.__lt__(position3)
        assert not position4.__lt__(position4)

    def test_eq(self):
        position1 = Position(0, 0)
        position2 = Position(1, 0)
        position3 = Position(0, 1)
        position4 = Position(1, 1)

        assert position1.__eq__(position1)
        assert not position1.__eq__(position2)
        assert not position1.__eq__(position3)
        assert not position1.__eq__(position4)

        assert not position2.__eq__(position1)
        assert position2.__eq__(position2)
        assert not position2.__eq__(position3)
        assert not position2.__eq__(position4)

        assert not position3.__eq__(position1)
        assert not position3.__eq__(position2)
        assert position3.__eq__(position3)
        assert not position3.__eq__(position4)

        assert not position4.__eq__(position1)
        assert not position4.__eq__(position2)
        assert not position4.__eq__(position3)
        assert position4.__eq__(position4)



if __name__ == '__main__':
    unittest.main()
