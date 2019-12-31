from board.BoardFactory import BoardFactory

from memory.Memory import Memory


class Game:

    def __init__(self, width, length):
        self.__board = BoardFactory.build_board(width, length, BoardFactory.DEFAULT_BOARD)
        self.__memory = Memory()
        self.__turn = 0

    def board_size(self):
        return self.__board.board_size()

    def get_board(self):
        return self.__board
