class Piece:

    #TODO check how class variable work
    pieceType = None
    color = None
    directions = []

    def __init__(self, pieceType, color):
        self.pieceType = pieceType
        self.color = color
        self.directions = pieceType.value

    def __str__(self):
        return self.pieceType.__str__() + '  '+self.color.__str__()
