""" The field wich contains the Pawns
"""
try:
    from pawn import Pawn
    from position import Position
    from consts import COLOR_BLACK, COLOR_WHITE
    import sys
except ImportError:
    print("ImportError")
    sys.exit()

class Field():
    """ Contains all the figures in the game and methods to interact
    """

    def __init__(self, load_field=None):
        if load_field is not None:
            self.__field = load_field
        else:
            self.__field = []
            for pos_char in "ABCDEFGH":
                self.__field.append(Pawn(COLOR_BLACK, Position(pos_char, 7)))
                self.__field.append(Pawn(COLOR_WHITE, Position(pos_char, 2)))

    def get_possible_moves(self, selected_figure):
        """
        Arguments:
            selected_figure {Position}
        """
        for figure in self.__field:
            if figure.get_position().get_pos_char() == selected_figure.get_pos_char():
                if figure.get_position().get_pos_number() == selected_figure.get_pos_number():
                    return figure.get_possible_moves(self.__field)
        raise AttributeError

    def get_field(self):
        """ get the field
        Return:
            field {Figure[]}
        """
        return self.__field

    def do_move(self, selected_figure, new_position):
        """Move figure to new position
        Arguments:
            new_position {Position} -- new position
        """
        for figure in self.__field:
            if figure.get_position().get_pos_char() == selected_figure.get_pos_char():
                if figure.get_position().get_pos_number() == selected_figure.get_pos_number():
                    figure.do_move(new_position)
                    return self.get_field()
        raise AttributeError

    def check_win(self):
        """ Check if someone won
        Returns:
            no winner {int = 0}
            white won {int = 1}
            black won {int = 2}
        """
        for figure in self.__field:
            if figure.get_color() == COLOR_WHITE:
                if figure.get_position.get_pos_number() == 8:
                    return 1
                count_white += 1
            if figure.get_color() == COLOR_BLACK:
                if figure.get_position.get_pos_number() == 1:
                    return 2
                count_black += 1
        if count_white == 0:
            return 2
        if count_black == 0:
            return 1
        return 0
