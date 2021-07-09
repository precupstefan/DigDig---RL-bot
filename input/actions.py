from enum import Enum


class DIRECTION(Enum):
    N = 1
    NE = 2
    E = 3
    SE = 4
    S = 5
    SW = 6
    W = 7
    NW = 8


class ABILITY(Enum):
    NONE = 0
    HEAL = 1
    RUN = 2
