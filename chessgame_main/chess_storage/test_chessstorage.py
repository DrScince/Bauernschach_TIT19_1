#TODO docstring
import unittest
from main.chess_storage import ChessStorage

class StorageTest(unittest.TestCase):
    #TODO docstring
    def test_load_data(self):
        #TODO docstring
        test = ChessStorage()
        self.assertTrue(test.load_data("test123"))
