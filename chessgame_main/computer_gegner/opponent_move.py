"""computer opponent for the chess game
"""
from random import randint

class Opponent:
    """Computer Opponent for the chess game
    """
    def __init__(self):
        pass
    def bot_move(self, pawn_array):
        """moves pawn (for external call)
        """

        result_list = []
        selected_pawn = randint(0, 7)
        selected_move = self.select_pawn_move(pawn_array, selected_pawn)

        while selected_pawn == "x":
            selected_pawn = randint(0, 7)
            selected_move = self.select_pawn_move(pawn_array, selected_pawn)
        result_list.insert(0, pawn_array[selected_pawn].position)
        result_list.insert(1, selected_move)

        return result_list


    def diagonal_left(self, pawn_pos):
        """checks for diagonal left field
        """

        x_value = ord(pawn_pos[0:1])
        y_value = pawn_pos[1:2]

        if x_value > 65:
            x_value = chr(x_value-1)
            y_value -= 1
            diagonal_left = x_value + str(y_value)
            return diagonal_left
        else:
            diagonal_left = "x"

    def diagonal_right(self, pawn_pos):
        """checks for diagonal right field
        """
        x_value = ord(pawn_pos[0:1])
        y_value = pawn_pos[1:2]

        if x_value < 72:
            x_value = chr(x_value+1)
            y_value -= 1
            diagonal_right = x_value + str(y_value)
            return diagonal_right
        else:
            diagonal_right = "x"

    def select_pawn_move(self, pawn_array, selected_pawn):
        """moves the pawn
        """
        no_move_possible = False
        diag_left_pos = self.diagonal_left(pawn_array[selected_pawn].position)
        diag_right_pos = self.diagonal_right(pawn_array[selected_pawn].position)
        if diag_left_pos != "x":
            for i in range(8, 16):
                if pawn_array[i].position != diag_left_pos:
                    continue
                else:
                    return diag_left_pos
        elif diag_right_pos != "x":
            for i in range(8, 16):
                if pawn_array[i].position != diag_right_pos:
                    continue
                else:
                    return diag_right_pos
        else:
            x_value = ord(pawn_array[selected_pawn].position[0:1])
            y_value = pawn_array[selected_pawn].position[1:2] - 1
            forward_step = x_value + str(y_value)

            for i in range(8, 16):
                if pawn_array[i].position != forward_step:
                    continue
                else:
                    no_move_possible = True
                    break
            if not no_move_possible:
                return forward_step
            else:
                return "x"
