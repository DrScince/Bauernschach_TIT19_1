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
        self.__dir_game_log = os.path.join(self.__dir_game_saves, "log")
        if not os.path.isdir(self.__dir_game_log):
            os.mkdir(self.__dir_game_log)

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
                return self.__write_file(__dir_game, current_game)
            else:
                return consts.FILE_EXIST
        else:
            return self.__write_file(__dir_game, current_game)

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

    def log(self, file_name, log_info, append):
        """Log in a txt file
        Arguments:
            file_name {string} -- new name from the file
            log_info {} -- info to log (converts to string)
            append {bool} -- True: append the file, False: do nothing
        Returns:
            ErrorCode -- 0 success, 2 file exists
        """
        __log_name = str(file_name) + "_log.txt"
        __dir_game_log = os.path.join(self.__dir_game_log, __log_name)
        if os.path.isfile(__dir_game_log):
            if append:
                return self.__log_append(__dir_game_log, log_info)
            else:
                return consts.FILE_EXIST
        else:
            return self.__log_append(__dir_game_log, log_info)

    def __write_file(self, file_path, current_game):
        """Write a file binary
        Arguments:
            file_path {string} -- must be a os path
            current_game {matchfield} -- the current game to save
        Returns:
            ErrorCode -- 0 Successs
        """
        assert isinstance(file_path, str), "file_path is not a string"
        with open(file_path, 'wb') as __old_game:
            pickle.dump(current_game, __old_game)
            return consts.SUCCESSFULL

    def __log_append(self, file_path, log_info):
        """Append logfiles
        Arguments:
            file_path {string} -- must be a os path
            log_info {} -- info to log (converts to string)
        Returns:
            ErrorCode -- 0 Successs
        """
        assert isinstance(file_path, str), "file_path is not a string"
        with open(file_path, 'a', encoding="utf8") as __log_game:
            if isinstance(log_info, list):
                __len_list = len(log_info)
                for i in range(__len_list):
                    __log_game.writelines([str(log_info[i]), "\n"])
                return consts.SUCCESSFULL
            else:
                __log_game.writelines([str(log_info), "\n"])
                return consts.SUCCESSFULL
