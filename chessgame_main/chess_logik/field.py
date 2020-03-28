""" The field wich contains the Pawns
"""
import sys
try:
    from chess_logik.position import Position
    from chess_logik.pawn import Pawn
    from chess_logik.consts import COLOR_BLACK, COLOR_WHITE
except ImportError as err:
    print("ImportError"+str(err))
    sys.exit()

class Field():
    """ Contains all the figures in the game and methods to interact
    """

    def __init__(self, load_field=None, white_turn=True):
        self.__white_turn = white_turn
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
        Returns:
            possible_moves {Position[]}
            1 {int} -- if figure doesn't exist
        """
        for figure in self.__field:
            if figure.get_position().get_pos_char() == selected_figure.get_pos_char():
                if figure.get_position().get_pos_number() == selected_figure.get_pos_number():
                    return figure.get_possible_moves(self.__field)
        return 1

    def get_field(self):
        """ get the field
        Return:
            field {Figure[]}
        """
        return self.__field

    def __del_old_figure(self, new_position):
        """ delete the old figure if there is one
        Arguments:
            new_position {Position}
        """
        for figure in self.__field:
            if figure.get_position().get_pos_char() == new_position.get_pos_char():
                if figure.get_position().get_pos_number() == new_position.get_pos_number():
                    self.__field.remove(figure)

    def do_move(self, selected_position, new_position):
        """Move figure to new position
        Arguments:
            selected_position {Position} -- old position
            new_position {Position} -- new position
        Returns:
            field {Figure[]}
            1 {int} -- if one of the figures doesn't exist
        """
        for figure in self.__field:
            if figure.get_position().get_pos_char() == selected_position.get_pos_char():
                if figure.get_position().get_pos_number() == selected_position.get_pos_number():
                    self.__del_old_figure(new_position)
                    figure.do_move(new_position)
                    return self.get_field()
        return 1

    def check_win(self):
        """ Check if someone won
        Returns:
            0 {int} -- no winner
            1 {int} -- white won
            2 {int} -- black won
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
