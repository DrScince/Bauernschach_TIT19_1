"""[summary]

Returns:
    [type] -- [description]
"""
#TODO Frank docstring
try:
    import consts
    from chess_logik.pawn import Pawn
    # from chess_logik.field import Field
    from chess_logik.position import Position
except ImportError:
    print("Import Error!")
    exit()

class UIutil():
    """[summary]

    Returns:
        [type] -- [description]
    """

    @staticmethod
    def fill_default_game():
        """[summary]
        Returns:
            [type] -- [description]
        """
        #TODO docstring
        gamefield = [[0 for i in range(consts.GAME_SIZE)] for j in range(consts.GAME_SIZE)]
        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        gamefield[i][j] = "◻"
                    else:
                        gamefield[i][j] = "◼"
                else:
                    if j % 2 == 0:
                        gamefield[i][j] = "◼"
                    else:
                        gamefield[i][j] = "◻"
        return gamefield

    @staticmethod
    def fill_game_field(logic_gamefield, printed_gamefield):
        """[summary]
        
        Arguments:
            logic_gamefield {[type]} -- [description]
            printed_gamefield {[type]} -- [description]
        """
        #TODO Docstring
        for actual_pawn in logic_gamefield:

            __actual_pos = actual_pawn.get_position()
            __actual_color = actual_pawn.get_color()
            __col = ord(__actual_pos.get_pos_char())-65
            __row = 8-__actual_pos.get_pos_number()
            
            
            #
            if __actual_color == consts.COLOR_BLACK:
                printed_gamefield[__row][__col] = "♟"
            elif __actual_color == consts.COLOR_WHITE:
                printed_gamefield[__row][__col] = "♙"
        #
        return printed_gamefield
            
