"""Test opponent_move
"""
import unittest

try:
    import sys
    import consts
    from computer_gegner.opponent_move import Opponent
    from chess_logik.position import Position
    from chess_logik.pawn import Pawn
except ImportError as err:
    print("ImportError "+str(err))
    sys.exit()

class OpponentTest(unittest.TestCase):
    """Tests the class Opponent
    """

    def test_1_bot_move(self):
        """Tests the method bot_move
        """
        opponent1 = Opponent()

        field1 = []
        field1.append(Pawn(consts.COLOR_WHITE, Position("A", 2)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("B", 4)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("E", 2)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("C", 5)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("E", 7)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("H", 7)))

        ret_val = opponent1.bot_move(field1)
        old_val = ret_val[0]
        old_val_char = list(old_val)[0]
        old_val_num = int(list(old_val)[1])
        self.assertIn(ord(old_val_char)-65, range(8))
        self.assertIn(old_val_num, range(1, 9))

        new_val = ret_val[1]
        new_val_char = list(new_val)[0]
        new_val_num = int(list(new_val)[1])
        self.assertIn(ord(new_val_char)-65, range(8))
        self.assertIn(new_val_num, range(1, 9))


        field2 = []
        field2.append(Pawn(consts.COLOR_WHITE, Position("A", 2)))
        field2.append(Pawn(consts.COLOR_WHITE, Position("B", 2)))
        field2.append(Pawn(consts.COLOR_WHITE, Position("C", 2)))
        field2.append(Pawn(consts.COLOR_BLACK, Position("E", 4)))
        field2.append(Pawn(consts.COLOR_BLACK, Position("A", 7)))
        field2.append(Pawn(consts.COLOR_BLACK, Position("B", 7)))
        field2.append(Pawn(consts.COLOR_BLACK, Position("H", 7)))
        field2.append(Pawn(consts.COLOR_BLACK, Position("D", 7)))
        field2.append(Pawn(consts.COLOR_WHITE, Position("F", 3)))
        field2.append(Pawn(consts.COLOR_WHITE, Position("C", 7)))

        ret_val = opponent1.bot_move(field2)
        old_val = ret_val[0]
        old_val_char = list(old_val)[0]
        old_val_num = int(list(old_val)[1])
        self.assertIn(ord(old_val_char)-65, range(8))
        self.assertIn(old_val_num, range(1, 9))

        new_val = ret_val[1]
        new_val_char = list(new_val)[0]
        new_val_num = int(list(new_val)[1])
        self.assertIn(ord(new_val_char)-65, range(8))
        self.assertIn(new_val_num, range(1, 9))


        field3 = []
        field3.append(Pawn(consts.COLOR_WHITE, Position("A", 2)))
        field3.append(Pawn(consts.COLOR_WHITE, Position("B", 2)))
        field3.append(Pawn(consts.COLOR_WHITE, Position("C", 2)))
        field3.append(Pawn(consts.COLOR_BLACK, Position("A", 7)))
        field3.append(Pawn(consts.COLOR_BLACK, Position("B", 7)))
        field3.append(Pawn(consts.COLOR_BLACK, Position("C", 7)))
        field3.append(Pawn(consts.COLOR_BLACK, Position("D", 7)))
        field3.append(Pawn(consts.COLOR_WHITE, Position("D", 2)))
        field3.append(Pawn(consts.COLOR_WHITE, Position("E", 2)))
        field3.append(Pawn(consts.COLOR_WHITE, Position("F", 2)))
        field3.append(Pawn(consts.COLOR_BLACK, Position("E", 7)))
        field3.append(Pawn(consts.COLOR_BLACK, Position("F", 7)))
        field3.append(Pawn(consts.COLOR_WHITE, Position("G", 2)))
        field3.append(Pawn(consts.COLOR_BLACK, Position("G", 7)))
        field3.append(Pawn(consts.COLOR_WHITE, Position("H", 2)))
        field3.append(Pawn(consts.COLOR_BLACK, Position("H", 7)))

        ret_val = opponent1.bot_move(field3)
        old_val = ret_val[0]
        old_val_char = list(old_val)[0]
        old_val_num = int(list(old_val)[1])
        self.assertIn(ord(old_val_char)-65, range(8))
        self.assertIn(old_val_num, range(1, 9))

        new_val = ret_val[1]
        new_val_char = list(new_val)[0]
        new_val_num = int(list(new_val)[1])
        self.assertIn(ord(new_val_char)-65, range(8))
        self.assertIn(new_val_num, range(1, 9))

    def test_2_diagonal_left(self):
        """Tests the method diagonal_left
        """
        opponent2 = Opponent()
        self.assertEqual(opponent2.diagonal_left(Position("A", 7)), "x")
        self.assertEqual(opponent2.diagonal_left(Position("D", 3)), "C2")
        self.assertEqual(opponent2.diagonal_left(Position("H", 5)), "G4")

    def test_3_diagonal_right(self):
        """Tests the method diagonal_right
        """
        opponent3 = Opponent()
        self.assertEqual(opponent3.diagonal_right(Position("A", 7)), "B6")
        self.assertEqual(opponent3.diagonal_right(Position("D", 3)), "E2")
        self.assertEqual(opponent3.diagonal_right(Position("H", 5)), "x")

    def test_4_select_pawn_move(self):
        """Tests the method select_pawn_move with diagonal_left
        """

        opponent4 = Opponent()

        field1 = []
        field1.append(Pawn(consts.COLOR_WHITE, Position("A", 2)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("B", 4)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("E", 2)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("C", 5)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("E", 7)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("H", 7)))

        self.assertEqual(opponent4.select_pawn_move(field1, 3), "B4")

    def test_5_select_pawn_move(self):
        """Tests the method select_pawn_move with diagonal_right
        """

        opponent5 = Opponent()

        field1 = []
        field1.append(Pawn(consts.COLOR_WHITE, Position("A", 2)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("B", 2)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("C", 2)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("A", 7)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("B", 7)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("H", 7)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("D", 7)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("F", 3)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("E", 4)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("C", 7)))

        self.assertEqual(opponent5.select_pawn_move(field1, 8), "F3")

    def test_6_select_pawn_move(self):
        """Tests the method select_pawn_move with normal move
        """

        opponent6 = Opponent()

        field1 = []
        field1.append(Pawn(consts.COLOR_WHITE, Position("A", 2)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("B", 2)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("C", 2)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("A", 7)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("B", 7)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("C", 7)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("D", 7)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("D", 2)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("E", 2)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("F", 2)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("E", 7)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("F", 7)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("G", 2)))
        field1.append(Pawn(consts.COLOR_WHITE, Position("H", 2)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("G", 7)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("H", 7)))

        self.assertEqual(opponent6.select_pawn_move(field1, 14), "G6")

    def test_7_select_pawn_move(self):
        """Tests the method select_pawn_move with no move possible
        """

        opponent7 = Opponent()

        field1 = []
        field1.append(Pawn(consts.COLOR_WHITE, Position("A", 4)))
        field1.append(Pawn(consts.COLOR_BLACK, Position("A", 5)))

        self.assertEqual(opponent7.select_pawn_move(field1, 1), "x")
