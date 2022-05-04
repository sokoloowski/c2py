from enum import Enum


class Token(Enum):
    KEYWORD = 1
    IDENTIFIER = 2
    CONSTANT = 3
    OPERATOR = 4
    SPECIAL_CHAR = 5
    STRING = 6
    