""" Pawn figure for the chess game
"""
import sys
try:
    from chess_logik.position import Position
    from chess_logik.figure import Figure
    from chess_logik import consts
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

    def __get_move_direction(self):
        """Returns the direction of the figure
        Returns:
            DIRECTIONS["BLACK_MOVE"] {int} -- own color is black
            DIRECTIONS["WHITE_MOVE"] {int} -- own color is white
        """
        if super().get_color() == consts.COLOR_BLACK:
            return consts.DIRECTIONS["BLACK_MOVE"]
        return consts.DIRECTIONS["WHITE_MOVE"]

    def get_double_move(self):
        """ Returns if the figure has done a double move
        Returns:
            has_done_double_move {bool} -- None if no move has been done
        """
        return self.__has_done_double_move

    def get_possible_moves(self, field):
        """ Gets all the possible moves of the Pawn
        Arguments:
            field {Figure[]} -- a list filled with all pawns on the field
        Return:
            possible_moves {Position[]} -- if there are none the array is empty
        """
        assert isinstance(field, list), "field ist kein []" + str(type(field))
        self.__possible_moves_buffer = []
        __straight_is_free = consts.FREE_FIELD
        own_pos_num = super().get_position().get_pos_number()
        own_pos_cha = ord(super().get_position().get_pos_char())
        own_direction = self.__get_move_direction()
        for figure in field:
            assert isinstance(figure, Figure), "figure ist kein Figure in field[]" + str(type(figure))
            fig_pos_num = figure.get_position().get_pos_number()
            fig_pos_cha = ord(figure.get_position().get_pos_char())
            if figure.get_color() != super().get_color():
                if fig_pos_cha in ((own_pos_cha + consts.DIRECTIONS["LEFT"]), (own_pos_cha + consts.DIRECTIONS["RIGHT"])):
                    if fig_pos_num == own_pos_num:
                        if figure.get_double_move():
                            self.__possible_moves_buffer.append(Position(chr(fig_pos_cha), (fig_pos_num + own_direction)))
                    elif fig_pos_num == (own_pos_num + own_direction):
                        self.__possible_moves_buffer.append(Position(chr(fig_pos_cha), fig_pos_num))
            if fig_pos_cha == own_pos_cha:
                if fig_pos_num == (own_pos_num + own_direction):
                    __straight_is_free = consts.ONE_IN_FRONT
                elif fig_pos_num == (own_pos_num + (consts.DOUBLE_MOVE * own_direction)):
                    __straight_is_free = consts.TWO_IN_FRONT
        if __straight_is_free == consts.FREE_FIELD:
            self.__possible_moves_buffer.append(Position(chr(own_pos_cha), (own_pos_num + own_direction)))
            if self.get_double_move() is None:
                self.__possible_moves_buffer.append(Position(chr(own_pos_cha), own_pos_num + (consts.DOUBLE_MOVE * own_direction)))
        elif __straight_is_free == consts.TWO_IN_FRONT:
            self.__possible_moves_buffer.append(Position(chr(own_pos_cha), (own_pos_num + own_direction)))
        return self.__possible_moves_buffer

    def do_move(self, new_position):
        """ Does the move to the position if the position is a possible move
        Arguments:
            new_position {Position} -- new Position of the pawn
        Return:
            consts.ERROR_CODES["Sucess"] {str} -- successfull moved
            consts.ERROR_CODES["NoPosMove"] {str} -- move is not possible
        """
        assert isinstance(new_position, Position), "new_position ist keine Position" + str(type(new_position))
        old_pos_num = super().get_position().get_pos_number()
        for position in self.__possible_moves_buffer:
            if position.get_pos_char() == new_position.get_pos_char():
                if position.get_pos_number() == new_position.get_pos_number():
                    super().do_move(new_position)
                    if old_pos_num + (consts.DOUBLE_MOVE * self.__get_move_direction()) == new_position.get_pos_number():
                        self.__has_done_double_move = True
                    else:
                        self.__has_done_double_move = False
                    self.__possible_moves_buffer = []
                    return consts.ERROR_CODES["Success"]
        self.__possible_moves_buffer = []
        return consts.ERROR_CODES["NoPosMove"]

    def en_passant_timed_out(self):
        """ if pawn has done double move then it will be set to false
        """
        if self.__has_done_double_move:
            self.__has_done_double_move = False
