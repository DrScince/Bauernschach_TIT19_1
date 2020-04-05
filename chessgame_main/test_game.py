"""[summary]
"""
#TODO docstring

import unittest
from unittest.mock import patch
import sys
import os

try:
    import io
    from contextlib import contextmanager
    import consts
    from chess_logik import consts as game_consts
    import game
    from chess_storage import chess_storage
    from computer_gegner.opponent_move import Opponent
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
    __test_game = game.ActiveGame("Test1", "Test2", "Test_Game", None, chess_storage.ChessStorage())
    __test_run_game = game.ActiveGame("Test1", "Test2", "Test_Game", None, chess_storage.ChessStorage())
    __test_bot_game = game.ActiveGame("Test1", "Test2", "Test_Game", Opponent, chess_storage.ChessStorage())
    __test_win_black_game = game.ActiveGame("Test1", "Test2", "Test_Game", None, chess_storage.ChessStorage())
    __test_win_white_game = game.ActiveGame("Test1", "Test2", "Test_Game", None, chess_storage.ChessStorage())

    def test_000_init(self):
        """[summary]
        """
        #TODO docstring
        self.__test_game = game.ActiveGame("Test1", "Test2", "Test_Game", None, chess_storage.ChessStorage())
        self.__test_run_game = game.ActiveGame("Test1", "Test2", "Test_Game", None, chess_storage.ChessStorage())
        self.__test_bot_game = game.ActiveGame("Test1", "Test2", "Test_Game", Opponent, chess_storage.ChessStorage())
        self.__test_win_black_game = game.ActiveGame("Test1", "Test2", "Test_Game", None, chess_storage.ChessStorage())
        self.__test_win_white_game = game.ActiveGame("Test1", "Test2", "Test_Game", None, chess_storage.ChessStorage())
        self.assertIsInstance(self.__test_game, game.ActiveGame)
        self.assertIsInstance(self.__test_run_game, game.ActiveGame)
        self.assertIsInstance(self.__test_bot_game, game.ActiveGame)
        self.assertIsInstance(self.__test_win_black_game, game.ActiveGame)
        self.assertIsInstance(self.__test_win_white_game, game.ActiveGame)

    @patch('builtins.input')
    def test_001_run_game(self, mock_input):
        """[summary]
        """
        #TODO docstring
        # Weis macht zug
        mock_input.side_effect = ["A2", "A4"]
        game_return = self.__test_run_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        #
        #Keine FIgur auf Feld
        mock_input.side_effect = ["A4"]
        game_return = self.__test_run_game.run_game()
        self.assertEqual(game_return, consts.ERROR_CODES["WRONG_INPUT"])
        #Schwarz macht zug
        mock_input.side_effect = ["A7", "A5"]
        game_return = self.__test_run_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        #Kein Zug für Figur
        mock_input.side_effect = ["A4"]
        game_return = self.__test_run_game.run_game()
        self.assertEqual(game_return, consts.ERROR_CODES["WRONG_INPUT"])
        #
        mock_input.side_effect = ["G5"]
        game_return = self.__test_run_game.run_game()
        self.assertEqual(game_return, consts.ERROR_CODES["WRONG_INPUT"])
        #
        mock_input.side_effect = ["7H"]
        game_return = self.__test_run_game.run_game()
        self.assertEqual(game_return, consts.ERROR_CODES["WRONG_INPUT"])
        #
        mock_input.side_effect = [consts.GAME_MODE["SAVE"]]
        game_return = self.__test_run_game.run_game()
        self.assertEqual(game_return, consts.GAME_MODE["SAVE"])
        #
        mock_input.side_effect = [consts.GAME_MODE["NEW_GAME"]]
        game_return = self.__test_run_game.run_game()
        self.assertEqual(game_return, consts.GAME_MODE["NEW_GAME"])
        #
        mock_input.side_effect = [consts.GAME_MODE["QUIT"]]
        game_return = self.__test_run_game.run_game()
        self.assertEqual(game_return, consts.GAME_MODE["QUIT"])
        #
        mock_input.side_effect = [consts.GAME_MODE["LOAD"]]
        game_return = self.__test_run_game.run_game()
        self.assertEqual(game_return, consts.GAME_MODE["LOAD"])
        #
        mock_input.side_effect = ["Schnitzel"]
        game_return = self.__test_run_game.run_game()
        self.assertEqual(game_return, consts.ERROR_CODES["WRONG_INPUT"])
        ################################## White Win #####################################################
        mock_input.side_effect = ["C2", "C4"]
        game_return = self.__test_win_white_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["B7", "B5"]
        game_return = self.__test_win_white_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["C4", "C5"]
        game_return = self.__test_win_white_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["D7", "D5"]
        game_return = self.__test_win_white_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["C5", "D6"]
        game_return = self.__test_win_white_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["A7", "A6"]
        game_return = self.__test_win_white_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["D6", "D7"]
        game_return = self.__test_win_white_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["A6", "A5"]
        game_return = self.__test_win_white_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["D7", "D8", "B"]
        game_return = self.__test_win_white_game.run_game()
        self.assertEqual(game_return, consts.GAME_MODE["QUIT"])
        ################################## End: White Win #####################################################
        ################################## Black Win #####################################################
        mock_input.side_effect = ["C2", "C4"]
        game_return = self.__test_win_black_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["B7", "B5"]
        game_return = self.__test_win_black_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["A2", "A4"]
        game_return = self.__test_win_black_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["B5", "C4"]
        game_return = self.__test_win_black_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["E2", "E3"]
        game_return = self.__test_win_black_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["C4", "C3"]
        game_return = self.__test_win_black_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["E3", "E4"]
        game_return = self.__test_win_black_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["C3", "C2"]
        game_return = self.__test_win_black_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["H2", "H3"]
        game_return = self.__test_win_black_game.run_game()
        self.assertEqual(game_return, game_consts.WINNER_CODES["NoWinner"])
        mock_input.side_effect = ["C2", "C1", "B"]
        game_return = self.__test_win_black_game.run_game()
        self.assertEqual(game_return, consts.GAME_MODE["QUIT"])
        ################################## End: Black Win #####################################################


    def test_002_update_game(self):
        """Test the update game function
        """
        # pylint: disable = protected-access, unused-variable
        with captured_std() as (out, err, inp):
            self.__test_game._ActiveGame__update_game()
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
        with captured_std() as (out, err, inp):
            self.__test_run_game._ActiveGame__update_game()
        #TODO docstring

    def test_003_fill_default_game(self):
        """[summary]
        """
        #TODO docstring
        # pylint: disable = protected-access, unused-variable
        __gamefield_test = self.__test_game._ActiveGame__fill_default_game()
        self.assertIsInstance(__gamefield_test, list)
        # pylint: enable = protected-access, unused-variable

    def test_004_fill_game_field(self):
        """[summary]
        """
        # pylint: disable = protected-access, unused-variable
        __gamefield_test = self.__test_game._ActiveGame__fill_game_field()
        self.assertIsInstance(__gamefield_test, list)
        #TODO docstring
        # pylint: enable = protected-access, unused-variable

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
        # test = self.__test_game._ActiveGame__get_input()

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
        __test_name = self.__test_game.get_game_name()
        self.assertEqual(__test_name, "Test_Game")

    def test_014_get_playername_one(self):
        """[summary]
        """
        #TODO docstring
        __test_name_1 = self.__test_game.get_playername_one()
        self.assertEqual(__test_name_1, "Test1")

    def test_015_get_playername_two(self):
        """[summary]
        """
        #TODO docstring
        __test_name_2 = self.__test_game.get_playername_two()
        self.assertEqual(__test_name_2, "Test2")

    def test_016_get_play_against_bot(self):
        """[summary]
        """
        #TODO docstring
        __test_name = self.__test_game.get_play_against_bot()
        self.assertEqual(__test_name, False)
        __test_name = self.__test_bot_game.get_play_against_bot()
        self.assertEqual(__test_name, True)

    def test_999_remove_testfiles(self):
        """[summary]
        """
        __dir_game_saves = os.path.dirname(__file__)
        __dir_game_saves = os.path.join(__dir_game_saves, 'chess_storage')
        __dir_game_saves = os.path.join(__dir_game_saves, 'games')
        __dir_game_log = os.path.join(__dir_game_saves, "log")
        __test_logname = "Test_Game_log.txt"
        __dir_game_logfile = os.path.join(__dir_game_log, __test_logname)
        os.remove(__dir_game_logfile)
        self.assertFalse(os.path.isfile(__dir_game_logfile))
        if os.path.isdir(__dir_game_log):
            __list_files = os.listdir(__dir_game_log)
            if len(__list_files) == 0:
                os.removedirs(__dir_game_log)
        if os.path.isdir(__dir_game_saves):
            __list_files = os.listdir(__dir_game_saves)
            if len(__list_files) == 0:
                os.removedirs(__dir_game_saves)

        #TODO docstring
# Needed to run without console command
# if __name__ == '__main__':
#     unittest.main()
