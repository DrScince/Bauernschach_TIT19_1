"""Manage gamedata
"""

import os
import pickle
import sys

try:
    from chess_storage import consts
except ImportError:
    print("Import Error!")
    sys.exit()

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

    def save_data(self, file_name, current_game, overwrite, append_name):
        """Save current game as an binary file
        Arguments:
            file_name {string} -- new name from the file
            current_game {matchfield} -- the current game to save
            overwrite {bool} -- True: overwrite the file, False: do nothing
            append_name {bool} -- True: append the file_name, False: do nothing
        Returns:
            ERROR_CODE -- SUCCESSFULL, FILE_EXIST
        """
        __dir_game = os.path.join(self.__dir_game_saves, str(file_name))
        if append_name:
            i = 0
            __file_name_split = str.split(file_name, "__")
            if len(__file_name_split) >= 2:
                if __file_name_split[1].isnumeric():
                    file_name = __file_name_split[0]
                    i = int(__file_name_split[1])
            while os.path.isfile(__dir_game):
                i += 1
                file_name = __file_name_split[0] + "__" + str(i)
                __dir_game = os.path.join(self.__dir_game_saves, str(file_name))
        if os.path.isfile(__dir_game):
            if overwrite:
                return self.__write_file(__dir_game, current_game)
            else:
                return consts.ERROR_CODES["FILE_EXIST"]
        else:
            return self.__write_file(__dir_game, current_game)

    def load_data(self, file_name):
        """load match from directory ../games
        Arguments:
            file_name {string} -- name frome file to load
        Returns:
            matchfield -- returns the loaded matchfield or ERROR_CODE -- FILE_EXIST
        """
        __dir_load_game = os.path.join(self.__dir_game_saves, str(file_name))
        try:
            with open(__dir_load_game, 'rb') as __new_game:
                __new_matchfield = pickle.load(__new_game)
                return __new_matchfield
        except IOError:
            return consts.ERROR_CODES["NO_FILE_EXIST"]

    def get_all_games(self):
        """list all files in ../games
        Returns:
            list -- all filenames as list
        """
        __games = []
        for __match in os.listdir(self.__dir_game_saves):
            if __match != "log":
                __games.append(__match)
        return __games

    def log(self, file_name, log_info, append):
        """Log in a txt file
        Arguments:
            file_name {string} -- new name from the file
            log_info {} -- info to log (converts to string)
            append {bool} -- True: append the file, False: do nothing
        Returns:
            ERROR_CODE -- SUCCESSFULL, FILE_EXIST
        """
        __log_name = str(file_name) + "_log.txt"
        __dir_game_log = os.path.join(self.__dir_game_log, __log_name)
        if os.path.isfile(__dir_game_log):
            if append:
                return self.__log_append(__dir_game_log, log_info)
            else:
                return consts.ERROR_CODES["FILE_EXIST"]
        else:
            return self.__log_append(__dir_game_log, log_info)

    def __write_file(self, file_path, current_game):
        """Write a file binary
        Arguments:
            file_path {string} -- must be a os path
            current_game {matchfield} -- the current game to save
        Returns:
            ERROR_CODE -- SUCCESSFULL
        """
        assert isinstance(file_path, str), "file_path is not a string"
        with open(file_path, 'wb') as __old_game:
            pickle.dump(current_game, __old_game)
            return consts.ERROR_CODES["SUCCESSFULL"]

    def __log_append(self, file_path, log_info):
        """Append logfiles
        Arguments:
            file_path {string} -- must be a os path
            log_info {} -- info to log (converts to string)
        Returns:
            ERROR_CODE -- SUCCESSFULL
        """
        assert isinstance(file_path, str), "file_path is not a string"
        with open(file_path, 'a', encoding="utf8") as __log_game:
            if isinstance(log_info, list):
                __len_list = len(log_info)
                for i in range(__len_list):
                    __log_game.writelines([str(log_info[i]), "\n"])
                return consts.ERROR_CODES["SUCCESSFULL"]
            else:
                __log_game.writelines([str(log_info), "\n"])
                return consts.ERROR_CODES["SUCCESSFULL"]
