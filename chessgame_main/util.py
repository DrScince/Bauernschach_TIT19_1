"""[summary]

Returns:
    [type] -- [description]
"""
#TODO Frank docstring
try:
    import consts
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
                        gamefield[i][j] = "◼"
                    else:
                        gamefield[i][j] = "◻"
                else:
                    if j % 2 == 0:
                        gamefield[i][j] = "◻"
                    else:
                        gamefield[i][j] = "◼"
        return gamefield
