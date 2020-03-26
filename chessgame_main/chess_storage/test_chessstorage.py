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

    def test_1_save_data(self):
        """Test the method save_data
        """
        __test = chess_storage.ChessStorage()
        __test_data = list(range(consts.TEST_LIST_LENGHT))
        __test_filename = consts.TEST_FILENAME
        __save_test = __test.save_data(__test_filename, __test_data, True)
        self.assertEqual(__save_test, 0)
        __save_test = __test.save_data(__test_filename, __test_data, False)
        self.assertEqual(__save_test, 2)
        __save_test = __test.save_data(__test_filename, __test_data, True)
        self.assertEqual(__save_test, 0)

    def test_2_load_data(self):
        """Test the method load_data
        """
        __test = chess_storage.ChessStorage()
        __test_filename = consts.TEST_FILENAME
        __test_data = list(range(consts.TEST_LIST_LENGHT))
        __load_test = __test.load_data(consts.TEST_NOTEXISTFILE)
        self.assertEqual(__load_test, None)
        __load_test = __test.load_data(__test_filename)
        self.assertEqual(__load_test, __test_data)

    def test_3_get_all_games(self):
        """Test the method get_all_games
        """
        __test = chess_storage.ChessStorage()
        __dir_game_saves = os.path.dirname(__file__)
        __dir_game_saves = os.path.join(__dir_game_saves, 'games')
        __filenames_infolder = []
        for __filename_infolder in os.listdir(__dir_game_saves):
            __filenames_infolder.append(__filename_infolder)
        __test_filenames = __test.get_all_games()
        self.assertEqual(__test_filenames, __filenames_infolder)

    def test_4_log_game(self):
        """Test the method log_game
        """
        __test = chess_storage.ChessStorage()
        __test_data = list(range(consts.TEST_LIST_LENGHT))
        __dir_game_saves = os.path.dirname(__file__)
        __dir_game_saves = os.path.join(__dir_game_saves, 'games')
        __test_filename = consts.TEST_FILENAME
        __test_logname = __test_filename + "_log.txt"
        __dir_game_log = os.path.join(__dir_game_saves, __test_logname)
        __log_test = __test.log_game(__test_filename, __test_data, True)
        self.assertEqual(__log_test, 0)
        with open(__dir_game_log, 'r') as __log_game:
            print("\nOne Line:")
            print(__log_game.read())
        __log_test = __test.log_game(__test_filename, __test_data, False)
        self.assertEqual(__log_test, 2)
        with open(__dir_game_log, 'r') as __log_game:
            print("Still one Line:")
            print(__log_game.read())
        __log_test = __test.log_game(__test_filename, __test_data, True)
        self.assertEqual(__log_test, 0)
        with open(__dir_game_log, 'r') as __log_game:
            print("Two Lines")
            print(__log_game.read())

    def test_999_remove_testfiles(self):
        """Remove all created files
        """
        __dir_game_saves = os.path.dirname(__file__)
        __dir_game_saves = os.path.join(__dir_game_saves, 'games')
        __test_filename = consts.TEST_FILENAME
        __dir_game_testfile = os.path.join(__dir_game_saves, __test_filename)
        __test_logname = __test_filename + "_log.txt"
        __dir_game_log = os.path.join(__dir_game_saves, __test_logname)
        os.remove(__dir_game_testfile)
        self.assertFalse(os.path.isfile(__dir_game_testfile))
        os.remove(__dir_game_log)
        self.assertFalse(os.path.isfile(__dir_game_log))
        __list_files = os.listdir(__dir_game_saves)
        if len(__list_files) == 0:
            os.removedirs(__dir_game_saves)

if __name__ == '__main__':
    unittest.main()
