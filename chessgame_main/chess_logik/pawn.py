""" Pawn figure for the chess game
"""
try:
    from chess_logik.figure import Figure
    from chess_logik.consts import COLOR_WHITE, COLOR_BLACK
    from chess_logik.position import Position
    import sys
except ImportError:
    print("ImportError")
    sys.exit()

class Pawn(Figure):
    """ Pawn figure for the chess game
    """

    def __init__(self, color, position):
        super().__init__(color, position)
        self.__has_done_double_move = None
        self.__possible_moves_buffer = []

    def __get_double_move(self):
        return self.__has_done_double_move

    def __get_possible_moves_black(self, field):
        own_position = super().get_position()
        straight_is_possible = True
        if self.__has_done_double_move is None:
            double_straight_is_possible = True
        for figure in field:
            if own_position.get_pos_number() - 1 == figure.get_position().get_pos_number():
                if own_position.get_pos_char() == figure.get_position().get_pos_char:
                    straight_is_possible = False
                if ord(own_position.get_pos_char()) - 1 == ord(figure.get_position().get_pos_char) and figure.get_color() == COLOR_WHITE:
                    self.__possible_moves_buffer.append(Position(chr(own_position.get_pos_char() - 1), own_position.get_pos_number() - 1))
                if ord(own_position.get_pos_char()) + 1 == ord(figure.get_position().get_pos_char) and figure.get_color() == COLOR_WHITE:
                    self.__possible_moves_buffer.append(Position(chr(own_position.get_pos_char() + 1), own_position.get_pos_number() - 1))
            if double_straight_is_possible and own_position.get_pos_number() - 2 == figure.get_position().get_pos_number():
                if own_position.get_pos_char() == figure.get_position().get_pos_char:
                    double_straight_is_possible = False
        if straight_is_possible:
            self.__possible_moves_buffer.append(Position(own_position.get_pos_char(), own_position.get_pos_number() - 1))
        if double_straight_is_possible and straight_is_possible:
            self.__possible_moves_buffer.append(Position(own_position.get_pos_char(), own_position.get_pos_number() - 2))
        return self.__possible_moves_buffer

    def __get_possible_moves_white(self, field):
        own_position = super().get_position()
        straight_is_possible = True
        if self.__has_done_double_move is None:
            double_straight_is_possible = True
        for figure in field:
            if own_position.get_pos_number() + 1 == figure.get_position().get_pos_number():
                if own_position.get_pos_char() == figure.get_position().get_pos_char:
                    straight_is_possible = False
                if ord(own_position.get_pos_char()) - 1 == ord(figure.get_position().get_pos_char) and figure.get_color() == COLOR_WHITE:
                    self.__possible_moves_buffer.append(Position(chr(own_position.get_pos_char() - 1), own_position.get_pos_number() + 1))
                if ord(own_position.get_pos_char()) + 1 == ord(figure.get_position().get_pos_char) and figure.get_color() == COLOR_WHITE:
                    self.__possible_moves_buffer.append(Position(chr(own_position.get_pos_char() + 1), own_position.get_pos_number() + 1))
            if double_straight_is_possible and own_position.get_pos_number() + 2 == figure.get_position().get_pos_number():
                if own_position.get_pos_char() == figure.get_position().get_pos_char:
                    double_straight_is_possible = False
        if straight_is_possible:
            self.__possible_moves_buffer.append(Position(own_position.get_pos_char(), own_position.get_pos_number() + 1))
        if double_straight_is_possible and straight_is_possible:
            self.__possible_moves_buffer.append(Position(own_position.get_pos_char(), own_position.get_pos_number() + 2))
        return self.__possible_moves_buffer

    def get_possible_moves(self, field):
        """ gets all the possible moves of the Pawn
        Return:
            possible_moves {Position[]}
        """
        self.__possible_moves_buffer = []
        if super().get_color() == COLOR_BLACK:
            self.__possible_moves_buffer = self.__get_possible_moves_black(field)
        elif super().get_color() == COLOR_WHITE:
            self.__possible_moves_buffer = self.__get_possible_moves_white(field)
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
                if position.get_pos_number() == new_position.get_pos_number()
                    super()._do_move(new_position)
                    __possible_moves = None
                    return
        __possible_moves = None
