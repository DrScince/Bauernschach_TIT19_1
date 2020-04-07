"""computer opponent for the chess game
"""
import sys
from random import randint
try:
    import consts
    from chess_logik.pawn import Pawn
except ImportError as err:
    print("ImportError "+str(err))
    sys.exit()

class Opponent:
    """Computer Opponent for the chess game
    """
    def __init__(self):
        pass

    def bot_move(self, pawn_array):
        """moves pawn (for external call)
            Arguments:
                pawn_array[] {pawns} -- selected pawn position
            Returns:
                pawn_move {string[]} -- old and new position of the pawn
                    string[0] = old_position
                    string[1] = new_position
        """
        assert isinstance(pawn_array, list), "pawn_array ist kein list-Objekt"
        for pawn in pawn_array:
            assert isinstance(pawn, Pawn), "pawn ist kein Pawn-Objekt in pawn_array[]"
        result_list = []
        selected_pawn = randint(0, len(pawn_array)-1)
        while pawn_array[selected_pawn].get_color() == consts.COLOR_WHITE:
            selected_pawn = randint(0, len(pawn_array)-1)

        selected_move = self.select_pawn_move(pawn_array, selected_pawn)

        while selected_move == "x":
            selected_pawn = randint(0, len(pawn_array)-1)
            while pawn_array[selected_pawn].get_color() == consts.COLOR_WHITE:
                selected_pawn = randint(0, len(pawn_array)-1)
            selected_move = self.select_pawn_move(pawn_array, selected_pawn)


        temp_pos = pawn_array[selected_pawn].get_position()
        result_list.insert(0, temp_pos.get_pos_char() + str(temp_pos.get_pos_number()))
        result_list.insert(1, selected_move)

        return result_list

    def diagonal_left(self, pawn_pos):
        """checks for diagonal left field
            Arguments:
                pawn_pos {Position} -- Position of the selected pawn
            Returns:
                possible_move {string} -- possible move or x
        """

        x_value = pawn_pos.get_pos_char()
        y_value = pawn_pos.get_pos_number()

        if ord(x_value) > ord("A"):
            x_value = chr(ord(x_value)-1)
            y_value -= 1
            diagonal_left = x_value + str(y_value)
            return diagonal_left
        else:
            return "x"

    def diagonal_right(self, pawn_pos):
        """checks for diagonal right field
          Arguments:
               pawn_pos {Position} -- Position of the selected pawn
            Returns:
                possible_move {string} -- possible move or x
        """
        x_value = pawn_pos.get_pos_char()
        y_value = pawn_pos.get_pos_number()

        if ord(x_value) < ord("H"):
            x_value = chr(ord(x_value)+1)
            y_value -= 1
            diagonal_right = x_value + str(y_value)
            return diagonal_right
        else:
            return "x"

    def select_pawn_move(self, pawn_array, selected_pawn):
        """moves the pawn
            Arguments:
                pawn_array[] {pawns} -- array with the pawn positions
                selected_pawn{int} -- index of the selected pawn
            Returns:
                possible_move{string} -- possible move or x
        """
        no_move_possible = False
        array_len = len(pawn_array)
        diag_left_pos = self.diagonal_left(pawn_array[selected_pawn].get_position())
        diag_right_pos = self.diagonal_right(pawn_array[selected_pawn].get_position())
        if diag_left_pos != "x" and diag_left_pos is not None:
            for i in range(0, array_len):
                if i != selected_pawn:
                    temp_pos = pawn_array[i].get_position()
                    if temp_pos.get_pos_char() != diag_left_pos[0:1] or temp_pos.get_pos_number() != int(diag_left_pos[1:2]):
                        continue
                    elif (pawn_array[i].get_color() == consts.COLOR_WHITE and temp_pos.get_pos_char() == diag_left_pos[0:1]
                          and temp_pos.get_pos_number() == int(diag_left_pos[1:2])):
                        return diag_left_pos
        if diag_right_pos != "x" and diag_right_pos is not None:
            for i in range(0, array_len):
                if i != selected_pawn:
                    temp_pos = pawn_array[i].get_position()
                    if temp_pos.get_pos_char() != diag_right_pos[0:1] or temp_pos.get_pos_number() != int(diag_right_pos[1:2]):
                        continue
                    elif (pawn_array[i].get_color() == consts.COLOR_WHITE and temp_pos.get_pos_char() == diag_right_pos[0:1]
                          and temp_pos.get_pos_number() == int(diag_right_pos[1:2])):
                        return diag_right_pos

        temp_pos = pawn_array[selected_pawn].get_position()
        x_value = temp_pos.get_pos_char()
        y_value = temp_pos.get_pos_number() - 1
        forward_step = x_value + str(y_value)

        for i in range(0, array_len):
            if i != selected_pawn:
                temp_pos = pawn_array[i].get_position()
                if temp_pos.get_pos_char() == forward_step[0:1] and temp_pos.get_pos_number() == int(forward_step[1:2]):
                    no_move_possible = True
                    break
        if no_move_possible:
            return "x"
        else:
            return forward_step
