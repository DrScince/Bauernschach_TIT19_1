""" Pawn figure for the chess game
"""
import sys
try:
    from chess_logik.figure import Figure
    from chess_logik.consts import COLOR_BLACK
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
            color {char}
            position {Position}
        """
        super().__init__(color, position)
        self.__has_done_double_move = None
        self.__possible_moves_buffer = []

    def __get_directional_factor(self):
        """
        Returns:
            -1 {int} -- own color is black
            1 {int} -- own color is white
        """
        if super().get_color() == COLOR_BLACK:
            return -1
        return 1

    def get_double_move(self):
        """ getter
        Returns:
            has_done_double_move {Bool} -- None if no move has been done
        """
        return self.__has_done_double_move

    def get_possible_moves(self, field):
        """ gets all the possible moves of the Pawn
        Return:
            possible_moves {Position[]} -- if there are none the array is empty
        """
        self.__possible_moves_buffer = []
        own_position = super().get_position()
        straight_is_possible = True
        double_straight_is_possible = False
        directional_factor = self.__get_directional_factor()
        if self.__has_done_double_move is None:
            double_straight_is_possible = True
        for figure in field:
            #search for figures in the same column
            fig_pos_num = figure.get_position().get_pos_number()
            fig_pos_cha = figure.get_position().get_pos_char()
            own_pos_num = own_position.get_pos_number()
            own_pos_cha = own_position.get_pos_char()
            if own_pos_num == fig_pos_num:
                if ord(own_pos_cha) - 1 == ord(fig_pos_cha) and figure.get_color() != super().get_color() and figure.get_double_move():
                    self.__possible_moves_buffer.append(Position(fig_pos_cha, fig_pos_num + directional_factor))
                elif ord(own_pos_cha) + 1 == ord(fig_pos_cha) and figure.get_color() != super().get_color() and figure.get_double_move():
                    self.__possible_moves_buffer.append(Position(fig_pos_cha, fig_pos_num + directional_factor))
            #search for figures in the next column
            elif own_pos_num + directional_factor == fig_pos_num:
                if own_pos_cha == fig_pos_cha:
                    straight_is_possible = False
                elif ord(own_pos_cha) - 1 == ord(fig_pos_cha) and figure.get_color() != super().get_color():
                    self.__possible_moves_buffer.append(Position(fig_pos_cha, fig_pos_num))
                elif ord(own_pos_cha) + 1 == ord(fig_pos_cha) and figure.get_color() != super().get_color():
                    self.__possible_moves_buffer.append(Position(fig_pos_cha, fig_pos_num))
            #search for figures in 2 columns
            elif double_straight_is_possible and own_pos_num + (directional_factor * 2) == fig_pos_num and own_pos_cha == fig_pos_cha:
                double_straight_is_possible = False
        if straight_is_possible: #add straight to the possible_moves
            self.__possible_moves_buffer.append(Position(own_pos_cha, own_pos_num + directional_factor))
        if double_straight_is_possible and straight_is_possible: #add double_straight to the possible_moves
            self.__possible_moves_buffer.append(Position(own_pos_cha, own_pos_num + (directional_factor * 2)))
        return self.__possible_moves_buffer

    def do_move(self, new_position):
        """ Does the move to the position if the position is a possible move
        Return:
            The new Field {Figure[]}
        """
        self.__has_done_double_move = False
        old_pos = super().get_position()
        if new_position.get_pos_number() - 2 == old_pos.get_pos_number() or new_position.get_pos_number() + 2 == old_pos.get_pos_number():
            self.__has_done_double_move = True
        for position in self.__possible_moves_buffer:
            if position.get_pos_char() == new_position.get_pos_char():
                if position.get_pos_number() == new_position.get_pos_number():
                    super().do_move(new_position)
                    __possible_moves = None
                    return
        __possible_moves = None
