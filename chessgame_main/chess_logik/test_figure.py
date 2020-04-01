# pylint: disable=C
import unittest
import sys
try:
    from chess_logik.position import Position
    from chess_logik.figure import Figure
except ImportError as err:
    print("ImportError "+str(err))
    sys.exit()

class FigureTest(unittest.TestCase):

    def test_wrong_argument_types(self):
        with self.assertRaises(Exception):
            Figure(2, Position("A", 2))
        with self.assertRaises(Exception):
            Figure("w", "not a Position Object")
        with self.assertRaises(Exception):
            tmp = Figure("w", Position("A", 2))
            tmp.do_move("not a Position Object")
