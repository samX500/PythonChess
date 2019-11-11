from enum import Enum


class KnightDirection(Enum):
    NORTH_EAST = [2,1]
    EAST_NORTH = [1,2]
    EAST_SOUTH = [-1,2]
    SOUTH_EAST = [-2,1]
    SOUTH_WEST = [-2,-1]
    WEST_SOUTH = [-1,-2]
    WEST_NORTH = [1,-2]
    NORTH_WEST = [2,-1]

    def __str__(self):
        return Enum.name
