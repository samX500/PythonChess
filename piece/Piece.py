from piece.PieceType import PieceType


class Piece:

    def __init__(self, piece_type, color,movement):
        self.pieceType = piece_type
        self.color = color
        self.movement = movement

    def build_movement(self):
        pass

    def get_movement(self):
        return self.movement

    def get_color(self):
        return self.color


    def get_legal_move(self,board,position):
        # TODO make special case for pawn
        piece = board.pieces[position.get_x()][position.get_y()]
        movement = piece.get_movement()
        possible_move = []

        for move in movement:
            i = 0
            test_position = position.clone()
            while not i == move.get_length():
                to_add = move.get_direction()
                to_add[0] *= piece.get_color().value
                test_position.add(*to_add)
                if board.is_in_bound(test_position):
                    if board.tile_is_empty(test_position):
                        possible_move.append(test_position.clone())
                    else:
                        if board.get_piece_at(test_position).get_color() != piece.get_color():
                            possible_move.append(test_position)
                        break
                    i += 1
                else:
                    break

        return possible_move

    @property
    def __str__(self):
        return str(self.pieceType)
