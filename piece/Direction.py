from enum import Enum


class Direction(Enum):
    NORTH = 'north'
    NORTH_EAST = 'northEast'
    EAST = 'east'
    SOUTH_EAST = 'southEast'
    SOUTH = 'south'
    SOUTH_WEST = 'southWest'
    WEST = 'west'
    NORTH_WEST = 'northWest'
    NONE = 'none'

    def __str__(self):
        return Enum.name