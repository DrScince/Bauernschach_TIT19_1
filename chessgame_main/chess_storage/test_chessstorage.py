#TODO docstring
import unittest

try:
    from chess_storage import ChessStorage
except ImportError:
    print("Import Error!")
    exit()

class StorageTest(unittest.TestCase):
    #TODO docstring
    def test_load_data(self):
        #TODO docstring
        test = ChessStorage()
        self.assertTrue(test.load_data("Test123"))
