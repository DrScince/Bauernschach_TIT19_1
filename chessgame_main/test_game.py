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

    def test_002_update_game(self):
        """[summary]
        """
        #TODO docstring

    def test_003_fill_default_game(self):
        """[summary]
        """
        #TODO docstring

    def test_004_fill_game_field(self):
        """[summary]
        """
        #TODO docstring

    def test_005_print_game_all(self):
        """[summary]
        """
        #TODO docstring
        # pylint: disable = protected-access, unused-variable
        with captured_std() as (out, err, inp):
            self.__test_game._ActiveGame__print_game_all()
        output = out.getvalue().strip()
        accepted_output = "Schachautomat\t\t\n\n\t\tNeues Spiel(N)\t\tSpeichern(S)\tLaden(L)\t\tSpiel Beenden(B)\n\t\t________________________________________"
        accepted_output = accepted_output + "________________________________________\n\n\t\t\t\t    A    B    C    D    E    F    G    H\n\n\t\t\t       \x1b"
        accepted_output = accepted_output + "[6;34;47m8\x1b[0;30;47m    ◻    ◼    ◻    ◼    ◻    ◼    ◻    ◼    \x1b[6;34;47m8\x1b[0;30;47m\n\t\t\t       \x1b"
        accepted_output = accepted_output + "[6;34;47m7\x1b[0;30;47m    ♟    ♟    ♟    ♟    ♟    ♟    ♟    ♟    \x1b[6;34;47m7\x1b[0;30;47m\n\t\t\t       \x1b"
        accepted_output = accepted_output + "[6;34;47m6\x1b[0;30;47m    ◻    ◼    ◻    ◼    ◻    ◼    ◻    ◼    \x1b[6;34;47m6\x1b[0;30;47m\n\t\t\t       \x1b"
        accepted_output = accepted_output + "[6;34;47m5\x1b[0;30;47m    ◼    ◻    ◼    ◻    ◼    ◻    ◼    ◻    \x1b[6;34;47m5\x1b[0;30;47m\t\t\x1b[0;30;47m\n"
        accepted_output = accepted_output + "\t\t\t       \x1b[6;34;47m4\x1b[0;30;47m    ◻    ◼    ◻    ◼    ◻    ◼    ◻    ◼    \x1b[6;34;47m4\x1b[0;30;47m\t"
        accepted_output = accepted_output + "\t\x1b[0;30;47m\n\t\t\t       \x1b[6;34;47m3\x1b[0;30;47m    ◼    ◻    ◼    ◻    ◼    ◻    ◼    ◻    \x1b[6;34;47"
        accepted_output = accepted_output + "m3\x1b[0;30;47m\n\t\t\t       \x1b[6;34;47m2\x1b[0;30;47m    ♙    ♙    ♙    ♙    ♙    ♙    ♙    ♙    \x1b[6;34;47"
        accepted_output = accepted_output + "m2\x1b[0;30;47m\n\t\t\t       \x1b[6;34;47m1\x1b[0;30;47m    ◼    ◻    ◼    ◻    ◼    ◻    ◼    ◻    \x1b[6;34;47"
        accepted_output = accepted_output + "m1\x1b[0;30;47m\n\n\t\t\t\t    A    B    C    D    E    F    G    H\n\n\t\t______________________________________"
        accepted_output = accepted_output + "__________________________________________"
        self.assertEqual(output, accepted_output)
        # pylint: enable = protected-access, unused-variable

    def test_006_print_menu(self):
        """[summary]
        """
        #TODO docstring
        # pylint: disable = protected-access, unused-variable
        with captured_std() as (out, err, inp):
            self.__test_game._ActiveGame__print_menu()
        output = out.getvalue().strip()
        accepted_output = "Schachautomat\t\t\n\n\t\tNeues Spiel(N)\t\tSpeichern(S)\tLaden(L)\t\tSpiel Beenden(B)\n\t\t"
        accepted_output = accepted_output + "________________________________________________________________________________"
        self.assertEqual(output, accepted_output)
        # pylint: enable = protected-access, unused-variable

    def test_007_print_footer(self):
        """[summary]
        """
        #TODO docstring
        # pylint: disable = protected-access, unused-variable
        with captured_std() as (out, err, inp):
            self.__test_game._ActiveGame__print_footer()
        output = out.getvalue().strip()
        accepted_output = "________________________________________________________________________________"
        self.assertEqual(output, accepted_output)
        # pylint: enable = protected-access, unused-variable

    def test_008_print_game(self):
        """[summary]
        """
        #TODO docstring
        # pylint: disable = protected-access, unused-variable
        with captured_std() as (out, err, inp):
            self.__test_game._ActiveGame__print_game()
        output = out.getvalue().strip()
        accepted_output = "A    B    C    D    E    F    G    H\n\n\t\t\t       \x1b[6;34;47m8\x1b[0;30;47m    ◻    ◼    ◻    ◼    ◻    ◼    ◻    ◼    \x1b[6;"
        accepted_output = accepted_output + "34;47m8\x1b[0;30;47m\n\t\t\t       \x1b[6;34;47m7\x1b[0;30;47m    ♟    ♟    ♟    ♟    ♟    ♟    ♟    ♟    \x1b[6;"
        accepted_output = accepted_output + "34;47m7\x1b[0;30;47m\n\t\t\t       \x1b[6;34;47m6\x1b[0;30;47m    ◻    ◼    ◻    ◼    ◻    ◼    ◻    ◼    \x1b[6;"
        accepted_output = accepted_output + "34;47m6\x1b[0;30;47m\n\t\t\t       \x1b[6;34;47m5\x1b[0;30;47m    ◼    ◻    ◼    ◻    ◼    ◻    ◼    ◻    \x1b[6;"
        accepted_output = accepted_output + "34;47m5\x1b[0;30;47m\t\t\x1b[0;30;47m\n\t\t\t       \x1b[6;34;47m4\x1b[0;30;47m    ◻    ◼    ◻    ◼    ◻    ◼    "
        accepted_output = accepted_output + "◻    ◼    \x1b[6;34;47m4\x1b[0;30;47m\t\t\x1b[0;30;47m\n\t\t\t       \x1b[6;34;47m3\x1b[0;30;47m    ◼    ◻    ◼  "
        accepted_output = accepted_output + "  ◻    ◼    ◻    ◼    ◻    \x1b[6;34;47m3\x1b[0;30;47m\n\t\t\t       \x1b[6;34;47m2\x1b[0;30;47m    ♙    ♙    ♙  "
        accepted_output = accepted_output + "  ♙    ♙    ♙    ♙    ♙    \x1b[6;34;47m2\x1b[0;30;47m\n\t\t\t       \x1b[6;34;47m1\x1b[0;30;47m    ◼    ◻    ◼  "
        accepted_output = accepted_output + "  ◻    ◼    ◻    ◼    ◻    \x1b[6;34;47m1\x1b[0;30;47m\n\n\t\t\t\t    A    B    C    D    E    F    G    H"
        self.assertEqual(output, accepted_output)
        # pylint: enable = protected-access, unused-variable

    def test_009_print_game_line(self):
        """[summary]
        """
        #TODO docstring
        # pylint: disable = protected-access, unused-variable
        with captured_std() as (out, err, inp):
            self.__test_game._ActiveGame__print_footer()
        output = out.getvalue().strip()
        accepted_output = "________________________________________________________________________________"
        self.assertEqual(output, accepted_output)
        # pylint: enable = protected-access, unused-variable

    def test_010_get_input(self):
        """[summary]
        """
        #TODO docstring

    def test_011_turn(self):
        """[summary]
        """
        #TODO docstring

    def test_012_get_input_move(self):
        """[summary]
        """
        #TODO docstring

    def test_013_get_game_name(self):
        """[summary]
        """
        #TODO docstring

    def test_014_get_playername_one(self):
        """[summary]
        """
        #TODO docstring

    def test_015_get_playername_two(self):
        """[summary]
        """
        #TODO docstring

    def test_016_get_play_against_bot(self):
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
