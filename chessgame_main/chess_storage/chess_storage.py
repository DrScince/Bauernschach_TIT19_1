"""Manage gamedata
"""

import os
import pickle

try:
    from chess_storage import consts
except ImportError:
    print("Import Error!")
    exit()

class ChessStorage:
    """Manage gamefiles
    """

    def __init__(self):
        """get path
        """
        self.__dir_game_saves = os.path.dirname(__file__)
        self.__dir_game_saves = os.path.join(self.__dir_game_saves, "games")
        if not os.path.isdir(self.__dir_game_saves):
            os.mkdir(self.__dir_game_saves)

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
        if os.path.isfile(__dir_game):
            if overwrite:
                with open(__dir_game, 'wb') as __old_game:
                    pickle.dump(current_game, __old_game)
                    return consts.SUCCESSFULL
            else:
                return consts.FILE_EXIST
        else:
            with open(__dir_game, 'wb') as __old_game:
                pickle.dump(current_game, __old_game)
                return consts.SUCCESSFULL

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

    def log_game(self, file_name, log_info, append):
        """Log in a txt file
        Arguments:
            file_name {string} -- new name from the file
            log_info {} -- info to log (converts to string)
            append {bool} -- True: append the file, False: do nothing
        Returns:
            ErrorCode -- 0 success, 2 file exists
        """
        __log_name = str(file_name) + "_log.txt"
        __dir_game_log = os.path.join(self.__dir_game_saves, __log_name)
        if os.path.isfile(__dir_game_log):
            if append:
                with open(__dir_game_log, 'a') as __log_game:
                    __log_game.writelines([str(log_info), "\n"])
                    return consts.SUCCESSFULL
            else:
                return consts.FILE_EXIST
        else:
            with open(__dir_game_log, 'a') as __log_game:
                __log_game.writelines([str(log_info), "\n"])
                return consts.SUCCESSFULL
