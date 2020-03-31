""" Pawn figure for the chess game
"""
import sys
try:
    from chess_logik.figure import Figure
    from chess_logik.consts import COLOR_BLACK
    from chess_logik.consts import DIRECTION_BLACK
    from chess_logik.consts import DIRECTION_WHITE
    from chess_logik.position import Position
except ImportError as err:
    print("ImportError"+str(err))
    sys.exit()

class Pawn(Figure):
    """ Pawn figure for the chess game
    """

    def __init__(self, color, position):
        """
        Arguments:
            color {str}
            position {Position}
        """
        super().__init__(color, position)
        self.__has_done_double_move = None
        self.__possible_moves_buffer = []

    def __get_directional_factor(self):
        """
        Returns:
            DIRECTION_BLACK {int} -- own color is black
            DIRECTION_WHITE {int} -- own color is white
        """
        if super().get_color() == COLOR_BLACK:
            return DIRECTION_BLACK
        return DIRECTION_WHITE

    def get_double_move(self):
        """ getter
        Returns:
            has_done_double_move {bool} -- None if no move has been done
        """
        return self.__has_done_double_move

    def get_possible_moves(self, field):
        """ gets all the possible moves of the Pawn
        Arguments:
            field {Figure[]}
        Return:
            possible_moves {Position[]} -- if there are none the array is empty
        """
        assert isinstance(field, list), "field ist kein []" + str(type(field))
        self.__possible_moves_buffer = []
        own_position = super().get_position()
        straight_is_possible = True
        double_straight_is_possible = False
        dir_factor = self.__get_directional_factor()
        if self.__has_done_double_move is None:
            double_straight_is_possible = True
        for figure in field:
            assert isinstance(figure, Figure), "field ist kein Figure[]" + str(type(figure))
            fig_pos_num = figure.get_position().get_pos_number()
            fig_pos_cha = ord(figure.get_position().get_pos_char())
            own_pos_num = own_position.get_pos_number()
            own_pos_cha = ord(own_position.get_pos_char())
            different_col = figure.get_color() != super().get_color()
            if own_pos_num == fig_pos_num:
                if  fig_pos_cha in (own_pos_cha + 1, own_pos_cha - 1):
                    if different_col and figure.get_double_move():
                        self.__possible_moves_buffer.append(Position(chr(fig_pos_cha), fig_pos_num + dir_factor))
            elif own_pos_num + dir_factor == fig_pos_num:
                if own_pos_cha == fig_pos_cha:
                    straight_is_possible = False
                elif fig_pos_cha in (own_pos_cha + 1, own_pos_cha - 1):
                    if different_col:
                        self.__possible_moves_buffer.append(Position(chr(fig_pos_cha), fig_pos_num))
            elif own_pos_num + (dir_factor * 2) == fig_pos_num and own_pos_cha == fig_pos_cha:
                double_straight_is_possible = False
        if straight_is_possible:
            self.__possible_moves_buffer.append(Position(chr(own_pos_cha), own_pos_num + dir_factor))
        if double_straight_is_possible and straight_is_possible:
            self.__possible_moves_buffer.append(Position(chr(own_pos_cha), own_pos_num + (dir_factor * 2)))
        return self.__possible_moves_buffer

    def do_move(self, new_position):
        """ Does the move to the position if the position is a possible move
        Arguments:
            new_position {Position}
        Return:
            The new Field {Figure[]}
        """
        assert isinstance(new_position, Position), "new_position ist keine Position" + str(type(new_position))
        old_pos_num = super().get_position().get_pos_number
        if old_pos_num in (new_position.get_pos_number() - 2, new_position.get_pos_number() + 2):
            self.__has_done_double_move = True
        for position in self.__possible_moves_buffer:
            if position.get_pos_char() == new_position.get_pos_char():
                if position.get_pos_number() == new_position.get_pos_number():
                    super().do_move(new_position)
                    self.__has_done_double_move = False
                    __possible_moves = None
                    return
        __possible_moves = None
