from enum import Enum


class Color(Enum):
    BLACK = 1
    WHITE = -1
    NONE = 0

    def __str__(self):
        return self.name

    @staticmethod
    def get_color(char):
        if char == 'B':
            return Color.BLACK
        if char == 'W':
            return Color.WHITE
        if char == 'N':
            return Color.NONE
