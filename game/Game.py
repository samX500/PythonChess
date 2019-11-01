from Board.Board import Board

from Memory.Memory import Memory


class Game:

    board = None
    memory = None
    turn = 0;

    def __init__(self,boardWidth,boardHeight):
        self.board = Board(boardWidth,boardHeight)
        self.memory = Memory()

