""" The field wich contains the Pawns
"""
import sys
try:
    from chess_logik.position import Position
    from chess_logik.pawn import Pawn
    from chess_logik.consts import COLOR_BLACK
    from chess_logik.consts import COLOR_WHITE
except ImportError as err:
    print("ImportError"+str(err))
    sys.exit()

class Field():
    """ Contains all the figures in the game and methods to interact
    """

    def __init__(self):
        self.__white_turn = True
        self.__field = []
        for pos_char in "ABCDEFGH":
            self.__field.append(Pawn(COLOR_BLACK, Position(pos_char, 7)))
            self.__field.append(Pawn(COLOR_WHITE, Position(pos_char, 2)))

    def get_possible_moves(self, selected_position):
        """
        Arguments:
            selected_position {Position}
        Returns:
            possible_moves {Position[]}
            Error:1 {int} -- if figure doesn't exist
            Error:2 {int} -- if figure has the wrong color
        """
        assert isinstance(selected_position, Position), "selected_position is not a Position" + str(type(selected_position))
        for figure in self.__field:
            if figure.get_position().get_pos_char() == selected_position.get_pos_char():
                if figure.get_position().get_pos_number() == selected_position.get_pos_number():
                    if (self.__white_turn and figure.get_color() == COLOR_WHITE) or (figure.get_color() == COLOR_BLACK and not self.__white_turn):
                        return figure.get_possible_moves(self.__field)
                    return 2
        return 1

    def get_field(self):
        """ getter
        Return:
            field {Figure[]}
        """
        return self.__field

    def __del_old_figure(self, new_position, own_color):
        """ if an figure gets thrown out, delete it
        Arguments:
            new_position {Position}
        """
        assert isinstance(new_position, Position), "new_position is not a Position" + str(type(new_position))
        assert isinstance(own_color, str), "own_color is not a str" + str(type(own_color))
        assert len(own_color) == 1, "own_color doesn't have the length 1, the length is: " + str(len(own_color))
        for figure in self.__field:
            if figure.get_position().get_pos_char() == new_position.get_pos_char():
                if figure.get_position().get_pos_number() == new_position.get_pos_number():
                    self.__field.remove(figure)
                    return
        for figure in self.__field:
            if figure.get_position().get_pos_char() == new_position.get_pos_char():
                if own_color == COLOR_BLACK:
                    directional_factor = -1
                elif own_color == COLOR_WHITE:
                    directional_factor = 1
                if figure.get_position().get_pos_number() == new_position.get_pos_number() - directional_factor:
                    if figure.get_double_move() and figure.get_color() != own_color:
                        self.__field.remove(figure)

    def do_move(self, selected_position, new_position):
        """Move figure to new position
        Arguments:
            selected_position {Position} -- old position
            new_position {Position} -- new position
        Returns:
            field {Figure[]}
            Error:1 {int} -- if one of the figures doesn't exist
            Error:2 {int} -- if figure has the wrong color
        """
        assert isinstance(selected_position, Position), "selected_position is not a Position" + str(type(selected_position))
        assert isinstance(new_position, Position), "new_position is not a Position" + str(type(new_position))
        for figure in self.__field:
            if figure.get_position().get_pos_char() == selected_position.get_pos_char():
                if figure.get_position().get_pos_number() == selected_position.get_pos_number():
                    if (self.__white_turn and figure.get_color() == COLOR_WHITE) or (figure.get_color() == COLOR_BLACK and not self.__white_turn):
                        self.__del_old_figure(new_position, figure.get_color())
                        figure.do_move(new_position)
                        self.__white_turn = not self.__white_turn
                        return self.get_field()
                    return 2
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
