from enum import Enum


class Direction(Enum):
    NORTH = [1, 0]
    NORTH_EAST = [1, 1]
    EAST = [0, 1]
    SOUTH_EAST = [-1, 1]
    SOUTH = [-1, 0]
    SOUTH_WEST = [-1, -1]
    WEST = [0, -1]
    NORTH_WEST = [1, -1]
    NONE = [0, 0]

    def __str__(self):
        return self.name
