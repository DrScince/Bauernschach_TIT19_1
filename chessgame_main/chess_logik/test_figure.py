# pylint: disable=C
import unittest
import sys
try:
    from chess_logik.position import Position
    from chess_logik.figure import Figure
    from chess_logik import consts
except ImportError as err:
    print("ImportError "+str(err))
    sys.exit()

class FigureTest(unittest.TestCase):

    def test_normal_init_and_getter(self):
        tmp_pos = Position("A", 2)
        tmp = Figure(consts.COLOR_BLACK, tmp_pos)
        self.assertEqual(tmp.get_color, consts.COLOR_BLACK)
        self.assertEqual(tmp.get_position, tmp_pos)

    def test_error_codes(self):
        self.assertEqual(Figure(consts.COLOR_WHITE, None), consts.ERROR_CODES["None"])
        self.assertEqual(Figure(consts.COLOR_WHITE, Position("A", 2).do_move(Position("A", 3))), consts.ERROR_CODES["Success"])

    def test_wrong_argument_types(self):
        with self.assertRaises(Exception):
            Figure(2, Position("A", 2))
        with self.assertRaises(Exception):
            Figure("w", "not a Position Object")
        with self.assertRaises(Exception):
            tmp = Figure("w", Position("A", 2))
            tmp.do_move("not a Position Object")
