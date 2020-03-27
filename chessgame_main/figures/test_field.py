# pylint: disable=C
import unittest
try:
    from field import Field
    from position import Position
    import sys
except ImportError:
    print("ImportError")
    sys.exit()

class FieldTest(unittest.TestCase):

    def __init__(self):
        self.test = "nothing"

    def test_overall(self):
        f = Field()
        f_pm = f.get_possible_moves(Position("A", 2))
        print(f_pm[0].get_pos_char())
        print(f_pm[1].get_pos_char())
        print(f_pm[0].get_pos_number())
        print(f_pm[1].get_pos_number())
        print(f.do_move(Position("A", 2), f_pm[0]))

ft = FieldTest()
ft.test_overall()