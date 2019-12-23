from board.BoardFactory import BoardFactory

from memory.Memory import Memory


class Game:

    def __init__(self, width, length):
        self.board = BoardFactory.build_board(width, length, BoardFactory.DEFAULT_BOARD)
        self.memory = Memory()
        self.turn = 0
