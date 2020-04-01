""" Position Object to handle the position of a figure
"""
import sys
try:
    from chess_logik import consts
except ImportError as err:
    print("ImportError"+str(err))
    sys.exit()

class Position():
    """ Position Object to handle the position of a figure
    """

    def __init__(self, char_pos, number_pos):
        """
        Arguments:
            char_pos{str} -- A to H -- switches to ERROR_CODES["OutOfBounds"] if OutOfBounds
            number_pos{int} -- 1 to 8 -- switches to ERROR_CODES["OutOfBounds"] if OutOfBounds
        """
        assert isinstance(char_pos, str), "char_pos is not a str" + str(type(char_pos))
        assert isinstance(number_pos, int), "number_pos is not a int" + str(type(number_pos))
        assert len(char_pos) == 1, "char_pos doesn't have the length 1, the length is: " + str(len(char_pos))
        if number_pos > consts.GAME_SIZE or number_pos < 1:
            number_pos = consts.ERROR_CODES["OutOfBounds"]
        if ord(char_pos) > consts.GAME_SIZE + 64 or ord(char_pos) < 64:
            char_pos = consts.ERROR_CODES["OutOfBounds"]
        self.pos_number = number_pos
        self.pos_char = char_pos

    def get_pos_number(self):
        """
        Return: the number part of the position
        """
        return self.pos_number

    def get_pos_char(self):
        """
        Return: the char part of the position
        """
        return self.pos_char
