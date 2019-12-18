from board.Board import Board

from memory.Memory import Memory


class Game:

    def __init__(self, boardWidth, boardHeight):
        self.board = Board(boardWidth, boardHeight)
        self.memory = Memory()
        self.turn = 0
