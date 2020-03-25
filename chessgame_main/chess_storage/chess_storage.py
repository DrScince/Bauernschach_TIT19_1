"""Manage gamedata
"""

import os
import pickle

class ChessStorage:
    """Manage gamefiles
    """

    def __init__(self):
        """get path
        """
        self.__dir_game_saves = os.path.dirname(__file__)
        self.__dir_game_saves = os.path.join(self.__dir_game_saves, '\\games')
        if not os.path.isdir(self.__dir_game_saves):
            os.mkdir(self.__dir_game_saves, mode=0o777)

    def save_data(self, file_name, current_game, overwrite):
        """Save current game as an binary file
        Arguments:
            file_name {string} -- new name from the file
            current_game {matchfield} -- the current game to save
            overwrite {bool} -- True: overwrite the file, False: do nothing
        Returns:
            ErrorCode -- 0 success, 2 file exists
        """
        __dir_game = os.path.join(self.__dir_game_saves, str(file_name))
        for __match in os.listdir(self.__dir_game_saves):
            if __match == file_name:
                if overwrite:
                    with open(__dir_game, 'wb') as __old_game:
                        pickle.dump(current_game, __old_game)
                        return 0
                else:
                    return 2
        with open(__dir_game, 'wb') as __old_game:
            pickle.dump(current_game, __old_game)
            return 0

    def load_data(self, file_name):
        """load match from directory ../games
        Arguments:
            file_name {string} -- name frome file to load
        Returns:
            matchfield -- returns the loaded matchfield or None
        """
        __dir_load_game = os.path.join(self.__dir_game_saves, str(file_name))
        try:
            with open(__dir_load_game, 'rb') as __new_game:
                __new_matchfield = pickle.load(__new_game)
                return __new_matchfield
        except IOError:
            return None

    def get_all_games(self):
        """list all files in ../games
        Returns:
            list -- all filenames as list
        """
        __games = []
        for __match in os.listdir(self.__dir_game_saves):
            __games.append(__match)
        return __games
