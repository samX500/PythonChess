import pyglet

from game.Game import Game
from gui.DrawChess import DrawChess
from piece.Color import Color
from piece.PieceType import PieceType
from utility.Position import Position


class Gui(pyglet.window.Window):
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    BOARD_SIZE = 8

    WHITE_PIECE_COLOR = (255, 255, 255, 255)
    BLACK_PIECE_COLOR = (0, 0, 0, 255)
    WHITE_TILE_COLOR = (247 / 255, 122 / 255, 255 / 255, 255 / 255)
    BLACK_TILE_COLOR = (122 / 255, 255 / 255, 238 / 255, 255 / 255)

    CAPTURE_PIECE = '▢'
    CAPTURE_SIZE = 80
    CAPTURE_COLOR = (255, 0, 0, 255)

    TILE_SIZE = 50
    PIECE_SIZE = 40

    def __init__(self):
        super().__init__(width=Gui.WINDOW_WIDTH, height=Gui.WINDOW_HEIGHT)
        self.__game = Game(Gui.BOARD_SIZE, Gui.BOARD_SIZE)
        self.__gui = DrawChess(self.__game.board_size(), self.WHITE_PIECE_COLOR, self.BLACK_PIECE_COLOR,
                               self.WHITE_TILE_COLOR, self.BLACK_TILE_COLOR, self.CAPTURE_COLOR, self.TILE_SIZE,
                               self.PIECE_SIZE, self.CAPTURE_PIECE, self.CAPTURE_SIZE,
                               self.width, self.height)
        self.__current_pos = None

    def on_draw(self):
        self.clear()
        self.__gui.draw_board(self.__game.get_board())

        if self.__current_pos is not None:
            possible_move = self.__game.get_board().get_possible_move(Position(*self.__current_pos))
            if possible_move is not None:
                self.__gui.draw_possible_move(possible_move)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        i, j = self.__gui.get_cell_index_from_position(x, y)
        if self.__game.get_board().is_in_bound(Position(i, j)):
            if self.__current_pos is None:
                piece_color = self.__game.get_board().get_at_xy(i, j).get_color()
                current_color = Color.BLACK if self.__game.get_turn() % 2 == 0 else Color.WHITE
                if piece_color == current_color:
                    self.__current_pos = i, j
            else:
                if self.__game.get_board().is_legal_move(Position(self.__current_pos[0], self.__current_pos[1]),
                                                         Position(i, j)):
                    if self.__game.get_board().get_at_xy(*self.__current_pos).get_piece_type() == PieceType.PAWN:
                        self.__game.get_board().get_at_xy(*self.__current_pos).move()

                    self.__game.get_board().move_piece(Position(self.__current_pos[0], self.__current_pos[1]),
                                                       Position(i, j))

                    self.__game.increment_turn()
                self.__current_pos = None


def run():
    window = Gui()
    pyglet.app.run()
