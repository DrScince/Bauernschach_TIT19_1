"""[summary]
"""
#TODO docstring

import unittest
import sys

try:
    import io
    from contextlib import contextmanager
    import consts
    import game
    from chess_storage import chess_storage
except ImportError:
    print("Import Error!")
    sys.exit("Import Error!")

@contextmanager
def captured_std():
    """[summary]
    """
    #TODO docstring
    new_out, new_err, new_in = io.StringIO(), io.StringIO(), io.StringIO()
    old_out, old_err, old_in = sys.stdout, sys.stderr, sys.stdin
    try:
        sys.stdout, sys.stderr, sys.stdin = new_out, new_err, new_in
        yield sys.stdout, sys.stderr, sys.stdin
    finally:
        sys.stdout, sys.stderr, sys.stdin = old_out, old_err, old_in

class GameTest(unittest.TestCase):
    """[summary]
    Arguments:
        unittest {[type]} -- [description]
    """
    #TODO docstring

    __test_game = game.ActiveGame("Test1", "Test2", "Test_Game", False, chess_storage.ChessStorage())

    def test_000_init(self):
        """[summary]
        """
        #TODO docstring
        self.__test_game = game.ActiveGame("Test1", "Test2", "Test_Game", False, chess_storage.ChessStorage())
        self.assertIsInstance(self.__test_game, game.ActiveGame)

    def test_001_run_game(self):
        """[summary]
        """
        #TODO docstring

    def test_002_fill_default_game(self):
        """[summary]
        """
        #TODO docstring

    def test_003_fill_game_fiel(self):
        """[summary]
        """
        #TODO docstring

    def test_004_print_game_all(self):
        """[summary]
        """
        #TODO docstring

    def test_005_print_menu(self):
        """[summary]
        """
        #TODO docstring

    def test_006_print_footer(self):
        """[summary]
        """
        #TODO docstring
        # pylint: disable = protected-access, unused-variable
        with captured_std() as (out, err, inp):
            self.__test_game._ActiveGame__print_footer()
        output = out.getvalue().strip()
        self.assertEqual(output, "________________________________________________________________________________")
        # pylint: enable = protected-access, unused-variable

    def test_007_print_game(self):
        """[summary]
        """
        #TODO docstring

    def test_008_print_game_line(self):
        """[summary]
        """
        #TODO docstring

    def test_009_get_input(self):
        """[summary]
        """
        #TODO docstring

    def test_010_turn(self):
        """[summary]
        """
        #TODO docstring

    def test_011_get_input_move(self):
        """[summary]
        """
        #TODO docstring

    def test_012_get_game_name(self):
        """[summary]
        """
        #TODO docstring

    def test_999_remove_testfiles(self):
        """[summary]
        """
        #TODO docstring

# Needed to run without console command
# if __name__ == '__main__':
#     unittest.main()
