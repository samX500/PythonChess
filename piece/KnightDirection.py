from enum import Enum


class KnightDirection(Enum):
    UP_RIGHT = [-2, 1]
    RIGHT_UP = [-1, 2]
    RIGHT_DOWN = [1, 2]
    DOWN_RIGHT = [2, 1]
    DOWN_LEFT = [2, -1]
    LEFT_DOWN = [1, -2]
    LEFT_UP = [-1, -2]
    UP_LEFT = [-2, -1]

    def __str__(self):
        return Enum.name
