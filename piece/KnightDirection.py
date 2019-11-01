from enum import Enum


class KnightDirection(Enum):
    NORTH_EAST = 'northEast'
    EAST_NORTH = 'eastNorth'
    EAST_SOUTH = 'eastSouth'
    SOUTH_EAST = 'southEast'
    SOUTH_WEST = 'southWest'
    WEST_SOUTH = 'westSouth'
    WEST_NORTH = 'westNorth'
    NORTH_WEST = 'northWest'

    def __str__(self):
        return Enum.name
