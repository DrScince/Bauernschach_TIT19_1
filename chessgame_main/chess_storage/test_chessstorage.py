"""Test chess_storage
"""
import unittest
import os

try:
    import chess_storage
    import consts
except ImportError:
    print("Import Error!")
    exit()

class StorageTest(unittest.TestCase):
    """Tests the class CHESSStorage
    """
    __test_data = list(range(consts.TEST_LIST_LENGHT))
    __test_filename = "TestGame"
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
        __dir_game_saves = os.path.dirname(__file__)
        __dir_game_saves = os.path.join(__dir_game_saves, '\\games')
        __filenames = []
        for __filename_folder in os.listdir(__dir_game_saves):
            __filenames.append(__filename_folder)
        __test_filenames = self.__test.get_all_games()
        self.assertEqual(__test_filenames, __filenames)

if __name__ == '__main__':
    unittest.main()
