"""save and load score
"""

import os
import pickle

class ChessStorage:
    """Manage gamefiles
    """
    __dir_game_saves = None

    def __init__(self):
        """get path
        """
        __dir_game_saves = os.path.dirname(__file__)
        __dir_game_saves = os.path.join(__dir_game_saves, '\\games')
        if os.path.isdir(__dir_game_saves) != True:
            os.mkdir(__dir_game_saves, mode=0o777, exist_ok=False)

    def load_data(self, file_name):
        """load match from directory ../games
        Arguments:
            file_name {string} -- name frome file to load
        Returns:
            matchfield -- returns the loaded matchfield or None
        """
        __dir_load_game = os.path.join(self.__dir_game_saves, file_name)
        try:
            with open(__dir_load_game, 'rb') as new_game:
                new_matchfield = pickle.load(new_game)
                return new_matchfield
        except IOError:
            return None

    def save_data(self, file_name, current_game, overwrite):
        """Save current game as an binary file
        Arguments:
            file_name {string} -- new name from the file
            current_game {matchfield} -- the current game to save
            overwrite {bool} -- True: overwrite the file, False: do nothing
        Returns:
            ErrorCode -- 0 success, 2 file exists
        """
        __dir_game = os.path.join(self.__dir_game_saves, file_name)
        for match in os.listdir(self.__dir_game_saves):
            if match == file_name:
                if overwrite:
                    with open(__dir_game, 'wb') as old_game:
                        pickle.dump(current_game, old_game)
                        return 0
                else:
                    return 2
        with open(__dir_game, 'wb') as old_game:
            pickle.dump(current_game, old_game)
            return 0

    def get_all_games(self):
        """list all files in ../games
        Returns:
            list -- all filenames as list
        """
        __games = []
        for match in os.listdir(self.__dir_game_saves):
            __games.append(match)
        return __games
