import pyglet

from game.Game import Game
from gui.DrawChess import DrawChess


class Gui(pyglet.window.Window):
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    BOARD_SIZE = 8

    WHITE_PIECE_COLOR = (255, 255, 255, 255)
    BLACK_PIECE_COLOR = (0, 0, 0, 255)
    WHITE_TILE_COLOR = (247, 122, 255, 255)
    BLACK_TILE_COLOR = (122, 255, 238, 255)

    TILE_SIZE = 50
    PIECE_SIZE = 40

    def __init__(self):
        super().__init__(width=Gui.WINDOW_WIDTH, height=Gui.WINDOW_HEIGHT)
        self.__game = Game(Gui.BOARD_SIZE, Gui.BOARD_SIZE)
        self.__gui = DrawChess(self.__game.board_size(), self.WHITE_PIECE_COLOR, self.BLACK_PIECE_COLOR,
                               self.WHITE_TILE_COLOR, self.BLACK_TILE_COLOR, self.TILE_SIZE, self.PIECE_SIZE,
                               self.width, self.height)

    def on_draw(self):
        self.clear()
        self.__gui.draw_board(self.__game.get_board())
        print(self.__game.get_board().__str__())

def run():
    window = Gui()
    pyglet.app.run()
