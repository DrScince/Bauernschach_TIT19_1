""" Position Object to handle the position of a figure
"""
try:
    from chess_logik.exceptions import OutOfBoundsException
    from chess_logik.consts import GAME_SIZE
    import sys
except ImportError:
    print("ImportError")
    sys.exit()

class Position():
    """ Position Object to handle the position of a figure
    """

    def __init__(self, char_pos, number_pos):
        """
        Arguments:
            char_pos{char} -- A to H
            number_pos{int} -- 1 to 8
        """
        if number_pos > GAME_SIZE or number_pos < 1:
            raise OutOfBoundsException
        if len(char_pos) == 1:
            if ord(char_pos) > GAME_SIZE + 64 or ord(char_pos) < 64:
                raise OutOfBoundsException
        else:
            raise Exception
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
