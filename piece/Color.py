from enum import Enum


class Color(Enum):
    BLACK = -1
    WHITE = 1
    NONE = 0

    def __str__(self):
        return self.name
