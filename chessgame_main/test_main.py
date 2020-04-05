import unittest
from unittest.mock import patch
import sys
import os

try:
    import io
    from contextlib import contextmanager
    from chess_storage.chess_storage import ChessStorage
    from game import ActiveGame
    import consts
    from main import __print_welcome_screen as print_welcome_screen
    from main import __get_load_game as get_load_game
    from main import __check_game_saved as check_game_saved
    from main import __set_new_game as set_new_game
    from main import __quit_game as quit_game
    from main import main
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


class MainTest(unittest.TestCase):
    def test_000_init(self):
        """no init needed because main is no class
        """

    @patch('builtins.input')
    def test_001_main(self, mock_input):
        """"[summary]
          
        Arguments:
            self {[type]} -- [description]
        """
        mock_input.side_effect = ["n", "n", "Test_Game", "Test1", "Test2", consts.GAME_MODE["QUIT"], consts.GAME_MODE["QUIT"], consts.GAME_MODE["QUIT"]]
        main()
        mock_input.side_effect = ["n", "n", "Test_Game", "Test1", "Test2", consts.GAME_MODE["QUIT"], consts.GAME_MODE["SAVE"], consts.GAME_MODE["QUIT"]]
        main()
        mock_input.side_effect = ["l", "1", "H2", "H4", consts.GAME_MODE["QUIT"], consts.GAME_MODE["QUIT"], consts.GAME_MODE["QUIT"]]
        main()
        mock_input.side_effect = [" " , consts.GAME_MODE["QUIT"]]
        main()

    @patch('builtins.input')
    def test_002_print_welcome_screen(self, mock_input):
        """[summary]
        """
        mock_input.side_effect = consts.GAME_MODE["NEW_GAME"]
        result = print_welcome_screen()
        self.assertEqual(result, consts.GAME_MODE["NEW_GAME"])
        mock_input.side_effect = consts.GAME_MODE["LOAD"]
        result = print_welcome_screen()
        self.assertEqual(result, consts.GAME_MODE["LOAD"])
        mock_input.side_effect = consts.GAME_MODE["QUIT"]
        result = print_welcome_screen()
        self.assertEqual(result, consts.GAME_MODE["QUIT"])
        
    @patch('builtins.input')
    def test_003_get_load_game(self, mock_input):
        """[summary]
          
        Arguments:
            self {[type]} -- [description]
        """
        mock_input.side_effect = ["1"]
        result = get_load_game(["Game1", "Game2", "Game3"])
        self.assertEqual(result, "Game1")
        mock_input.side_effect = ["2"]
        result = get_load_game(["Game1", "Game2", "Game3"])
        self.assertEqual(result, "Game2")
        mock_input.side_effect = ["3"]
        result = get_load_game(["Game1", "Game2", "Game3"])
        self.assertEqual(result, "Game3")
        mock_input.side_effect = ["1"]
        result = get_load_game([])
        self.assertEqual(result, consts.ERROR_CODES["NO_GAME_TO_LOAD"])
        #TODO 

    @patch('builtins.input')
    def test_004_check_new_game(self, mock_input):
        """[summary]
        """
        test_storage = ChessStorage()
        test_game = ActiveGame("Test1", "Test2", "Test_Game", None, test_storage)
        mock_input.side_effect = consts.GAME_MODE["SAVE"]
        with captured_std() as (out, err, inp):
            check_game_saved(test_game, test_storage)
        output = out.getvalue().strip()
        accept_output = 'Spiel wurde noch nicht gepspeichert\n\t\t\t\t\t(S)\tSpiel Speichern\n\t\t\t\t\t(B)\tohne Speichern fortfahren'
        self.assertEqual(output, accept_output)

        mock_input.side_effect = consts.GAME_MODE["SAVE_NEW"]
        with captured_std() as (out, err, inp):
            check_game_saved(test_game, test_storage)
        output = out.getvalue().strip()
        accept_output = 'Spiel wurde bereits gespeichert\n\t\t\t\t\tSoll der Spielstand überschrieben werden\n\t\t\t\t\t(S)\tSpiel Überschreiben\n\t\t\t\t\t(S'
        accept_output = accept_output + 'N)\tals neues Spiel Speichern\n\t\t\t\t\t(B)\tohne Speichern fortfahren'
        self.assertEqual(output, accept_output)

        mock_input.side_effect = consts.GAME_MODE["QUIT"]
        with captured_std() as (out, err, inp):
            check_game_saved(test_game, test_storage)
        output = out.getvalue().strip()
        accept_output = 'Spiel wurde bereits gespeichert\n\t\t\t\t\tSoll der Spielstand überschrieben werden\n\t\t\t\t\t(S)\tSpiel Überschreiben\n\t\t\t\t\t(S'
        accept_output = accept_output + 'N)\tals neues Spiel Speichern\n\t\t\t\t\t(B)\tohne Speichern fortfahren'
        self.assertEqual(output, accept_output)
    
    @patch('builtins.input')
    def test_005_set_new_game(self, mock_input):
        """[summary]
        """
        test_storage = ChessStorage()
        mock_input.side_effect = ["n", "Test_Game1", "Test1", "Test2"]
        result = set_new_game(test_storage)
        self.assertIsInstance(result, ActiveGame)
        mock_input.side_effect = ["j", "Test_Game1", "Test1", "Test2"]
        result = set_new_game(test_storage)
        self.assertIsInstance(result, ActiveGame)

    def test_006_quit_game(self):
        """[summary]
        """
        result = quit_game()
        self.assertEqual(result, False)
        
    def test_999_remove_testfiles(self):
        """Remove all created files
        """
        __dir_game_saves = os.path.dirname(__file__)
        __dir_game_saves = os.path.join(__dir_game_saves, 'chess_storage')
        __dir_game_saves = os.path.join(__dir_game_saves, 'games')
        __dir_game_testfile = os.path.join(__dir_game_saves, "Test_Game")
        __dir_game_log = os.path.join(__dir_game_saves, "log")
        __dir_game_logfile = os.path.join(__dir_game_log, "Test_Game_log.txt")
        os.remove(__dir_game_logfile)
        os.remove(__dir_game_testfile)

        self.assertFalse(os.path.isfile(__dir_game_logfile))
        self.assertFalse(os.path.isfile(__dir_game_testfile))

        if os.path.isdir(__dir_game_log):
            __list_files = os.listdir(__dir_game_log)
            if len(__list_files) == 0:
                os.removedirs(__dir_game_log)
        if os.path.isdir(__dir_game_saves):
            __list_files = os.listdir(__dir_game_saves)
            if len(__list_files) == 0:
                os.removedirs(__dir_game_saves)
      

# Needed to run without console command
# if __name__ == '__main__':
#     unittest.main()