"""Figure base class for the chess game
"""
import sys
try:
    from chess_logik.consts import COLOR_BLACK
    from chess_logik.consts import COLOR_WHITE
    from chess_logik.consts import ERROR_CODES
    from chess_logik.position import Position
except ImportError as err:
    print("ImportError "+str(err))
    sys.exit()

class Figure:
    """Figure base class for the chess game
    """

    def __init__(self, color, position):
        """
        Arguments:
            color {str} -- COLOR_BLACK or COLOR_WHITE
            position{Position}
        if an error occurs position will be Error:position -> they need to be validated
        """
        assert isinstance(color, str), "color is not a str" + str(type(color))
        assert len(color) == 1, "color doesn't have the length 1, the length is: " + str(len(color))
        assert isinstance(position, Position), "position is not a Position" + str(type(position))
        if color == COLOR_WHITE:
            self.__color = COLOR_WHITE
        elif color == COLOR_BLACK:
            self.__color = COLOR_BLACK
        if position is not None:
            self.__position = position
        else:
            self.__position = "ERROR:position"

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

    def do_move(self, new_position):
        """
        Arguments:
            new_position {Position}
        """
        assert isinstance(new_position, Position), "new_position is not a Position" + str(type(new_position))
        self.__position = new_position
