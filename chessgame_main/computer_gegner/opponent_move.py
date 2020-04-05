"""computer opponent for the chess game
"""
try:
    import sys
    import consts
    from random import randint
    #from chess_logik import consts
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
        """

        result_list = []
        selected_pawn = randint(0, 15)#randint(0, 7)
        while pawn_array[selected_pawn].get_color() == consts.COLOR_WHITE:
            selected_pawn = randint(0, 15)

        selected_move = self.select_pawn_move(pawn_array, selected_pawn)

        while selected_move == "x":
            selected_pawn = randint(0, 15)#randint(0, 7)
            while pawn_array[selected_pawn].get_color() == consts.COLOR_WHITE:
                selected_pawn = randint(0, 15)
            selected_move = self.select_pawn_move(pawn_array, selected_pawn)
        temp_pos = pawn_array[selected_pawn].get_position()
        result_list.insert(0, temp_pos.pos_char + str(temp_pos.pos_number))
        result_list.insert(1, selected_move)

        return result_list


    def diagonal_left(self, pawn_pos):
        """checks for diagonal left field
        """

        x_value = pawn_pos.pos_char
        y_value = pawn_pos.pos_number

        if ord(x_value) > 65:
            x_value = chr(ord(x_value)-1)
            y_value -= 1
            diagonal_left = x_value + str(y_value)
            return diagonal_left
        else:
            diagonal_left = "x"

    def diagonal_right(self, pawn_pos):
        """checks for diagonal right field
        """
        x_value = pawn_pos.pos_char
        y_value = pawn_pos.pos_number

        if ord(x_value) < 72:
            x_value = chr(ord(x_value)+1)
            y_value -= 1
            diagonal_right = x_value + str(y_value)
            return diagonal_right
        else:
            diagonal_right = "x"

    def select_pawn_move(self, pawn_array, selected_pawn):
        """moves the pawn
        """
        no_move_possible = False
        diag_left_pos = self.diagonal_left(pawn_array[selected_pawn].get_position())
        diag_right_pos = self.diagonal_right(pawn_array[selected_pawn].get_position())
        if diag_left_pos != "x" and diag_left_pos is not None:
            for i in range(0, 16):#range(8, 16):
                if i != selected_pawn:
                    temp_pos = pawn_array[i].get_position()
                    if temp_pos.pos_char != diag_left_pos[0:1] or temp_pos.pos_number != diag_left_pos[1:2]:
                        continue
                    elif (pawn_array[i].get_color() == consts.COLOR_WHITE and temp_pos.pos_char == diag_left_pos[0:1]
                          and temp_pos.pos_number == diag_left_pos[1:2]):
                        return diag_left_pos
        if diag_right_pos != "x" and diag_right_pos is not None:
            for i in range(0, 16):#range(8, 16):
                if i != selected_pawn:
                    temp_pos = pawn_array[i].get_position()
                    if temp_pos.pos_char != diag_right_pos[0:1] or temp_pos.pos_number != diag_right_pos[1:2]:
                        continue
                    elif (pawn_array[i].get_color() == consts.COLOR_WHITE and temp_pos.pos_char == diag_right_pos[0:1]
                          and temp_pos.pos_number == diag_right_pos[1:2]):
                        return diag_right_pos

        temp_pos = pawn_array[selected_pawn].get_position()
        x_value = temp_pos.pos_char
        y_value = temp_pos.pos_number - 1
        forward_step = x_value + str(y_value)

        for i in range(0, 16):#range(8, 16):
            if i != selected_pawn:
                temp_pos = pawn_array[i].get_position()
                if temp_pos.pos_char != forward_step[0:1] or temp_pos.pos_number != forward_step[1:2]:
                    continue
                else:
                    no_move_possible = True
                    break
        if not no_move_possible:
            return forward_step
        else:
            return "x"
