from board.Board import Board
from piece.Color import Color
from piece.PieceFactory import PieceFactory
from utility.Position import Position


class BoardFactory:
    DEFAULT_BOARD = ['WR,WN,WB,WQ,WK,WB,WN,WR', 'WP,WP,WP,WP,WP,WP,WP,WP', 'NE,NE,NE,NE,NE,NE,NE,NE',
                     'NE,NE,NE,NE,NE,NE,NE,NE', 'NE,NE,NE,NE,NE,NE,NE,NE', 'NE,NE,NE,NE,NE,NE,NE,NE',
                     'BP,BP,BP,BP,BP,BP,BP,BP', 'BR,BN,BB,BK,BQ,BB,BN,BR']

    @staticmethod
    def build_board(length, width, content):
        board = Board(length, width)
        current_line = 0
        current_row = 0
        for line in content:
            pieces = line.split(',')
            for piece in pieces:
                color = Color.get_color(piece[0])

                # TODO hardcoded
                if len(piece) == 3:
                    board.add_piece(Position(current_line, current_row), PieceFactory.build_used_pawn(color))
                else:
                    board.add_piece(Position(current_line, current_row), PieceFactory.build_piece(piece[1], color))

                current_row += 1
            current_row = 0
            current_line += 1
        return board
