# pylint: disable=C
import unittest
import sys
try:
    from chess_logik.position import Position
except ImportError as err:
    print("ImportError "+str(err))
    sys.exit()

class PositionTest(unittest.TestCase):

    def test_normal_init_and_getter(self):
        for char in "ABCDEFGH":
            for num in range(1,9):
                assert self.assertEqual(Position(char,num).get_pos_number(), num)
                assert self.assertEqual(Position(char,num).get_pos_char(), char)

    def test_error_codes(self):
        for num in range(1,9):
            assert self.assertEqual(Position("@",num).get_pos_number(), num)
            assert self.assertEqual(Position("@",num).get_pos_char(), "Error:char")
            assert self.assertEqual(Position("I",num).get_pos_number(), num)
            assert self.assertEqual(Position("I",num).get_pos_char(), "Error:char")
        for char in "ABCDEFGH":
            assert self.assertEqual(Position(char,0).get_pos_number(), "Error:number")
            assert self.assertEqual(Position(char,0).get_pos_char(), char)
            assert self.assertEqual(Position(char,9).get_pos_number(), "Error:number")
            assert self.assertEqual(Position(char,9).get_pos_char(), char)

    def test_wrong_argument_types(self):
        with self.assertRaises(Exception):
            Position("A2", 2)
        with self.assertRaises(Exception):
            Position("A", "2")
        with self.assertRaises(Exception):
            Position(6, 2)
