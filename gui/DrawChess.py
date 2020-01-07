import pyglet
import pyglet.gl as gl

from board.Board import Board
from piece.Bishop import Bishop
from piece.Color import Color
from piece.Empty import Empty
from piece.King import King
from piece.Knight import Knight
from piece.Pawn import Pawn
from piece.Piece import Piece
from piece.Queen import Queen
from piece.Rook import Rook


class DrawChess:
    def __init__(self, board_size: (int, int), white_piece_color: (int, int, int, int),
                 black_piece_color: (int, int, int, int), white_tile_color: (int, int, int, int),
                 black_tile_color: (int, int, int, int), capture_color: (int, int, int, int), tile_size: int,
                 piece_size: int, capture_piece: str, capture_size: int, width: int, height: int):
        self.__board_size = board_size
        self.__white_piece_color = white_piece_color
        self.__black_piece_color = black_piece_color
        self.__white_tile_color = white_tile_color
        self.__black_tile_color = black_tile_color
        self.__capture_color = capture_color
        self.__tile_size = tile_size
        self.__half_tile_size = tile_size / 2
        self.__piece_size = piece_size
        self.__capture_piece = capture_piece
        self.__capture_size = capture_size
        self.__width = width
        self.__height = height

        self.__w, self.__h = self.__board_size
        self.__transform = self.__width / 2 - self.__w / 2 * self.__tile_size, \
                           self.__height / 2 - self.__h / 2 * self.__tile_size, \
                           0

    def get_cell_index_from_position(self, x: int, y: int):
        x, y = x - self.__transform[0], y - self.__transform[1]
        return int(y // self.__tile_size), int(x // self.__tile_size)

    def draw_board(self, board: Board):
        gl.glPushMatrix()
        gl.glTranslatef(*self.__transform)

        for x in range(self.__w):
            for y in range(self.__h):
                gl.glPushMatrix()
                gl.glTranslatef(y * self.__tile_size, x * self.__tile_size, 0)
                tile_color = self.__white_tile_color if (x + y) % 2 == 0 else self.__black_tile_color
                self.__draw_tile(tile_color)
                self.__draw_piece(board, y, x)
                gl.glPopMatrix()
        gl.glPopMatrix()

    def __draw_tile(self, tile_color: (int, int, int, int)):
        gl.glColor4f(*tile_color)

        gl.glBegin(gl.GL_QUADS)
        gl.glVertex2d(0, 0)
        gl.glVertex2d(self.__tile_size, 0)
        gl.glVertex2d(self.__tile_size, self.__tile_size)
        gl.glVertex2d(0, self.__tile_size)
        gl.glEnd()

    def __draw_piece(self, board: Board, x: int, y: int):
        piece = board.get_at_xy(y, x)
        if isinstance(piece, Empty):
            return
        str_piece = self.__show_piece(piece)
        piece_color = self.__white_piece_color if piece.get_color() == Color.WHITE else self.__black_piece_color
        self.__draw_label(piece_color, str_piece, self.__half_tile_size, self.__half_tile_size, self.__piece_size)

    def draw_possible_move(self, possible_move):
        gl.glPushMatrix()
        gl.glTranslatef(*self.__transform)

        for pos in possible_move:
            gl.glPushMatrix()
            gl.glTranslatef(pos.get_y() * self.__tile_size, pos.get_x() * self.__tile_size, 0)
            self.__draw_label(self.__capture_color, self.__capture_piece, self.__half_tile_size,self.__half_tile_size, self.__capture_size)
            gl.glPopMatrix()
        gl.glPopMatrix()

    @staticmethod
    def __show_piece(piece: Piece):
        if isinstance(piece, Bishop):
            return '♗'
        elif isinstance(piece, King):
            return '♔'
        elif isinstance(piece, Knight):
            return '♘'
        elif isinstance(piece, Pawn):
            return '♙'
        elif isinstance(piece, Queen):
            return '♕'
        elif isinstance(piece, Rook):
            return '♖'

    def __draw_label(self, piece_color: (int, int, int, int), string: str, x: float, y: float, font_size: float):
        label = pyglet.text.Label(string, font_size=font_size, color=piece_color, x=int(x), y=int(y), anchor_x='center',
                                  anchor_y='center')
        label.draw()
