"""Consts for figures
"""

GAME_SIZE = 8
GAME_SIZE_MIN = 1
COLOR_WHITE = 'w'
COLOR_BLACK = 'b'

ERROR_CODES = {
    "NoFigure": "Error:FigureDoesn'tExist",
    "WrongColor": "Error:SelectedFigureHasWrongColor",
    "Number": "Error:NumberIsNotInRange",
    "Char": "Error:CharIsNotInRange",
    "NoPosMove": "Error:NotAPossibleMove",
    "NoPosMoves": "Error:NoPossibleMoves",
    "Success": "Success:NothingFailed"
}

WINNER_CODES = {
    "NoWinner": 10,
    "WhiteWon": 11,
    "BlackWon": 12
}

DIRECTIONS = {
    "LEFT": -1,
    "RIGHT": 1,
    "BLACK_MOVE": -1,
    "WHITE_MOVE": 1
}

#Movement
FREE_FIELD = 0
ONE_IN_FRONT = 1
TWO_IN_FRONT = 2
DOUBLE_MOVE = 2
