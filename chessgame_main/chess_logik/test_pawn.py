# pylint: disable=C
import unittest
import sys
try:
    from chess_logik.pawn import Pawn
    from chess_logik.position import Position
    from chess_logik import consts
except ImportError as err:
    print("ImportError"+str(err))
    sys.exit()

class PawnTest(unittest.TestCase):

    def test_get_pos(self):
        pos = Position("A", 2)
        f = Pawn(consts.COLOR_BLACK, pos)
        self.assertEqual(f.get_position(), pos)

    def test_wrong_argument_types(self):
        pass
