"""Figure base class for the chess game
"""
try:
    from chess_logik.consts import COLOR_BLACK, COLOR_WHITE
    import sys
except ImportError:
    print("ImportError")
    sys.exit()

class Figure:
    """Figure base class for the chess game
    """

    def __init__(self, color, position):
        """
        Arguments:
            color {String} -- COLOR_BLACK or COLOR_WHITE
            position{Position}
        """
        if color == COLOR_WHITE:
            self.__color = COLOR_WHITE
        elif color == COLOR_BLACK:
            self.__color = COLOR_BLACK
        else:
            raise AttributeError

        if position is not None:
            self.__position = position
        else:
            raise AttributeError

    def get_color(self):
        """ Gets the color of the Figure
        Return:
            COLOR_BLACK or COLOR_WHITE
        """
        return self.__color

    def get_position(self):
        """ Gets the position of the Figure

        Return:
            position {Position}
        """
        return self.__position

    def _do_move(self, new_position):
        self.__position = new_position
