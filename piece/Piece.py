from piece.PieceType import PieceType


class Piece:

    def __init__(self, piece_type, color):
        self.pieceType = piece_type
        self.color = color
        self.movement = PieceType.get_piece_move(piece_type)

    def get_movement(self):
        return self.movement

    def get_color(self):
        return self.color

    @property
    def __str__(self):
        return str(self.pieceType)
