"""Consts for figures
"""

GAME_SIZE = 8
COLOR_WHITE = 'w'
COLOR_BLACK = 'b'

#Direction
DIRECTION_BLACK = -1
DIRECTION_WHITE = 1

ERROR_CODES = {
    "Null": "Error:Null",
    "NoFigure": "Error:FigureDoesn'tExist",
    "WrongColor": "Error:SelectedFigureHasWrongColor",
    "Number": "Error:NumberIsNotInRange",
    "Char": "Error:CharIsNotInRange"
}

LEFT = -1
RIGHT = 1

#Movement
DOUBLE_MOVE = 2
FREE_FIELD = 0
ONE_IN_FRONT = 1
TWO_IN_FRONT = 2

#ERRORCODE
SUCCESSFULL = 0
NO_POSSIBLE_MOVE = 1
