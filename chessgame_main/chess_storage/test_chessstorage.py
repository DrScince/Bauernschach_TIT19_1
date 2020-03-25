"""Test chess_storage
"""
import unittest
import os

from ..chess_storage import chess_storage

try:
    # import chess_storage
    import consts
except ImportError:
    print("Import Error!")
    exit()

class StorageTest(unittest.TestCase):
    """Tests the class CHESSStorage
    """
    #Data
    __test_data = list(range(consts.TEST_LIST_LENGHT))
    __test_filename = "TestGame"
    #Path
    __dir_game_saves = os.path.dirname(__file__)
    __dir_game_saves = os.path.join(__dir_game_saves, '\\games')
    #Instance of Chessstorage
    __test = chess_storage.ChessStorage()

    def test_1_save_data(self):
        """Test the method save_data
        """
        __save_test = self.__test.save_data(self.__test_filename, self.__test_data, True)
        self.assertEqual(__save_test, 0)
        __save_test = self.__test.save_data(self.__test_filename, self.__test_data, False)
        self.assertEqual(__save_test, 2)
        __save_test = self.__test.save_data(self.__test_filename, self.__test_data, True)
        self.assertEqual(__save_test, 0)

    def test_2_load_data(self):
        """Test the method load_data
        """
        __load_test = self.__test.load_data("Test123")
        self.assertEqual(__load_test, None)
        __load_test = self.__test.load_data(self.__test_filename)
        self.assertEqual(__load_test, self.__test_data)

    def test_3_get_all_games(self):
        """Test the method get_all_games
        """
        __filenames = []
        for __filename_folder in os.listdir(self.__dir_game_saves):
            __filenames.append(__filename_folder)
        __test_filenames = self.__test.get_all_games()
        self.assertEqual(__test_filenames, __filenames)

    def test_4_log_game(self):
        """Test the method log_game
        """
        __test_filename = str(self.__test_filename) + "_log.txt"
        __dir_game_log = os.path.join(self.__dir_game_saves, str(__test_filename))
        with open(__dir_game_log, 'w') as __log_game:
            __log_game.truncate()
        __log_test = self.__test.log_game(self.__test_filename, self.__test_data, True)
        self.assertEqual(__log_test, 0)
        with open(__dir_game_log, 'r') as __log_game:
            print("\nOne Line:")
            print(__log_game.read())
        __log_test = self.__test.log_game(self.__test_filename, self.__test_data, False)
        self.assertEqual(__log_test, 2)
        with open(__dir_game_log, 'r') as __log_game:
            print("Still one Line:")
            print(__log_game.read())
        __log_test = self.__test.log_game(self.__test_filename, self.__test_data, True)
        self.assertEqual(__log_test, 0)
        with open(__dir_game_log, 'r') as __log_game:
            print("Two Lines")
            print(__log_game.read())

if __name__ == '__main__':
    unittest.main()
