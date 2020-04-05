# pylint: disable=C
# pylint: disable = too-many-statements
import unittest
import sys
try:
    from chess_logik.pawn import Pawn
    from chess_logik.position import Position
    from chess_logik.field import Field
    from chess_logik import consts
except ImportError as err:
    print("ImportError"+str(err))
    sys.exit()

class FieldTest(unittest.TestCase):  
    
    def test_game_all_black_hit(self):
        field = Field()
        self.assertIsInstance(field.get_possible_moves(Position("A", 2)), list)
        self.assertIsInstance(field.do_move(Position("A", 2), Position("A", 3)), list)
        self.assertIsInstance(field.get_possible_moves(Position("B", 7)), list)
        self.assertIsInstance(field.do_move(Position("B", 7), Position("B", 6)), list)
        self.assertIsInstance(field.get_possible_moves(Position("A", 3)), list)
        self.assertIsInstance(field.do_move(Position("A", 3), Position("A", 4)), list)
        self.assertIsInstance(field.get_possible_moves(Position("C", 7)), list)
        self.assertIsInstance(field.do_move(Position("C", 7), Position("C", 5)), list)
        self.assertIsInstance(field.get_possible_moves(Position("A", 4)), list)
        self.assertIsInstance(field.do_move(Position("A", 4), Position("A", 5)), list)
        self.assertIsInstance(field.get_possible_moves(Position("D", 7)), list)
        self.assertIsInstance(field.do_move(Position("D", 7), Position("D", 5)), list)
        self.assertIsInstance(field.get_possible_moves(Position("A", 5)), list)
        self.assertIsInstance(field.do_move(Position("A", 5), Position("B", 6)), list)
        self.assertIsInstance(field.get_possible_moves(Position("C", 5)), list)
        self.assertIsInstance(field.do_move(Position("C", 5), Position("C", 4)), list)
        self.assertIsInstance(field.get_possible_moves(Position("B", 6)), list)
        self.assertIsInstance(field.do_move(Position("B", 6), Position("A", 7)), list)
        self.assertIsInstance(field.get_possible_moves(Position("E", 7)), list)
        self.assertIsInstance(field.do_move(Position("E", 7), Position("E", 6)), list)
        self.assertIsInstance(field.get_possible_moves(Position("B", 2)), list)
        self.assertIsInstance(field.do_move(Position("B", 2), Position("B", 3)), list)
        self.assertIsInstance(field.get_possible_moves(Position("H", 7)), list)
        self.assertIsInstance(field.do_move(Position("H", 7), Position("H", 6)), list)
        self.assertIsInstance(field.get_possible_moves(Position("B", 3)), list)
        self.assertIsInstance(field.do_move(Position("B", 3), Position("C", 4)), list)
        self.assertIsInstance(field.get_possible_moves(Position("G", 7)), list)
        self.assertIsInstance(field.do_move(Position("G", 7), Position("G", 6)), list)
        self.assertIsInstance(field.get_possible_moves(Position("C", 4)), list)
        self.assertIsInstance(field.do_move(Position("C", 4), Position("D", 5)), list)
        self.assertIsInstance(field.get_possible_moves(Position("H", 6)), list)
        self.assertIsInstance(field.do_move(Position("H", 6), Position("H", 5)), list)
        self.assertIsInstance(field.get_possible_moves(Position("D", 5)), list)
        self.assertIsInstance(field.do_move(Position("D", 5), Position("E", 6)), list)
        self.assertIsInstance(field.get_possible_moves(Position("H", 5)), list)
        self.assertIsInstance(field.do_move(Position("H", 5), Position("H", 4)), list)
        self.assertIsInstance(field.get_possible_moves(Position("E", 6)), list)
        self.assertIsInstance(field.do_move(Position("E", 6), Position("F", 7)), list)
        self.assertIsInstance(field.get_possible_moves(Position("H", 4)), list)
        self.assertIsInstance(field.do_move(Position("H", 4), Position("H", 3)), list)
        self.assertIsInstance(field.get_possible_moves(Position("G", 2)), list)
        self.assertIsInstance(field.do_move(Position("G", 2), Position("H", 3)), list)
        self.assertIsInstance(field.get_possible_moves(Position("G", 6)), list)
        self.assertIsInstance(field.do_move(Position("G", 6), Position("G", 5)), list)
        self.assertIsInstance(field.get_possible_moves(Position("F", 2)), list)
        self.assertIsInstance(field.do_move(Position("F", 2), Position("F", 3)), list)
        self.assertIsInstance(field.get_possible_moves(Position("G", 5)), list)
        self.assertIsInstance(field.do_move(Position("G", 5), Position("G", 4)), list)
        self.assertIsInstance(field.get_possible_moves(Position("H", 3)), list)
        self.assertIsInstance(field.do_move(Position("H", 3), Position("G", 4)), list)
        self.assertEqual(field.check_win(), consts.WINNER_CODES("WhiteWon"))


    def test_game_all_white_hit(self):
        field = Field()

    def test_game_all_black_back_line(self):
        field = Field()

    def test_game_all_white_back_line(self):
        field = Field()

    def test_error_codes(self):
        field = Field()
        self.assertEqual(field.do_move(Position("A", 3), Position("A", 4)), consts.ERROR_CODES["NoFigure"])
        self.assertEqual(field.do_move(Position("A", 7), Position("A", 6)), consts.ERROR_CODES["WrongColor"])
        self.assertEqual(field.get_possible_moves("A", 7), consts.ERROR_CODES["WrongColor"])
        self.assertEqual(field.check_win(), consts.WINNER_CODES["NoWinner"])

    def test_wrong_argument_types(self):
        field = Field()
        with self.assertRaises(Exception):
            field.get_possible_moves("Not a position Object")
        with self.assertRaises(Exception):
            field.do_move("Not a Position Object", "Not a Position Object")
        with self.assertRaises(Exception):
            field.do_move("Not a Position Object", Position("A", 2))
        with self.assertRaises(Exception):
            field.do_move(Position("A", 2), "Not a Position Object")
