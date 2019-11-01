from enum import Enum

class Color(Enum):
    BLACK = 0
    WHITE = 1
    NONE = 2

    def __str__(self):
        return Enum.name