""" Position Object to handle the position of a figure
"""
import sys
try:
    from chess_logik.consts import GAME_SIZE
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

        If the Position isn't in the field, the value is ERROR:char or :number
        so the values needs to be proofed
        """
        if number_pos > GAME_SIZE or number_pos < 1:
            number_pos = "ERROR:number"
        if len(char_pos) == 1:
            if ord(char_pos) > GAME_SIZE + 64 or ord(char_pos) < 64:
                char_pos = "ERROR:char"
        else:
            char_pos = "ERROR:char"
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
