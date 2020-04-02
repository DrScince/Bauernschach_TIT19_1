""" The field wich contains the Pawns
"""
import sys
try:
    from chess_logik.position import Position
    from chess_logik.pawn import Pawn
    from chess_logik import consts
except ImportError as err:
    print("ImportError"+str(err))
    sys.exit()

class Field():
    """ Contains all the figures in the game and methods to interact
    """
    def __init__(self, load_field=None):
        self.__white_turn = True
        #loadField is meant for testing
        self.__field = load_field
        if self.__field is None:
            self.__field = []
            for pos_char in "ABCDEFGH":
                self.__field.append(Pawn(consts.COLOR_BLACK, Position(pos_char, 7)))
                self.__field.append(Pawn(consts.COLOR_WHITE, Position(pos_char, 2)))

    def get_possible_moves(self, selected_position):
        """
        Arguments:
            selected_position {Position}
        Returns:
            possible_moves {Position[]}
            ERROR_CODES["WrongColor"] {str} -- if figure doesn't exist
            ERROR_CODES["NoFigure"] {str} -- if figure has the wrong color
            ERROR_CODES["NoPosMoves"] {str} -- if no moves are possible
        """
        assert isinstance(selected_position, Position), "selected_position is not a Position" + str(type(selected_position))
        for figure in self.get_field():
            if figure.get_position().get_pos_char() == selected_position.get_pos_char():
                if figure.get_position().get_pos_number() == selected_position.get_pos_number():
                    if (self.__white_turn and figure.get_color() == consts.COLOR_WHITE) or (figure.get_color() == consts.COLOR_BLACK and not self.__white_turn):
                        pos_moves = figure.get_possible_moves(self.get_field())
                        if len(pos_moves) == 0:
                            return consts.ERROR_CODES["NoPosMoves"]
                        return pos_moves
                    return consts.ERROR_CODES["WrongColor"]
        return consts.ERROR_CODES["NoFigure"]

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
        for figure in self.get_field():
            if figure.get_position().get_pos_char() == new_position.get_pos_char():
                if figure.get_position().get_pos_number() == new_position.get_pos_number():
                    self.get_field().remove(figure)
                    return
        for figure in self.get_field():
            if figure.get_position().get_pos_char() == new_position.get_pos_char():
                if own_color == consts.COLOR_BLACK:
                    move_direction = consts.DIRECTIONS["BLACK_MOVE"]
                elif own_color == consts.COLOR_WHITE:
                    move_direction = consts.DIRECTIONS["WHITE_MOVE"]
                if figure.get_position().get_pos_number() == new_position.get_pos_number() - move_direction:
                    if figure.get_double_move() and figure.get_color() != own_color:
                        self.get_field().remove(figure)

    def do_move(self, selected_position, new_position):
        """Move figure to new position
        Arguments:
            selected_position {Position} -- old position
            new_position {Position} -- new position
        Returns:
            field {Figure[]}
            ERROR_CODES["NoFigure"] {str} -- if one of the figures doesn't exist
            ERROR_CODES["WrongColor"] {str} -- if figure has the wrong color
        """
        assert isinstance(selected_position, Position), "selected_position is not a Position" + str(type(selected_position))
        assert isinstance(new_position, Position), "new_position is not a Position" + str(type(new_position))
        for figure in self.get_field():
            if figure.get_position().get_pos_char() == selected_position.get_pos_char():
                if figure.get_position().get_pos_number() == selected_position.get_pos_number():
                    if (self.__white_turn and figure.get_color() == consts.COLOR_WHITE) or (figure.get_color() == consts.COLOR_BLACK and not self.__white_turn):
                        self.__del_old_figure(new_position, figure.get_color())
                        figure.do_move(new_position)
                        self.__white_turn = not self.__white_turn
                        return self.get_field()
                    return consts.ERROR_CODES["WrongColor"]
        return consts.ERROR_CODES["NoFigure"]

    def check_win(self):
        """ Check if someone won
        Returns:
            WINNER_CODES["NoWinner"] {int} -- no winner
            WINNER_CODES["WhiteWon"] {int} -- white won
            WINNER_CODES["BlackWon"] {int} -- black won
        """
        for figure in self.get_field():
            if figure.get_color() == consts.COLOR_WHITE:
                if figure.get_position.get_pos_number() == consts.GAME_SIZE:
                    return consts.WINNER_CODES["WhiteWon"]
                count_white += consts.WINNER_CODES["WhiteWon"]
            if figure.get_color() == consts.COLOR_BLACK:
                if figure.get_position().get_pos_number() == consts.GAME_SIZE_MIN:
                    return consts.WINNER_CODES["BlackWon"]
                count_black += consts.WINNER_CODES["WhiteWon"]
        if count_white == 0:
            return consts.WINNER_CODES["BlackWon"]
        if count_black == 0:
            return consts.WINNER_CODES["WhiteWon"]
        return consts.WINNER_CODES["NoWinner"]
